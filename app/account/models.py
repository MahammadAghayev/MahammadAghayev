from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser):
    username = models.CharField(_("username"), max_length=25, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True, null=True)
    image = models.ImageField(upload_to="accounts", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("account")
        verbose_name_plural = _("accounts")
    
    def __str__(self) -> str:
        return f"Account : {self.email}"


class SubscribedUser(models.Model):
    email = models.EmailField()
    subscribe_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("subscribed user")
        verbose_name_plural = _("subscribed users")

    def __str__(self):
        return self.email