# Generated by Django 4.0.2 on 2022-02-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=200)),
                ('issu', models.TextField()),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
