from django.db import models
from PIL import Image

class Product(models.Model):
    CLOTHES = 'clothes'
    SHOES = 'shoes'
    BAGS = 'bags'
    ACC = 'Accessories'

    CHOICE_GROUP = {
        (CLOTHES, 'clothes'),
        (SHOES, 'shoes'),
        (BAGS, 'bags'),
        (ACC, 'accessories')
    }

    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField()
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=CLOTHES)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')

    def __str__(self):
        return f'{self.name}'

# Create your models here.
