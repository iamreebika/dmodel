from django.db import models
from location_field.models.plain import PlainLocationField


# Create your models here.
class Location(models.Model):
   city = models.CharField(max_length=255)
   location = PlainLocationField(based_fields=['city'], zoom=7)

class Properties(models.Model):
    STATUS_CHOICE=[
        ('FS','For Sale'),
        ('SO','Sold'),
    ]
    id = models.AutoField(primary_key=True)
    property_name = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=30, decimal_places=2)
    property_status = models.CharField(max_length = 20,
        choices = STATUS_CHOICE,
        default = '1'
        )
    property_holder = models.CharField(max_length=100)
    location_id =  models.OneToOneField(
        Location,
        on_delete=models.CASCADE,

    )
    def __str__(self):
        return self.property_name


class PropertiesDetail(models.Model):

    area = models.PositiveIntegerField()
    properties_id = models.ForeignKey(Properties,on_delete=models.CASCADE)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    avaliable_from = models.DateField()
    def __str__(self):
        return self.avaliable_from

class Social_Amenities(models.Model):
    GAME_CHOICE=[
        ('ID','IndoorGames'),
        ('VB','VolleyBall'),
        ('BB','BasketBallCourt'),
         ('A','AllAbove'),
    ]

    properties_id =models.ManyToManyField(Properties)
    water_supply = models.TimeField(auto_now=False)
    play_area = models.PositiveIntegerField()
    health_facilities=models.CharField(max_length=100)
    game=   models.CharField(max_length = 20,
        choices = GAME_CHOICE,
        default = '1'
        )
    swimming_pool=models.BooleanField(default=True, verbose_name="There is SwimmingPool")
    cctv_camera = models.BooleanField(default=True)
    gyms = models.BooleanField(default=True)
    lift = models.BooleanField(default=True)
    parking = models.BooleanField(default=True,verbose_name="There is covered car parking")
    def __str__(self):
        return self.water_supply

class FieldVisit(models.Model):

    name = models.CharField(max_length=100,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.name










class Gallery(models.Model):

    image = models.ImageField(upload_to='upload',blank=True)




