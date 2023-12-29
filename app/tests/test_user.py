from django.urls import reverse
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


def test_auth_view(client, create_user):
    user = create_user(username='john', password='cena')

    url = reverse('profile-page')

    client.login(username=user.username, password= 'cena')

    response = client.get(url)

    assert response.status_code == 200


@pytest.fixture
def auto_login_user(db, client, create_user):
    def make_auto_login(**kwargs):
        user = create_user(username=kwargs['username'], password=kwargs['password'])

        client.login(username=user.username, password=kwargs['password'])
        
        return client, user
    
    return make_auto_login

def test_auto_login_auth_view(auto_login_user):
    client, user = auto_login_user(username='john', password='cena')

    url = reverse('profile-page')

    response = client.get(url)

    assert response.status_code == 200