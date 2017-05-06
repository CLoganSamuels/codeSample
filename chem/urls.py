# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.output, name='output'),
        url(r'main', views.showMain, name='main'),
        url(r'removeCoefficients', views.showRemove, name='removeCoefficients'),
        url(r'moleculeSplit', views.showMoleculeSplit, name='moleculeSplit'),
        url(r'nullMath', views.showNullMath, name='nullMath'),
        url(r'out', views.showOut, name='out'),
        url(r'capLowNum', views.showCapLowNum, name='capLowNum'),
        url(r'populate', views.showPopulate, name='populate'),
]