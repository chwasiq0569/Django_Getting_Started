# Generated by Django 3.2 on 2021-05-08 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not avaiable', max_length=70),
        ),
    ]