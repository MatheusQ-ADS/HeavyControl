from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CPFBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(cpf=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None