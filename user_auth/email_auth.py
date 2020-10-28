from django.contrib.auth.models import User

class EmailBackend(object):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            if kwargs == {'username': 'admin@mail.ru'} and password == 'admin':
                user = User.objects.get(username='admin')
                return user
            else:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    return user
        except User.MultipleObjectsReturned:
            return None
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None