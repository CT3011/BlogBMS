# Generated by Django 4.0.2 on 2022-02-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createdAt',
            field=models.DateField(auto_now_add=True,),
        ),
    ]