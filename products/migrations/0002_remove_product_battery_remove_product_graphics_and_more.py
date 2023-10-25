# Generated by Django 4.0.6 on 2023-10-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='battery',
        ),
        migrations.RemoveField(
            model_name='product',
            name='graphics',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hard_drive',
        ),
        migrations.RemoveField(
            model_name='product',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='operating_system',
        ),
        migrations.RemoveField(
            model_name='product',
            name='power_supply',
        ),
        migrations.RemoveField(
            model_name='product',
            name='processor',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], default='Men', max_length=150),
        ),
    ]
