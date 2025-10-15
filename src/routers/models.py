from django.db import models

class Router(models.Model):
    ROLE_CHOICES = [
        ('main', 'Main Hub Router'),
        ('branch', 'Branch Router'),
    ]

    name = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)  # later we’ll encrypt this
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='branch')
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"
