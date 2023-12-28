import pytest
from django.contrib.auth.models import User

def test_create_user(django_user_model):
    django_user_model.objects.create(username='john', password='password')

    user = django_user_model.objects.get(username='john')

    assert user != None
    assert user.username == 'john'


# Custom Fixture
    
@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    
    return make_user


def test_user_create_with_custom_fixture(create_user):
    create_user(username='shira', password='password')

    user = User.objects.get(username='shira')

    assert user != None
    assert user.username == 'shira'
