# Generated by Django 3.2.5 on 2021-08-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='författare'),
        ),
        migrations.AlterField(
            model_name='book',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='kommentar'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='isbn'),
        ),
        migrations.AlterField(
            model_name='book',
            name='nationality',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='nationalitet'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='antal sidor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='forlag'),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='utgivningsår'),
        ),
    ]
