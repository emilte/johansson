# Generated by Django 3.2.5 on 2021-08-01 13:20

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
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edited', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Sist redigert')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('name', models.CharField(max_length=200, verbose_name='navn')),
                ('hex', models.CharField(blank=True, help_text='Fargekode i hex (6 symboler)', max_length=6, null=True, verbose_name='hex')),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_color_set', to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
                ('last_editor', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editor_color_set', to=settings.AUTH_USER_MODEL, verbose_name='Sist redigert av')),
            ],
            options={
                'verbose_name': 'farge',
                'verbose_name_plural': 'farger',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edited', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Sist redigert')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('name', models.CharField(max_length=200, verbose_name='navn')),
                ('bg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='domain_bg', to='root.color', verbose_name='bakgrunnsfarge')),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_domain_set', to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
                ('font', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='domain_font', to='root.color', verbose_name='skriftfarge')),
                ('last_editor', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editor_domain_set', to=settings.AUTH_USER_MODEL, verbose_name='Sist redigert av')),
            ],
            options={
                'verbose_name': 'domene',
                'verbose_name_plural': 'domener',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='TagGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edited', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Sist redigert')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('name', models.CharField(max_length=200, verbose_name='navn')),
                ('bg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag_group_bg', to='root.color', verbose_name='bakgrunnsfarge')),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_taggroup_set', to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.domain', verbose_name='tag-domene')),
                ('font', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag_group_font', to='root.color', verbose_name='skriftfarge')),
                ('last_editor', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editor_taggroup_set', to=settings.AUTH_USER_MODEL, verbose_name='Sist redigert av')),
            ],
            options={
                'verbose_name': 'tag-gruppe',
                'verbose_name_plural': 'tag-grupper',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_edited', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Sist redigert')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Opprettet')),
                ('name', models.CharField(help_text="En vilkårlig egenskap til en plante. (Tips: Du kan prefikse tags med kolon ':', f.eks. 'familie:fiola' )", max_length=200, verbose_name='navn')),
                ('bg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag_bg', to='root.color', verbose_name='bakgrunnsfarge')),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_tag_set', to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av')),
                ('font', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag_font', to='root.color', verbose_name='skriftfarge')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.taggroup', verbose_name='tag-gruppe')),
                ('last_editor', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='editor_tag_set', to=settings.AUTH_USER_MODEL, verbose_name='Sist redigert av')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': [],
            },
        ),
    ]