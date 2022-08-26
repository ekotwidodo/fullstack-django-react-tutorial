from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    menu_type = models.CharField(max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
            return self.name
