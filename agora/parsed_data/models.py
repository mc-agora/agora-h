from django.db import models
from datetime import datetime
from django.conf import settings

# gov No. 법령명   법령종류  제개정구분  소관부처  추진현황
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

# assem   의안명   제안자   상임위원회  국회현황   의결현황    의안번호
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

# assem_regu    No.  법률안   규제조문수  소관부처  제안자 국회현황 추진현황  의안번호
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

class Pg_Board(models.Model):
    #raws = models.ForeignKey(RawData, on_delete=models.CASCADE, related_name='pg_board_raws')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=120)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, upload_to='documents/%Y/%m/%d')

class Pg_Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Pg_Board, on_delete=models.CASCADE, related_name='pd_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Pg_Board2(models.Model):
    #raws = models.ForeignKey(RawData, on_delete=models.CASCADE, related_name='pg_board_raws2')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=120)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, upload_to='documents/%Y/%m/%d')

class Pg_Comment2(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Pg_Board2, on_delete=models.CASCADE, related_name='pd_comments2')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

##########################################################################################
################################## 국회 ###################################################
##########################################################################################

class Pa_Board(models.Model):
    #laws = models.ForeignKey(LawData, on_delete=models.CASCADE, related_name='pa_board_laws')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=120)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, upload_to='documents/%Y/%m/%d')

class Pa_Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Pa_Board, on_delete=models.CASCADE, related_name='pa_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Pa_Board2(models.Model):
    #laws = models.ForeignKey(LawData, on_delete=models.CASCADE, related_name='pa_board_laws2')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=120)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, upload_to='documents/%Y/%m/%d')

class Pa_Comment2(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Pa_Board2, on_delete=models.CASCADE, related_name='pa_comments2')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

##########################################################################################
################################## 국회 규제 ###############################################
##########################################################################################

class Par_Board(models.Model):
    #regu = models.ForeignKey(ReguData, on_delete=models.CASCADE, related_name='par_board')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=120)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, upload_to='documents/%Y/%m/%d')

class Par_Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Par_Board, on_delete=models.CASCADE, related_name='par_comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Par_Board2(models.Model):
    #regu = models.ForeignKey(ReguData, on_delete=models.CASCADE, related_name='par_board2')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=120)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(null=True, upload_to='documents/%Y/%m/%d')

class Par_Comment2(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Par_Board2, on_delete=models.CASCADE, related_name='par_comments2')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)