from django.db import models

class AboutMe(models.Model):
    abtName = models.CharField(max_length=25)
    abtFirstname = models.CharField(max_length=25)
    abtText = models.CharField(max_length=500)
    abtCompetencies = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.abtName} {self.abtFirstname}: {self.abtText}. {self.abtCompetencies}"

   
    
