from django.db import models

# Create your models here.
class worker(models.Model):
	worker_id = models.CharField(max_length=200)
	worker_ip = models.CharField(max_length=200)
	last_ping = models.DateTimeField('last ping')
	status = models.IntegerField(default=0)