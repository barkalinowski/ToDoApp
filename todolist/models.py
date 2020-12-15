from django.db import models

class Task(models.Model):
	task_name = models.CharField(max_length = 500)
	task_status = models.BooleanField(default = False)
	task_date_created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.task_name