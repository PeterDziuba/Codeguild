from django.db import models

class Flutt(models.Model):
    text = models.CharField(max_length=140)
    user = models.CharField(max_length=140)

    def __str__(self):
        return "{} : {}".format(self.user, self.text)

    def __repr__(self):
        return "{} : {}".format(self.user, self.text)