from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from services.db.users import get_user, get_user_by_id
# from django.contrib.auth import login


class AuthBackend():
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):
        # login_valid = (settings.ADMIN_LOGIN == username)
        # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        # if login_valid and pwd_valid:
        # try:
        user = get_user(username=username)
        user['backend'] = 'app_auth.auth_backend.AuthBackend'
        print('============================')
        # except User.DoesNotExist:
        # Create a new user. There's no need to set a password
        # because only the password from settings.py is checked.
        # user = User(username=username)
        # user.is_staff = True
        # user.is_superuser = True
        # user.save()
        return user
        # return None

    def get_user(self, user_id):
        # try:
        return get_user_by_id(id=user_id)
        # except User.DoesNotExist:
        #    return None