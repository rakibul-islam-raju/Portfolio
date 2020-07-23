from django.db import models
  

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    portfolio_choices = (
        ('web', 'Web Development'),
        ('graphics', 'Graphics Design')
        )
    category = models.CharField(max_length=10, choices=portfolio_choices)
    image = models.ImageField()

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name} --> {self.company} --> {self.title}'


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} -> {self.email}'
