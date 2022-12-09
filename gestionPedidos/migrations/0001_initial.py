# Generated by Django 3.2.16 on 2022-12-09 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.CharField(max_length=200, null=True)),
                ('type_component', models.CharField(choices=[('No definido', 'No definido'), ('Sillin', 'Sillin'), ('Ruedas', 'Ruedas'), ('Manillar', 'Manillar'), ('Cámara rueda', 'Cámara rueda'), ('Cuadro de la bici', 'Cuadro de la bici')], default='No definido', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentsInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPedidos.cart')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPedidos.component')),
            ],
        ),
        migrations.CreateModel(
            name='ComponentBike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionPedidos.bike')),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionPedidos.component')),
            ],
        ),
        migrations.CreateModel(
            name='BikesInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPedidos.bike')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPedidos.cart')),
            ],
        ),
    ]
