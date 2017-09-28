from django.conf.urls import url
from . import views
from .core import ajax

urlpatterns = [
    # Views
    url(r'^$', views.index, name='index'),
    url(r'^uses/?$', views.uses, name='uses'),
    url(r'^index/?$', views.index, name='index'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^resume/?$', views.resume, name='resume'),
    url(r'^contacts/?$', views.contacts, name='contacts'),
    url(r'^portfolio/?$', views.contacts, name='portfolio'),

    # Methods
    url(r'^greeting/?$', ajax.greeting, name='greeting'),
]
