# Generated by Django 3.2 on 2022-09-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email address')),
                ('phone_number', models.CharField(max_length=12, unique=True, verbose_name='Phone Number')),
                ('country_code', models.CharField(max_length=5, verbose_name='Country Code')),
                ('name', models.CharField(max_length=100, verbose_name='user name')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='user name')),
                ('invite_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='invite code')),
                ('refer_count', models.IntegerField(blank=True, default=0, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
