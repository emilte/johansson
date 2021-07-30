# Generated by Django 3.2.5 on 2021-07-30 18:22

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=60, unique=True, verbose_name='brukernavn')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Fornavn')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Etternavn')),
                ('gender', models.CharField(blank=True, choices=[(None, None), ('M', 'Mann'), ('F', 'Kvinne'), ('O', 'Annet')], default=None, max_length=1, null=True, verbose_name='Kjønn')),
                ('is_active', models.BooleanField(default=True)),
                ('phone_number', models.CharField(blank=True, default=None, max_length=13, null=True, verbose_name='Mobilnummer')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, verbose_name='Opprettet')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tittel')),
            ],
            options={
                'verbose_name': 'Seksjon',
                'verbose_name_plural': 'Seksjoner',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='PermissionCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Dato påmeldt')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.department', verbose_name='Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Bruker')),
            ],
            options={
                'verbose_name': 'Medlem',
                'verbose_name_plural': 'Medlemmer',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='departments', through='accounts.Member', to=settings.AUTH_USER_MODEL, verbose_name='Medlemmer'),
        ),
        migrations.AddField(
            model_name='department',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='accounts.department', verbose_name='Over-seksjon'),
        ),
    ]
