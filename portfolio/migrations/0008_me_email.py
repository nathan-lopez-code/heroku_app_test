# Generated by Django 4.0.2 on 2022-02-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_me_city_me_number1_me_number2'),
    ]

    operations = [
        migrations.AddField(
            model_name='me',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
    ]