from django.db import models

# Create your models here.

class RawData(models.Model):
    raw_num = models.CharField(max_length=200)
    raw_name = models.CharField(max_length=200)
    raw_attribue = models.CharField(max_length=200)
    raw_condition = models.CharField(max_length=200)
    raw_department = models.CharField(max_length=200)
    raw_status = models.CharField(max_length=200)

    def __str__(self):
    	return f'<{self.raw_num}/{self.raw_name}/{self.raw_attribue}/{self.raw_condition}/{self.raw_department}/{self.raw_status}>'

class NumData(models.Model):
    page_num_num = models.CharField(max_length=200)

    def __str__(self):
        return f'<{self.page_num_num}>'

# Create your models here.

class LawData(models.Model):
    law_name = models.CharField(max_length=200)
    law_people = models.CharField(max_length=200)
    law_department = models.CharField(max_length=200)
    law_condition = models.CharField(max_length=200)
    law_date = models.CharField(max_length=200)
    law_doc_num = models.CharField(max_length=200)

    def __str__(self):
    	return f'<{self.law_name}/{self.law_people}/{self.law_department}/{self.law_condition}/{self.law_date}/{self.law_doc_num}>'

class LawNum(models.Model):
    page_num_num = models.CharField(max_length=200)

    def __str__(self):
        return f'<{self.page_num_num}>'


class ReguData(models.Model):
    total_num = models.CharField(max_length=200)
    trash_val = models.CharField(max_length=200)
    regu_name = models.CharField(max_length=200)
    regu_paper_num = models.CharField(max_length=200)
    regu_department = models.CharField(max_length=200)
    regu_dates = models.CharField(max_length=200)
    regu_status = models.CharField(max_length=200)
    regu_condition = models.CharField(max_length=200)
    regu_num = models.CharField(max_length=200)


    def __str__(self):
    	return f'<{self.total_num}/{self.trash_val}/{self.regu_name}/{self.regu_paper_num}/{self.regu_department}/{self.regu_dates}/{self.regu_status}/{self.regu_condition}/{self.regu_num}>'

class ReguNum(models.Model):
    Link_Page_num = models.CharField(max_length=200)

    def __str__(self):
        return f'<{self.Link_Page_num}>'

