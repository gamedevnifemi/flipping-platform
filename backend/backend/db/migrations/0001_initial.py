# Generated by Django 5.1.6 on 2025-02-24 22:46

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('seller', models.CharField(blank=True, max_length=255, null=True)),
                ('marketplace', models.CharField(choices=[('ebay', 'eBay'), ('stockx', 'StockX'), ('goat', 'GOAT'), ('amazon', 'Amazon'), ('other', 'Other')], max_length=50)),
                ('date_fetched', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.URLField()),
                ('product_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_id', models.CharField(max_length=50, unique=True)),
                ('shoe_name', models.CharField(max_length=255)),
                ('retail_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('thumbnail', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('colorway', models.CharField(blank=True, max_length=100, null=True)),
                ('stockx_url', models.URLField()),
                ('goat_url', models.URLField()),
                ('date_released', models.DateField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('github_id', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('is_active_user', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'db_customuser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
