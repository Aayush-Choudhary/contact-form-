from django.views import generic
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

class main(View):
    def get(self, request):
        return HttpResponseRedirect('https://aayush-choudhary.github.io/404.html')