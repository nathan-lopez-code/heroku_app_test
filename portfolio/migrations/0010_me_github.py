# Generated by Django 4.0.2 on 2022-03-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_me_js'),
    ]

    operations = [
        migrations.AddField(
            model_name='me',
            name='github',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
