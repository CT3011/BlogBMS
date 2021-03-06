# Generated by Django 4.0.2 on 2022-02-20 12:33

import User.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('mNo', models.IntegerField(null=True)),
                ('image', models.ImageField(null=True, upload_to=User.models.get_file_path)),
                ('address', models.CharField(max_length=250, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('empNo', models.IntegerField()),
                ('about', models.CharField(max_length=255, null=True)),
                ('birthDate', models.DateField()),
                ('dateOfJoining', models.DateField()),
                ('jonTittle', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.department')),
                ('jobType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.jobtype')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.position')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.role')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.shift')),
                ('workTye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.worktype')),
            ],
        ),
    ]
