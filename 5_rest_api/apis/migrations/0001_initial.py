# Generated by Django 5.0.4 on 2024-06-21 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id_school', models.AutoField(primary_key=True, serialize=False)),
                ('name_school', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id_class', models.AutoField(primary_key=True, serialize=False)),
                ('grade_class', models.IntegerField()),
                ('room_class', models.IntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='apis.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id_student', models.AutoField(primary_key=True, serialize=False)),
                ('name_student', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender_id', models.CharField(max_length=20)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='apis.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id_teacher', models.AutoField(primary_key=True, serialize=False)),
                ('name_teacher', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=20)),
                ('classroom', models.ManyToManyField(related_name='teachers', to='apis.classroom')),
            ],
        ),
    ]