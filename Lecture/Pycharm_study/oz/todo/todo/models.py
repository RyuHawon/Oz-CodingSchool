from django.contrib.auth import get_user_model
from django.db import models
from datetime import date

User = get_user_model()

class Todo(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    start_date = models.DateField('Start Date', default=date.today)
    end_date = models.DateField('End Date', default=date.today)
    is_completed = models.BooleanField('Completed', default=False)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    modified_at = models.DateTimeField('Modified At', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo list'