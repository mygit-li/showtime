from django.db import models


class Students(models.Model):
    ic_code = models.CharField(primary_key=True, max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    sex = models.CharField(max_length=10, blank=True, default='')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('create_time', )
        app_label = "ora1"
        db_table = 'my_students'
        managed = False
