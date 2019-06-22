from django.db import models

# Create your models here.

class raws(models.Model):
    raw_num = models.CharField(max_length=200)
    raw_name = models.CharField(max_length=200)
    raw_attribue = models.CharField(max_length=200)
    raw_condition = models.CharField(max_length=200)
    raw_department = models.CharField(max_length=200)
    raw_status = models.CharField(max_length=200)
    page_num_num = models.CharField(max_length=200)

    def __str__(self):
    	return f'<{self.raw_num}/{self.raw_name}/{self.raw_attribue}/{self.raw_condition}/{self.raw_department}/{self.raw_status}/{self.page_num_num})>'