# Generated by Django 3.1.7 on 2021-09-23 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackapp', '0005_auto_20210922_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_photo',
            field=models.ImageField(default='media/default.jpg', upload_to='media/courses/'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='lecturer_profile',
            field=models.ImageField(default='media/default.jpg', upload_to='media/lecturers/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.ImageField(default='media/default.jpg', upload_to='media/images/'),
        ),
    ]