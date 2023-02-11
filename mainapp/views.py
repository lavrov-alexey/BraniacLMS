# from django.shortcuts import render

# from django.views.generic import View
# import json

# from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previsious data
        context = super().get_context_data(**kwargs)

        # вариант задания тестовой новости "вручную"
        # context["news_title"] = "ГРОМКИЙ НОВОСТНОЙ ЗАГОЛОВОК"
        # context["news_preview"] = "Предварительное описание новости, которое заинтересует каждого"
        # context["datetime_obj"] = datetime.now()
        # context["range"] = range(1, 6)

        # открываем файл с новостями на чтение (встроенными ср-ми Питона) и сохраняем в контекст список из новостей
        # with open(settings.BASE_DIR / "news.json") as news_file:
        # новости из списка будем перебирать в цикле в шаблоне news по полям
        # context["news_list"] = json.load(news_file)

        # вариант получения новостей из БД - получаем из таблицы news все новости и берем первые 5
        context["news_qs"] = mainapp_models.News.objects.all()[:5]

        return context

    # переопределим у контроллера метод get
    def get(self, *args, **kwargs):
        # если был передан get-параметр c ключом 'q' в словаре с get-параметрами поля запроса
        # - сохраняем его, если нет - None
        query = self.request.GET.get("q", None)
        if query:  # если запрос по ключу q был (не None), то делаем редирект на поисковую систему с фразой для поиска
            return HttpResponseRedirect(f"https://google.ru/search?q={query}")
        # если нет - продолжаем норм. работу контроллера
        return super().get(*args, **kwargs)


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context


class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesPageView, self).get_context_data(**kwargs)
        # тащим из БД все курсы и берем в контекст первые 7
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(course=context["course_object"])
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/../authapp/Templates/authapp/login.html"
