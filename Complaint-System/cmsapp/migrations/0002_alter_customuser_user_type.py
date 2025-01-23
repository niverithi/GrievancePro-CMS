# Generated by Django 5.0.4 on 2024-04-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'compuser')], default=1, max_length=50),
        ),
    ]
