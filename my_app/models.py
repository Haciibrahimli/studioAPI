from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.generator import Generator
from services.uploader import Uploader
from django.contrib.auth import get_user_model 
from services.extract import extract_google_maps_url_from_iframe


SOCIAL_CHOICES = (
    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp", "WhatsApp"),
    ("twitter", "Twitter"),
    ("linkedin", "Linkedin"),
    ("tiktok", "Tiktok")
)

User = get_user_model()



COUNTRY_CHOICES = (
    ("usa", "Amerika"),
    ("az", "Azerbaijan"),
    ("eu", "Europa"),
    ("as", "Asia"),
    
    
)

# User = get_user_model()


# Create your models here.
class About(DateMixin):
    subject1 = models.TextField(verbose_name = 'subject')
    image1 = models.ImageField(upload_to=Uploader.upload_photo_about,null=True,blank=True)
    # slogan 
    subject2 = models.TextField(verbose_name = 'subject')
    image2 = models.ImageField(upload_to=Uploader.upload_photo_about,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
     ordering = ('-created_at',)
     verbose_name = 'category'
     verbose_name_plural = 'categories'



class Team(DateMixin):
      name = models.TextField(verbose_name = 'iscinin adi')
      profession = models.CharField(max_length=255,verbose_name = 'peshesi')
      image = models.ImageField(upload_to=Uploader.upload_photo_team,null=True,blank=True)
      imagehover = models.ImageField(upload_to=Uploader.upload_photo_team,null=True,blank=True)

      def __str__(self):
        return self.name

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'reng'
       verbose_name_plural = 'rengler'


class OurServices(SlugMixin, DateMixin):
    name = models.TextField(verbose_name = 'mehsulun olcusu')
    text = models.TextField(verbose_name = 'metn')

    def __str__(self):
       return self.name

    class Meta:
       ordering = ('-created_at',)
       verbose_name = 'olcu'
       verbose_name_plural = 'olculer'


    def save(self, *args, **kwargs):
       if not self.slug:
        self.slug = Generator.create_slug_shortcode(size=10, model_= OurServices)
       super(OurServices, self).save(*args, **kwargs)

 


class Projects(SlugMixin, DateMixin):
     name = models.CharField(max_length = 255,verbose_name = 'mehsulun adi')
     image = models.ImageField(upload_to=Uploader.upload_photo_projects,null=True,blank=True)
    

     def __str__(self):
        return self.name

     class Meta:
       ordering = ('-created_at',)
       verbose_name = 'mehsul'
       verbose_name_plural = 'mehsullar'


     def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Projects)
        super(Projects, self).save(*args, **kwargs)

    

 
        
class Partniors(DateMixin):
      image = models.ImageField(upload_to=Uploader.upload_photo_partniors,null=True,blank=True)
      
      def __str__(self):
        return f'{self.created_at}'

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'partnior sekil'
       verbose_name_plural = 'partnior sekiller'


class Contact(SlugMixin, DateMixin):
       
    name = models.CharField(max_length=255,verbose_name='ad ve soyad')
    email = models.CharField(max_length=255,verbose_name='email adress')
    subject = models.CharField(max_length=255,verbose_name='movzu')
    mesage = models.TextField(verbose_name='mesaj')
    
    
   
    def __str__(self):
        return self.name
    
    class Meta:

     ordering = ('name',)
     verbose_name = 'contact'
     verbose_name_plural = 'contactlar'



    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Contact)
        super(Contact, self).save(*args, **kwargs)



class Checkout(SlugMixin, DateMixin):
       name = models.CharField(max_length = 255,verbose_name = 'ad')
       surname = models.CharField(max_length = 255,verbose_name = 'soyad')
       email = models.CharField(max_length = 255,verbose_name = 'email')
       phone = models.CharField(max_length = 255, verbose_name = 'telefon')
       adress1 = models.CharField(max_length = 255, verbose_name = 'adress 1')
       adress2 = models.CharField(max_length = 255, verbose_name = 'adress 2')
       country = models.CharField(max_length=255,verbose_name='olke adlari',choices=COUNTRY_CHOICES)
       city = models.CharField(max_length = 255,verbose_name = 'sheher adi')
       state  = models.CharField(max_length = 255,verbose_name = 'dovlet')
       zipcode = models.CharField(max_length = 255, verbose_name = 'olke kodu')

       def __str__(self):
         return self.name
    
       class Meta:
        ordering = ('name',)
        verbose_name = 'checkout'
        verbose_name_plural = 'checkout'


       def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_= Checkout)
        super(Checkout, self).save(*args, **kwargs)



class SosialMedia(DateMixin):
    sosial_name = models.CharField(max_length=255,verbose_name='sosial media hesabi',choices=SOCIAL_CHOICES)
    sosial_link = models.TextField(verbose_name='sosial media linki')

    def __str__(self):
        return self.sosial_name

    class Meta:
        ordering = ("sosial_name", )
        verbose_name = "sosial media hesabi"
        verbose_name_plural = "sosial media hesablari"


class MainDetails(SlugMixin, DateMixin):
    email = models.EmailField(verbose_name='Email')
    adresss = models.CharField(max_length=255,verbose_name='adress' )
    phones = models.CharField(max_length=255,verbose_name='phones')
    locations = models.TextField(verbose_name='locations',null=True,blank=True)
    
  
    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "elaqe melumati"
        verbose_name_plural = "elaqe melumatlari"


    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=MainDetails)
        super(MainDetails, self).save(*args, **kwargs)
