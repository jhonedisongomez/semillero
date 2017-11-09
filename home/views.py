# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin,TemplateView):
    template_name = "home/home.html"
    login_url = "/"
    class_form = ""

    def get(self, request, *args, **kwargs):

        print("hello")

    def post(self, request, *args, **kwargs):

        print("hello")
