from django.db import models
from routers.models import Router
from templates_config.models import ConfigTemplate

class DeploymentJob(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]

    router = models.ForeignKey(Router, on_delete=models.CASCADE, related_name='jobs')
    template = models.ForeignKey(ConfigTemplate, on_delete=models.SET_NULL, null=True)
    variables = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    output_log = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.router.name} - {self.template.name} - {self.status}"
