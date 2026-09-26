from django.db import models

# Create your models here.

class Student(models.Model):
    image = models.ImageField(upload_to='student-images/')
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50, blank=True, null=True)
    yosh = models.IntegerField(default=15)
    manzil = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism} --- {self.familiya}"
