from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    persName = models.CharField(max_length=25)
    persFirstname = models.CharField(max_length=25)
    persText = models.TextField()
    persCompetencies = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.persName} {self.persFirstname} : {self.persText} {self.persCompetencies} {self.user}" 

class SubjectBlog(models.Model):
    subjName = models.CharField(max_length=128)
    subjCreationDate = models.DateField()
    subjEdited_date =models.DateField()
    subjTextmessage = models.TextField()

    def __str__(self):
        return f"{self.subjName} {self.subjCreationDate}: {self.subjEdited_date} {self.subjTextmessage}" 

class CommentBlog(models.Model):
    commPosted_date = models.DateField()
    commEdited_date =models.DateField()
    commTextmessage = models.TextField()
    subject = models.ForeignKey(SubjectBlog, on_delete=models.DO_NOTHING,null=False,blank=True)
    def __str__(self):
        return f"{self.messPosted_date} + {self.messEdited_date}, {self.messTextmessage}" 

   
    
