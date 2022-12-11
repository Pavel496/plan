# Generated by Django 4.1.4 on 2022-12-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_options_student_surname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Фамилия'),
        ),
    ]