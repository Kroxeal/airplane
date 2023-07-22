from django.db.models import TextChoices


class SexTypes(TextChoices):
    M = 'male'
    F = 'female'


class StatusChoices(TextChoices):
    P = 'paid'
    U = 'unpaid'
    R = 'rejected'
