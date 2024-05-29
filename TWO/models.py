from django.db import models

class MyModel(models.Model):
    STATUS_CHOICES = [
        ('HIGH', 'high'),
        ('LOW', 'low'),
        ('COMPLETED', 'Completed'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='NEW')
    message = models.TextField(default='Default message')
    id_status = models.IntegerField()
    current_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.status}"
