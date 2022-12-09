# Generated by Django 3.2.16 on 2022-11-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0006_alter_cart_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.AddField(
            model_name='bike',
            name='image',
            field=models.ImageField(null=True, upload_to='media/photos'),
        ),
        migrations.AddField(
            model_name='component',
            name='image',
            field=models.ImageField(null=True, upload_to='media/photos'),
        ),
    ]
