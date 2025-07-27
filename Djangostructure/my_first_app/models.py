from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class App(models.Model):
    CHAI_TYPES_CHOICE = [
        ('ML', 'MASALA'),
        ('GN', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPES_CHOICE, default='PL')
    description=models.TextField(default='')
    def __str__(self):
        return self.name
#one_to_many

class ChaiReview(models.Model):
    chai= models.ForeignKey(App,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    RATING_CHOICE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    rating=models.IntegerField(choices=RATING_CHOICE, default='5')
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    # Many_to_Many

class store(models.Model):
        name=models.CharField(max_length=100)
        location=models.CharField(max_length=100)
        chai_varieties=models.ManyToManyField(App,related_name='stores')
        def __str__(self):
            return self.name
        
        # One_To_One
class ChaiCertificate(models.Model):
    chai=models.OneToOneField(App,on_delete=models.CASCADE,related_name="certificate")
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now)
    valid_until=models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.name.my_first_app}"