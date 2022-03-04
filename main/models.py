from django.db import models

GENDER = [
    ('m', 'Male'),
    ('f', 'Female')
]
COURSE = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
]
FACULTY = [
    ('Faculty of Law and Social Sciences', 'Faculty of Law and Social Sciences'),
    ('Faculty of Education and Humanities Sciences', 'Faculty of Education and Humanities Sciences'),
    ('Faculty of Engineering and Natural Sciences', 'Faculty of Engineering and Natural Sciences'),
    ('Business school', 'Business school')
]


class Req(models.Model):
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    email = models.CharField('E-mail', max_length=50)
    gender = models.CharField('Gender', max_length=2, choices=GENDER)
    course = models.IntegerField('Course', choices=COURSE)
    faculty = models.CharField('Faculty', max_length=60, choices=FACULTY)

    def __str__(self):
        return self.first_name
