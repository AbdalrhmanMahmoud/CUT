
import random  # this for the short code

import string

from django.conf import settings


SHORTCODE_Min= getattr(settings, "SHORTCODE_Min",6)


def code_generator(size=SHORTCODE_Min, chars=string.ascii_lowercase + string.digits):  # generate random code

    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_Min):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code