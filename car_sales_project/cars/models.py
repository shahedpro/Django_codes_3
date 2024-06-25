from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name}'
