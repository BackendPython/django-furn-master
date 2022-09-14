from audioop import add
from django.db import models
from  django.contrib.auth.models import AbstractUser
from PIL import Image

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

class Profile(models.Model):
    class Meta:
        verbose_name = "My profile"
        verbose_name_plural = "Profile"
    sell = models.IntegerField(default=0)
    bio = models.CharField(max_length=100, default="biooo")
    phone_number = models.IntegerField(default=998949949494)
    custome_user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(default='arrivals5.png', upload_to = "profile")
    
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

class Carousel(models.Model):
    img = models.ImageField()
    slider_title = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    aboute = models.TextField(max_length=700)
    price = models.IntegerField(default=1)
    old_price = models.IntegerField(default=2)

    def __str__(self):
        return self.title

class Arrival(models.Model):
    arrivals_img = models.ImageField()
    arrivals_title = models.CharField(max_length=200)
    arrivals_url = models.URLField(max_length=500)
    arrivals_price = models.IntegerField(default=10)
    category = models.ForeignKey("Category", blank=True, on_delete=models.CASCADE)
    
    # for information
    
    arrvals_size = models.CharField(max_length=30)
    arrivals_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.arrivals_title

class Blog(models.Model):
    img = models.ImageField()
    date = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    aboute = models.TextField(max_length=700)
    title_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Product(models.Model):
    
    rate_1 = 1
    rate_2 = 2
    rate_3 = 3
    rate_4 = 4
    rate_5 = 5
    
    CONTACT_CHOICES = [
        (rate_1, 1),
        (rate_2, 2),
        (rate_3, 3),
        (rate_4, 4),
        (rate_5, 5),
    ]
    
    img = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=1)
    rate_1_choices = models.CharField(max_length=8, choices=CONTACT_CHOICES, default=rate_1)

    def __str__(self):
        return self.title

class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Category(models.Model):
    class Meta:
        verbose_name = 'My Category'
        verbose_name_plural = 'My Categorys bob'
        
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name

class Contact(models.Model):
    
    TAKLIF = 'Taklif'
    SUPPORT = 'Support'
    
    CONTACT_CHOICES = [
        (TAKLIF, 'Taklif'),
        (SUPPORT, 'Support'),
    ]
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    choices = models.CharField(max_length=8, choices=CONTACT_CHOICES, default=TAKLIF)
    mobile = models.IntegerField(default='+998')
    text = models.TextField(max_length=700)
    data = models.DateTimeField(auto_now=add)
    
    def __str__(self):
        return self.full_name



