# Generated by Django 4.2.16 on 2024-10-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_models', '0003_rename_c_introduction_course_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Syllabus',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='course',
            name='calendar',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='information',
            name='I_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
