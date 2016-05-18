from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name