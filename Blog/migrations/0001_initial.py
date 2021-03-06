# Generated by Django 4.0.2 on 2022-02-20 14:24

import Blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0002_user_createdat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.TimeField(auto_now_add=True)),
                ('blogTittle', models.CharField(max_length=50)),
                ('postImage', models.ImageField(null=True, upload_to=Blog.models.get_file_path)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likedAt', models.DateField(auto_now_add=True)),
                ('Blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('Blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
    ]
