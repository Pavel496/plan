# Generated by Django 4.1.4 on 2022-12-19 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0004_alter_student_options_alter_student_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unirecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_name', models.CharField(max_length=50)),
                ('record_date', models.DateField(blank=True, null=True)),
                ('record_time', models.TimeField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
            options={
                'ordering': ['record_date', 'record_time'],
            },
        ),
    ]
