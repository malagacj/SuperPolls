from django.db import models
from django.conf import settings


class Question(models.Model):
    text = models.CharField(max_length=200)
    answered_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='questions'
    )

    # Auditing fields
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_questions'
    )

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='updated_questions'
    )


class Option(models.Model):
    question = models.ForeignKey(Question,
        on_delete=models.SET_NULL,
        null=True
    )
    text = models.CharField(max_length=100)


class Answer(models.Model):
    uuid = models.UUIDField()
    option = models.ManyToManyField(Option)

    # Auditing fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
