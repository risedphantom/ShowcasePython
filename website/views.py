from django.http import HttpResponse
from django.template import loader
import platform
import psutil


# Index page
def index(request):
    template = loader.get_template('website/index.html')
    context = {
        'title': 'Панов Антон, Менеджер продукта',
    }
    return HttpResponse(template.render(context, request))


# Resume page
def resume(request):
    template = loader.get_template('website/resume.html')
    context = {
        'title': 'Резюме',
    }
    return HttpResponse(template.render(context, request))


# Portfolio page
def portfolio(request):
    template = loader.get_template('website/portfolio.html')
    context = {
        'title': 'Портфолио',
    }
    return HttpResponse(template.render(context, request))


# WhatIUse page
def uses(request):
    template = loader.get_template('website/whatIUse.html')
    context = {
        'title': 'Что я использую',
    }
    return HttpResponse(template.render(context, request))


# Contacts page
def contacts(request):
    template = loader.get_template('website/contacts.html')
    context = {
        'title': 'Контакты',
    }
    return HttpResponse(template.render(context, request))


# About page
def about(request):
    template = loader.get_template('website/about.html')
    context = {
        'title': 'Об этом сайте',
        'os_type': platform.system(),
        'os_arch': platform.machine(),
        'os_platform': platform.platform(),
        'os_freemem': int(psutil.virtual_memory().free / 1048576),
        'os_totalmem': int(psutil.virtual_memory().total / 1048576),
        'os_cpu': platform.processor(),
    }
    return HttpResponse(template.render(context, request))


# Error page
def error(request):
    template = loader.get_template('website/error.html')
    context = {
        'title': 'Страница не найдена',
    }
    return HttpResponse(template.render(context, request))
