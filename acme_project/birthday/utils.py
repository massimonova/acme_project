from datetime import date


def calculate_birthday_countdown(birthday):
    """
    Возвращает количество дней до следующего дня рождения.

    Если день рождения сегодня, то возвращает 0.
    """
    today = date.today()
    # Получаем день рождения в этом году с помощью вспом. функции
    this_year_birthday = get_birthday_for_year(birthday, today.year)

    # Если день рождения уже прошёл:
    if this_year_birthday < today:
        next_birthday = get_birthday_for_year(birthday, today.year + 1)
    else:
        # Если ДР не было, то он будет следующим
        next_birthday = this_year_birthday

    # Считаем разницу между следующим днём рождения и сегодняшним в днях.
    birthday_countdown = (next_birthday - today).days
    return birthday_countdown


def get_birthday_for_year(birthday, year):
    """
    Получает дату дня рождения для конкретного года.

    Ошибка ValueError Возможна только в случаве с високосными
    годами и ДР 29 февраля.
    В этом случае приравниваем дату ДР к 1 марта.
    """
    try:
        # Пробуем заменить год в дате рождения на переданный в функцию.
        calculate_birthday = birthday.replace(year=year)
    # Если возникла ошибка, значит др 29 февраля
    # и подставляемый год н являетс я високосным.
    except ValueError:
        # В этом случае устанавливаем ДР на 1 марта.
        calculate_birthday = date(year=year, month=3, day=1)
    return calculate_birthday
