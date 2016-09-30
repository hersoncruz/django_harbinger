from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.db import models

@python_2_unicode_compatible
class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    hire_date = models.DateField('hire date')
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

@python_2_unicode_compatible
class Skills(models.Model):
    skills_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description


class Employee_Skills(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skills_id = models.ForeignKey(Skills, on_delete=models.CASCADE)

@python_2_unicode_compatible
class Unit(models.Model):
    unit_number_id = models.IntegerField(primary_key=True)
    unit_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    install_date = models.DateField('installation date')
    pid_number = models.CharField(max_length=100)
    def __str__(self):
        return '%s %s' % (self.unit_number, self.name)

@python_2_unicode_compatible
class Parts(models.Model):
    parts_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=200)
    quantity_on_hand = models.IntegerField(default=0)
    def __str__(self):
        return '%s %s %s' % (self.name, self.description, self.location)


class Parts_Units(models.Model):
    unit_number_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    parts_id = models.ForeignKey(Parts, on_delete=models.CASCADE)

@python_2_unicode_compatible
class Lockout(models.Model):
    lock_out_id = models.IntegerField(primary_key=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='employee_id')
    def __str__(self):
        return '%s %s' % (self.lock_out_id, self.created_by)

@python_2_unicode_compatible
class Work_Order(models.Model):
    work_order_id = models.IntegerField(primary_key=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='employee_id')
    priority_level = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    status = models.IntegerField(default=0)
    start_date = models.DateTimeField('start date')
    close_date = models.DateTimeField('close date')
    lock_out_id = models.ForeignKey(Lockout, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s' % (self.start_date, self.description, self.created_by)

class Work_Order_Unit(models.Model):
    work_order_id = models.ForeignKey(Work_Order, on_delete=models.CASCADE)
    unit_number_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
