from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class newReg(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = "newReg"

class addEmp(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(('password'), max_length=50)
    joining_date = models.DateField(editable=False, auto_now=True)
    rem_leaves = models.IntegerField()
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    current_project = models.CharField(max_length=100)

    class Meta:
        db_table = "addEmp"

class leaveRequest(models.Model):
    empId=models.ForeignKey(addEmp,on_delete=CASCADE)
    leaveType=models.CharField(max_length=50)
    startDate=models.DateField()
    endDate=models.DateField()
    leaveDesc=models.TextField(max_length=300)
    decision=models.CharField(max_length=20,default="Pending")

    class Meta:
        db_table = "leaveRequest"

class notice(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    issue_date = models.DateField(editable=False, auto_now=True)

