# Generated by Django 2.2.4 on 2019-08-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('username', models.CharField(default='abc', max_length=255, primary_key=True, serialize=False)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
