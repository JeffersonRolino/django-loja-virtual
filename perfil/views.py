from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Criar Perfil')


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar Perfil')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
