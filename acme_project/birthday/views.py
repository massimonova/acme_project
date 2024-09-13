from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy


class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV
    model = Birthday
    # Указываем сортировку, применяемую при выводе списка объектов
    ordering = 'id'
    # Настройки пагинации
    paginate_by = 10


# Добавляем миксин первым по списку родительских классов.
class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context
