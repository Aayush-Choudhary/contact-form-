from django.views import generic
from django.views.generic.base import View
from django.shortcuts import render, redirect
from api.models import contact as Contact
from django.http import HttpResponse, HttpResponseRedirect

class message(View):
    def get(self, request, content):
        content = content.split('$$$')
        name = content[0]
        name = ' '.join(name.split('--'))
        email = content[1]
        message = content[2]
        message = ' '.join(message.split('--'))
        addMessage = Contact(name=name, email=email, message=message)
        addMessage.save()
        return HttpResponseRedirect('https://aayush-choudhary.github.io/contact.html')