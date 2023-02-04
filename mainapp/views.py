# from django.shortcuts import render

# from django.views.generic import View
import json

from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


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
        with open(settings.BASE_DIR / "news.json") as news_file:
            # новости из списка будем перебирать в цикле в шаблоне news по полям
            context["news_list"] = json.load(news_file)

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


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
