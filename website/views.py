from django.shortcuts import render
import platform
import psutil


# Index page
def index(request):
    context = {
        'title': 'Панов Антон, Менеджер продукта',
    }
    return render(request, 'website/index.html', context)


# Resume page
def resume(request):
    context = {
        'title': 'Резюме',
    }
    return render(request, 'website/resume.html', context)


# Portfolio page
def portfolio(request):
    context = {
        'title': 'Портфолио',
    }
    return render(request, 'website/portfolio.html', context)


# WhatIUse page
def uses(request):
    context = {
        'title': 'Что я использую',
    }
    return render(request, 'website/whatIUse.html', context)


# Contacts page
def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'website/contacts.html', context)


# About page
def about(request):
    context = {
        'title': 'Об этом сайте',
        'os_type': platform.system(),
        'os_arch': platform.machine(),
        'os_platform': platform.platform(),
        'os_freemem': int(psutil.virtual_memory().free / 1048576),
        'os_totalmem': int(psutil.virtual_memory().total / 1048576),
        'os_cpu_percent': psutil.cpu_percent(),
    }
    return render(request, 'website/about.html', context)


# Error handling
def handler404(request):
    context = {
        'title': 'Страница не найдена'
    }
    return render(request, 'website/404.html', context, status=404)


def handler500(request):
    context = {
        'title': 'Ошибка'
    }
    return render(request, 'website/500.html', context, status=500)
