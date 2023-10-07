from django.db import models

class ExtractedText(models.Model):
    CATEGORY_CHOICES = (
        ('id', 'ID'),
        ('passport', 'Passport'),
        ('invoice', 'Invoice'),
    )
    name = models.CharField(max_length= 200, default="")
    text = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category} - {self.created_at}'