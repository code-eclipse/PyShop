# Generated by Django 5.1.2 on 2024-10-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('descreption', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
    ]