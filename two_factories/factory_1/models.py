from django.db import models
from django.shortcuts import reverse


class Products1(models.Model):
    name = models.CharField(max_length=80)

    CHOICE_CATEGORY = [
        ('ice cream', 'ice cream'),
        ('candy', 'candy'),
        ('chocolate bar', 'chocolate bar'),
        ('cake', 'cake'),
        ('other', 'other'),
    ]

    category = models.CharField(max_length=80, choices=CHOICE_CATEGORY)
    price = models.PositiveIntegerField()
    availability = models.BooleanField()
    date_creation = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.category} {self.price} - {self.availability}"

    def get_absolute_url(self):
        return reverse('factory_1:product', kwargs={'product_id': self.pk})
