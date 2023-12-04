from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Message

def index(request):
    return render(request, 'index.html')
    
def get(request):
    messages = Message.objects.all()
    return JsonResponse({"messages":list(messages.values())})

def send(request):
    username = request.POST['username']
    text = request.POST['text']
    new_message = Message(username=username, text=text)
    if (new_message.is_valid()):
        new_message.save()
        return HttpResponse('Message sent successfully')
    return HttpResponse('Message sent unsuccessful')
