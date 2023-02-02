# from django.shortcuts import render

# from django.http import HttpResponse
# from django.views.generic import View
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previsious data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_title"] = "ГРОМКИЙ НОВОСТНОЙ ЗАГОЛОВОК"
        context["news_preview"] = "Предварительное описание новости, которое заинтересует каждого"
        context["range"] = range(1, 6)
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
