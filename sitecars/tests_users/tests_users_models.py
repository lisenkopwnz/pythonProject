import pytest
from users.models import User


class Test_model_user:
    @pytest.fixture
    def users(self, db):
        User.objects.create(username='Денис', first_name='Иванов', last_name='Иванович', email='dii@.com',
                            password='123')

    def test_user_create(self, users):
        user = User.objects.filter(username='Денис').exists()
        assert user == True

    def test_verbose_name_photo(self, users):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('photo').verbose_name
        assert field_label == 'Фотография'

    def test_value_photo(self, users):
        user = User.objects.get(id=1)
        field_name = user._meta.get_field('photo')
        field_value = str(getattr(user, field_name.attname))
        assert field_value == ''
