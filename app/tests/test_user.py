import pytest


def test_create_user(django_user_model):
    django_user_model.objects.create(username='john', password='password')

    user = django_user_model.objects.get(username='john')

    assert user != None
    assert user.username == 'john'

