from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Card(models.Model):
    card_number = models.IntegerField()

    def __str__(self):
        return str(self.card_number)


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.title}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    # ✅ إضافة العلاقة مع Card
    card = models.OneToOneField(
        Card,
        on_delete=models.PROTECT,  # يمنع حذف البطاقة المرتبطة بطالب
        null=True,  # نسمح بأن الطالب ما يكون له بطاقة مبدئياً
        blank=True
    )

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name='students')



    def __str__(self):
        return self.name


