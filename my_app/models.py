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



# User = get_user_model()


# Create your models here.
class About(DateMixin):
    subject1 = models.TextField(verbose_name = 'subject')
    image1 = models.ImageField(upload_to=Uploader.upload_photo_about,null=True,blank=True)
    slogan = models.ImageField(upload_to=Uploader.upload_photo_about,null=True,blank=True)
    subject2 = models.TextField(verbose_name = 'subject')
    image2 = models.ImageField(upload_to=Uploader.upload_photo_about,null=True,blank=True)

    def __str__(self):
        return self.subject1    

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
       verbose_name = 'team'
       verbose_name_plural = 'teams'


class OurServices(SlugMixin, DateMixin):
    name = models.TextField(verbose_name = 'adi')
    text = models.TextField(verbose_name = 'metn')

    def __str__(self):
       return self.name

    class Meta:
       ordering = ('-created_at',)
       verbose_name = 'bizim xidmet'
       verbose_name_plural = 'bizim xidmetler'


    def save(self, *args, **kwargs):
       if not self.slug:
        self.slug = Generator.create_slug_shortcode(size=10, model_= OurServices)
       super(OurServices, self).save(*args, **kwargs)

 
class Partniors(DateMixin):
      image = models.ImageField(upload_to=Uploader.upload_photo_partniors,null=True,blank=True)
      
      def __str__(self):
        return f'{self.created_at}'

      class Meta:
       ordering = ('-created_at',)
       verbose_name = 'partnior sekil'
       verbose_name_plural = 'partnior sekiller'


class Contact(SlugMixin, DateMixin): #create
       
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


class BlogCategory(DateMixin ):
    name = models.CharField(max_length = 255,verbose_name = 'adi')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "blog category"
        verbose_name_plural = "blog categories"


class Blog(DateMixin,SlugMixin): #list,create retrive
        title = models.CharField(max_length = 255,verbose_name = 'blog')
        image = models.ImageField(upload_to=Uploader.upload_photo_blog,null=True,blank=True)
        information = models.TextField(verbose_name = 'melumat')
        user = models.CharField(max_length = 255,verbose_name = 'istifadeci')
        blog_category = models.ForeignKey(BlogCategory,on_delete=models.SET_NULL, null=True, blank=True)

   
        def __str__(self):
          return self.title
 
        class Meta:
          ordering = ("-created_at", )
          verbose_name = "blog"
          verbose_name_plural = "bloglar"


        def save(self, *args, **kwargs):
             if not self.slug:
              self.slug = Generator.create_slug_shortcode(size=10, model_= Blog)
             super(Blog, self).save(*args, **kwargs)

class Projects(SlugMixin, DateMixin):
     name = models.CharField(max_length = 255,verbose_name = 'mehsulun adi')
     image1 = models.ImageField(upload_to=Uploader.upload_photo_projects,null=True,blank=True)
     image2 = models.ImageField(upload_to=Uploader.upload_photo_projects,null=True,blank=True)
     project_category = models.ForeignKey(BlogCategory,on_delete=models.SET_NULL, null=True, blank=True)
     text = models.TextField(verbose_name = 'metn',null=True,blank=True)
     image3 = models.ImageField(upload_to=Uploader.upload_photo_projects,null=True,blank=True)
     image4 = models.ImageField(upload_to=Uploader.upload_photo_projects,null=True,blank=True)
     
    

     def __str__(self):
        return self.name

     class Meta:
       ordering = ('-created_at',)
       verbose_name = 'project'
       verbose_name_plural = 'projects'


     def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=Projects)
        super(Projects, self).save(*args, **kwargs)
