# Generated by Django 4.2.16 on 2024-12-09 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('global_models', '0010_alter_admin_user_alter_student_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='passward',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='passward',
        ),
        migrations.AlterField(
            model_name='admin',
            name='A_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='admin',
            name='account',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='account',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='T_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='account',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
