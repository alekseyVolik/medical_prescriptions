# Generated by Django 2.2.4 on 2021-02-04 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('father_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('specialization', models.CharField(max_length=75, verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Доктора',
                'ordering': ['specialization', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('father_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Создан')),
                ('validity', models.DurationField(verbose_name='Срок действия')),
                ('priority', models.CharField(choices=[('Нормальный', 'Нормальный'), ('Срочный', 'Срочный'), ('Незамедлительный', 'Незамедлительный')], max_length=20, verbose_name='Приоритет')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='prescriptions.Doctor', verbose_name='Доктор')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='prescriptions.Patient', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ['create_date'],
            },
        ),
    ]
