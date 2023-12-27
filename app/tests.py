import pytest
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user('John', 'john@gmail.com', 'password')

    assert User.objects.count() == 1
    assert user.username == 'John'

def test_view(client):
    url = reverse('index-page')
    response = client.get(url)

    assert response.status_code == 200