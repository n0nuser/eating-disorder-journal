from django import template
from datetime import datetime, date, time
from json import loads

register = template.Library()


@register.filter()
def field_name_to_label(value):
    return value.replace("_", " ").capitalize()


@register.filter()
def typeof(value):
    return str(type(value))

@register.filter()
def weekday(value):
    day = {
        "1": "Sunday",
        "2": "Monday",
        "3": "Tuesday",
        "4": "Wednesday",
        "5": "Thursday",
        "6": "Friday",
        "7": "Saturday",
    }
    return day[str(value)]

@register.filter()
def parse_value(value):
    if isinstance(value, datetime):
        return value.strftime("%d/%m/%Y %H:%M:%S")
    elif isinstance(value, date):
        return value.strftime("%d/%m/%Y")
    elif isinstance(value, time):
        return value.strftime("%H:%M:%S")
    elif isinstance(value, float):
        return round(value, 2)
    elif callable(value):
        return value()
    else:
        return value


@register.filter
def get_obj_attr(obj, attr):
    """
    Improvement of https://stackoverflow.com/a/32158083/16612992 for foreign keys.
    """
    # Get data from a foreign key
    if "__" in attr:
        attr = attr.split("__")
        for a in attr:
            obj = getattr(obj, a)
        return obj
    # Return field value
    return getattr(obj, attr)


@register.filter()
def todict(value):
    try:
        return loads(value.replace("'", '"'))
    except Exception:
        return value


@register.filter
def currency(value):
    if value is None:
        return None
    value = "{:,.2f}€".format(value)
    main_currency, fractional_currency = value.split(".")[0], value.split(".")[1]
    new_main_currency = main_currency.replace(",", ".")
    return f"{new_main_currency},{fractional_currency}"


@register.filter
def subtract(value, arg):
    return value - arg
