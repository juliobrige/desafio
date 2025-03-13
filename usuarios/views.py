from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class cadastro (View):
    def get(self, request):
        return HttpResponse('teste')
