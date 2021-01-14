# Generated by Django 3.1.4 on 2021-01-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210108_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='mainapp.CartProduct'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='amount',
            field=models.PositiveIntegerField(default=1, verbose_name='Amount'),
        ),
    ]
