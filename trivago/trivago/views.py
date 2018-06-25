from django.shortcuts import redirect,reverse


def login_redirect(requests):
    return redirect(reverse('hotel:home'))
