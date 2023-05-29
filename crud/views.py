from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Person


class PersonBaseView(View):
    model = Person
    fields = ['name', 'age']
    success_url = "/"


class PersonListView(PersonBaseView, ListView):
    """Просмотреть список всех имен. Будем использовать переменную 'person_list' в шаблоне"""


class PersonCreateView(PersonBaseView, CreateView):
    """Создание новой персоны (Принимаем имя и возраст)"""


class PersonUpdateView(PersonBaseView, UpdateView):
    """Редактирование созданных записей"""


class PersonDeleteView(PersonBaseView, DeleteView):
    """Удаление созданной записи"""

