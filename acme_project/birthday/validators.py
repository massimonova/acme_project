from datetime import date
from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    # Считаем разницу между сегодняшним днём и днём рождения в днях
    # и делим на 365
    age = (date.today() - value).days / 365
    if not (1 <= age <= 120):
        raise ValidationError(
            'Ожидается возраст от 1 года до 120 лет'
        )
