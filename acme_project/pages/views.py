from django.views.generic import TemplateView
from birthday.models import Birthday


class HomePage(TemplateView):
    # В атрибуте template_name обязательно указывается имя шаблона,
    # на основе которго будет создана воззвращаемая страница.
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста из родительского метода.
        context = super().get_context_data(**kwargs)
        context['total_count'] = Birthday.objects.count()
        return context
