# Generated by Django 3.2.5 on 2021-08-01 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.domain', verbose_name='tag-domene'),
        ),
    ]