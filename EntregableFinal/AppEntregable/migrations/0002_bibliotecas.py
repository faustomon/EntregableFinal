# Generated by Django 4.0.4 on 2022-06-07 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntregable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliotecas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('localidad', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=60)),
                ('apertura', models.CharField(max_length=100)),
                ('link', models.URLField(blank=True, max_length=100, null=True)),
                ('imagen', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
