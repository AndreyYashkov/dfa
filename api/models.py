from django.db import models
from django.conf import settings


class Photo(models.Model):

    title = models.CharField(verbose_name="title", db_index=True, max_length=64)
    date_created = models.DateTimeField(
        verbose_name="Creation date", auto_now_add=True, null=True
    )
    image = models.ImageField(upload_to="uploads/Photos/")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE
    )
