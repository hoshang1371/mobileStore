from djoser import email
from djoser import utils
from djoser.conf import settings
from django.contrib.auth.tokens import default_token_generator
from decouple import config

FRONT_URL = config('FRONT_URL')
class ActivationEmail(email.ActivationEmail):
    template_name = 'account/ActivationEmail.html'

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["frontUrl"] = FRONT_URL
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.ACTIVATION_URL.format(**context)
        # context["url"] = "http://localhost:8080/".format(**context)
        return context


class ConfirmationEmail(email.ConfirmationEmail):
    template_name = 'account/ConfirmationEmail.html'


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = "account/password_reset.html"

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()

        user = context.get("user")
        print(user.pk)
        context["uid"] = utils.encode_uid(user.pk)
        context["frontUrl"] = FRONT_URL
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        return context


class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name = "account/password_changed_confirmation.html"