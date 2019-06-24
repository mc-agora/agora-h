from django.db import models

class laws(models.Model):
    law_num = models.CharField(max_length=200)
    law_name = models.CharField(max_length=200)
    law_attribute = models.CharField(max_length=200)
    law_condition = models.CharField(max_length=200)
    law_department = models.CharField(max_length=200)
    law_status = models.CharField(max_length=200)
    page_num_num = models.CharField(max_length=200)

    def __str__(self):
    	return f'<{self.law_num}/{self.law_name}/{self.law_attribute}/{self.law_condition}/{self.law_department}/{self.law_status}/{self.page_num_num})>'