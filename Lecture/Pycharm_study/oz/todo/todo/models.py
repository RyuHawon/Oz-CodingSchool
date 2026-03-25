from django.db import models

class Todo(models.Model):
    title = models.CharField('제목', max_length=50)
    description = models.TextField('설명')
    start_date = models.DateTimeField('시작일')
    end_date = models.DateTimeField('마감일')
    is_completed = models.BooleanField('완료여부', default=False)
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    modified_at = models.DateTimeField('수정일', auto_now=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo list'