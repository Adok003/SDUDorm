from django.db import models
import datetime


GENDER = [
    ('m', 'Male'),
    ('f', 'Female')
]

TYPE = [
    ('Log In', 'Log In'),
    ('Log Out', 'Log Out')
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


class User(models.Model):
    student_id = models.IntegerField('Student ID', default = 0,null = False)
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    email = models.EmailField('E-mail', max_length=50)
    gender = models.CharField('Gender', max_length=2, choices=GENDER)
    course = models.IntegerField('Course', choices=COURSE)
    faculty = models.CharField('Faculty', max_length=60, choices=FACULTY)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + str(self.course) + ' course'

class Block(models.Model):
    block_name = models.CharField('Block name', max_length=50)
    block_type = models.CharField('Block type', max_length=50)

    def __str__(self):
        return self.block_name + ' block for ' + self.block_type


class Floor(models.Model):
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE)
    floor_number = models.IntegerField('Floor number')

    def __str__(self):
        return str(self.block_id) + ' ' + str(self.floor_number) + ' floor'

    class Meta:
        ordering = ('floor_number', )


class Room(models.Model):
    floor_number = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_number = models.IntegerField('Room number')
    faculty = models.CharField('Faculty', default='None', max_length=50, choices=FACULTY)
    course = models.IntegerField('Course', choices=COURSE)
    room_info = models.CharField('Room info', max_length=100)

    def __str__(self):
        return str(self.floor_number) + ' ' + str(self.room_number) + ' room'

    class Meta:
        ordering = ('room_number', )

class Entry(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField('Type Of Entry', default='None', max_length=60, choices=TYPE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.last_name + ' ' + self.student_id.first_name + ' ' + self.type + ' ' + str(self.date)
