# Generated by Django 4.2.16 on 2024-09-30 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('C_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('C_introduction', models.CharField(blank=True, max_length=1000, null=True)),
                ('Syllabus', models.CharField(blank=True, max_length=1000, null=True)),
                ('calendar', models.CharField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('period', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('D_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('F_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('follow_num', models.IntegerField(blank=True, default=0, null=True)),
                ('like_num', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('I_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('R_id', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('R_id', models.IntegerField(primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='resource/')),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('S_id', models.IntegerField(primary_key=True, serialize=False)),
                ('account', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('attention_num', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('T_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('account', models.CharField(blank=True, max_length=20, null=True)),
                ('passward', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('W_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='global_models.student')),
                ('follow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='global_models.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.course')),
                ('S_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.student')),
            ],
        ),
        migrations.CreateModel(
            name='Releasement',
            fields=[
                ('R_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('C_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.course')),
                ('I_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.information')),
                ('S_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.student')),
                ('T_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('N_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('F_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.favorite')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.favorite')),
                ('S_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.student')),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='S_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.student'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.favorite'),
        ),
        migrations.CreateModel(
            name='DoWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_push', models.BooleanField(blank=True, default=False, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='work/')),
                ('C_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.course')),
                ('S_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.student')),
                ('T_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.teacher')),
                ('W_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.work')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.discuss')),
                ('R_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.reply')),
            ],
        ),
        migrations.AddField(
            model_name='discuss',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.student'),
        ),
        migrations.CreateModel(
            name='DisCou',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.course')),
                ('D_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.discuss')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.course')),
                ('T_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.course')),
                ('R_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='global_models.resource')),
            ],
        ),
    ]
