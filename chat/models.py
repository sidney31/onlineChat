from django.db import models

class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        return "" if val is None else val.isoformat("|", "minutes")

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sendDate = CustomDateTimeField(auto_now_add=True, db_index=True)
    username = models.CharField(max_length=150, db_index = True)
    text = models.CharField(max_length=150, db_index = True)

    def is_valid(self):
        return not (None or '') in list(vars(self).values())

    def __str__(self):
        return self.text
