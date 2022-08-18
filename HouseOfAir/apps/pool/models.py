from django.db import models

class plain (models.Model):
    name = models.CharField ('Самолет', max_length=  25)

class company(models.Model):
    name = models.CharField ('Название компании', max_length=  25)

class pilot(models.Model):
    id_plain = models.ForeignKey(plain, null=True, on_delete= models.SET_NULL)
    id_company = models.ForeignKey(company, on_delete= models.CASCADE)
    name = models.CharField ('ФИО Пилота', max_length=  255)
    passport = models.BigIntegerField('Номер и Серия', default = 0)
    hours = models.BigIntegerField('Количество летных часов', default = 0) 

class dispatcher(models.Model):
    name = models.CharField ('ФИО Диспетчера', max_length=  255)
    passport = models.BigIntegerField('Номер и Серия')
    phone = models.BigIntegerField('Номер телефона')

class terminal(models.Model):
    name = models.CharField ('Номер терминала', max_length=  5)


class arrival_schedule(models.Model):
    arrivalF_time = models.DateTimeField('Время вылета', null=True)
    arrivalT_time = models.DateTimeField('Время прибытия', null=True)
    from_where = models.CharField('Город вылета', max_length = 25)
    id_company = models.ForeignKey(company, on_delete= models.CASCADE)
    id_plain = models.ForeignKey(plain, on_delete= models.CASCADE)
    id_pilotONE = models.ForeignKey(pilot, null=True, on_delete= models.SET_NULL, related_name='aONE')
    id_pilotTWO = models.ForeignKey(pilot, null=True, on_delete= models.SET_NULL, related_name='aTWO')
    id_terminal = models.ForeignKey(terminal, null=True, on_delete = models.SET_NULL)
    id_dispatcher = models.ForeignKey(dispatcher, null=True, on_delete= models.SET_NULL)

class depart_schedule(models.Model):
    departF_time = models.DateTimeField('Время вылета', null=True)
    departT_time = models.DateTimeField('Время прибытия', null=True)
    where = models.CharField('Город прилета', max_length = 25)
    id_company = models.ForeignKey(company, on_delete= models.CASCADE)
    id_plain = models.ForeignKey(plain, on_delete= models.CASCADE)
    id_pilotONE = models.ForeignKey(pilot, null=True, on_delete= models.SET_NULL, related_name='dONE')
    id_pilotTWO = models.ForeignKey(pilot, null=True, on_delete= models.SET_NULL, related_name='dTWO')
    id_terminal = models.ForeignKey(terminal, null=True, on_delete= models.SET_NULL)
    id_dispatcher = models.ForeignKey(dispatcher, null=True, on_delete= models.SET_NULL)

class passanger(models.Model):
    flight_depart = models.ForeignKey(depart_schedule, null=True, blank=True, on_delete=  models.SET_NULL)
    flight_arrival = models.ForeignKey(arrival_schedule, null=True, blank=True, on_delete=  models.SET_NULL)
    name = models.CharField ('ФИО', max_length=  255)
    passport = models.BigIntegerField('Номер и Серия')



#============================================================

class parking(models.Model):
    id_terminal = models.ForeignKey(terminal, null=True, on_delete= models.SET_NULL)
    tipe = models.CharField('Тип парковки', max_length=15)
    cost_h = models.PositiveIntegerField('Почасовая стоимость', null=True)
    cost_d = models.PositiveIntegerField('Суточная стоимость', null=True)

class service(models.Model):
    id_terminal = models.ForeignKey(terminal, null=True, on_delete= models.SET_NULL)
    tipe = models.CharField("Тип услуги", max_length=30)
    floor = models.PositiveSmallIntegerField('Этаж')
    cost = models.PositiveIntegerField('Стоимость')

class store(models.Model):
    id_terminal = models.ForeignKey(terminal, null=True, on_delete= models.SET_NULL)
    tipe = models.CharField("Тип магазина", null=True, max_length=10)
    name = models.CharField ('Название', null=True, max_length=  255)
    sq_m = models.PositiveIntegerField ('Квадратных метров', null= True)
    month_cost = models.PositiveBigIntegerField('Стоимость аренды', null=True)
    rent_to = models.DateField('Арендовано до', null= True)