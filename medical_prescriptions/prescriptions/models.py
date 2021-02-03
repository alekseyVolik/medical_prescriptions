from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    father_name = models.CharField(max_length=50, verbose_name='Отчество')
    phone_number = models.CharField(max_length=50, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['first_name']


class Doctor(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    father_name = models.CharField(max_length=50, verbose_name='Отчество')
    specialization = models.CharField(max_length=75, verbose_name='Специализация')

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ['specialization', 'first_name']


class Prescription(models.Model):

    PRIORITY_TYPES = (('Нормальный', 'Нормальный'),
                      ('Срочный', 'Срочный'),
                      ('Незамедлительный', 'Незамедлительный'))

    description = models.TextField()
    patient = models.ForeignKey('Patient', null=True, on_delete=models.PROTECT, verbose_name='Пациент')
    doctor = models.ForeignKey('Doctor', null=True, on_delete=models.PROTECT, verbose_name='Доктор')
    create_date = models.DateField(auto_now_add=True, verbose_name='Создан')
    validity = models.DurationField(verbose_name='Срок действия')
    priority = models.CharField(max_length=20, verbose_name='Приоритет', choices=PRIORITY_TYPES)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['create_date']
