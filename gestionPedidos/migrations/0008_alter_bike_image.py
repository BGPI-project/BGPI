# Generated by Django 3.2.16 on 2022-11-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0007_alter_bike_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(null=True, upload_to='media/photos'),
        ),
    ]
