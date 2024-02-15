# Generated by Django 4.2.5 on 2024-02-15 17:41

from django.db import migrations, models
import django.db.models.deletion
import services.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='adi')),
            ],
            options={
                'verbose_name': 'blog category',
                'verbose_name_plural': 'blog categories',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='about',
            name='slogan',
            field=models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_photo_about),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='blog')),
                ('image', models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.upload_photo_blog)),
                ('information', models.TextField(verbose_name='melumat')),
                ('user', models.CharField(max_length=255, verbose_name='istifadeci')),
                ('blog_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.blogcategory')),
            ],
            options={
                'verbose_name': 'elaqe melumati',
                'verbose_name_plural': 'elaqe melumatlari',
                'ordering': ('-created_at',),
            },
        ),
    ]
