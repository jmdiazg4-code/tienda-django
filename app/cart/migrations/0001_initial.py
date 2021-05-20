# Generated by Django 3.2 on 2021-04-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=80, verbose_name='Nombre Completo')),
                ('customer_email', models.EmailField(max_length=120, verbose_name='E-mail')),
                ('customer_mobile', models.CharField(max_length=40, verbose_name='Celular')),
                ('status', models.CharField(max_length=20, verbose_name='Estado del Pedido')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')),
                ('url_payment', models.URLField(max_length=500)),
                ('product', models.CharField(max_length=100, verbose_name='Producto de la compra')),
                ('imagen', models.ImageField(default=False, upload_to='')),
                ('total', models.FloatField(default=True)),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
                'db_table': 'orders',
                'ordering': ['id'],
            },
        ),
    ]