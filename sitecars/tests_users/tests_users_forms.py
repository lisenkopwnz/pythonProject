import pytest
from django.contrib.auth import get_user_model

from users.forms import Regestration_User_Form
from django import forms
import tempfile


class Test_regestration_User_Form:

    @pytest.fixture
    def setup(self, db):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name

        return image

    @pytest.mark.parametrize(
        'photo, username, first_name, last_name,email, password1, password2',
        [
            ('setup', 'Анатолий', 'Задорожний', 'Вячеславович', 'test@example.org', '260715aboba', '260715aboba')
        ]
    )
    def test_valid_regestration_form(self, setup, photo, username, first_name, last_name,
                                     email, password1, password2):
        data = {
            'photo': 'photo',
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'password1': 'password1',
            'password2': 'password2'
        }
        form = Regestration_User_Form(data=data)
        f = form.errors.as_data
        print(f)
        assert form.is_valid() is True
