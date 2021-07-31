# Generated by Django 3.2.5 on 2021-07-31 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edited', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Sist redigert')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('name', models.CharField(max_length=200, verbose_name='navn')),
                ('name_latin', models.CharField(blank=True, max_length=200, null=True, verbose_name='latinsk navn')),
                ('longevity', models.DecimalField(decimal_places=1, default=1, max_digits=100, verbose_name='levetid')),
                ('longevity_unit', models.CharField(blank=True, choices=[(None, ''), ('seconds', 'sekunder'), ('minutes', 'minutter'), ('hours', 'timer'), ('days', 'dager'), ('weeks', 'uker'), ('months', 'måneder'), ('years', 'år')], default='years', max_length=20, null=True, verbose_name='enhet')),
                ('water_freq', models.DecimalField(decimal_places=1, default=7, max_digits=100, verbose_name='vannefrekvens')),
                ('water_freq_unit', models.CharField(blank=True, choices=[(None, ''), ('seconds', 'sekunder'), ('minutes', 'minutter'), ('hours', 'timer'), ('days', 'dager'), ('weeks', 'uker'), ('months', 'måneder'), ('years', 'år')], default='days', max_length=20, null=True, verbose_name='enhet')),
                ('water_amount', models.DecimalField(decimal_places=1, default=2, max_digits=100, verbose_name='vannmengde')),
                ('water_amount_unit', models.CharField(blank=True, choices=[(None, ''), ('ml', 'ml'), ('cl', 'cl'), ('dl', 'dl'), ('l', 'l')], default='dl', max_length=20, null=True, verbose_name='enhet')),
                ('image_url', models.URLField(blank=True, help_text='høyre klikk, kopier bildeaddresse, lim inn her', null=True, verbose_name='bilde')),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_flower_set', to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
                ('last_editor', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editor_flower_set', to=settings.AUTH_USER_MODEL, verbose_name='Sist redigert av')),
                ('tags', models.ManyToManyField(blank=True, to='root.Tag')),
            ],
            options={
                'verbose_name': 'blomst',
                'verbose_name_plural': 'blomster',
                'ordering': [],
            },
        ),
    ]
