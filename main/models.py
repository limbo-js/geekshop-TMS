from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    text = models.TextField(verbose_name='About')
    image = models.ImageField(verbose_name='Image', upload_to='photo')
    coast = models.PositiveIntegerField(help_text='in dollars')
    amount = models.PositiveIntegerField(help_text='number')

    def __str__(self):
        return self.name
