from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField(max_length=500, null=True)
    message = models.TextField(max_length=1000, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    name = models.CharField(max_length=10, null=False, default='visit')
    visit = models.IntegerField()

    def __str__(self):
        return self.name