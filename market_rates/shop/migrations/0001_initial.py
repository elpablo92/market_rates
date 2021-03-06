# Generated by Django 3.1.2 on 2020-10-15 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Nombre del producto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Precio')),
                ('image', models.ImageField(upload_to=None, verbose_name='Imagen')),
                ('description', models.TextField(verbose_name='Descripcion del producto')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanti', models.IntegerField(verbose_name='Cantidad')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='cliente')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Producto')),
            ],
        ),
    ]
