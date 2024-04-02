# Generated by Django 5.0.3 on 2024-04-01 11:31

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='major_outreach')),
                ('paragraph', tinymce.models.HTMLField()),
                ('writers_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainHeroSectionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='main_hero_image')),
            ],
        ),
        migrations.CreateModel(
            name='NewMajorOutreach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('top_image', models.ImageField(upload_to='major_outreach')),
                ('right_image', models.ImageField(upload_to='major_outreach')),
                ('left_image', models.ImageField(upload_to='major_outreach')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='NewsAndUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='homepage_what_we_have_done')),
                ('Headline', models.CharField(max_length=30)),
                ('paragraph', tinymce.models.HTMLField()),
            ],
        ),
    ]
