from django.db import models

# Create your models here.


class studentregister_model(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    department=models.CharField(max_length=20)
    register_num=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    # def __str__(self):
    #     return self.firstname


class regmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()


# class first_sem_model(models.Model):
#     id2 = models.IntegerField()
#     arabic=models.IntegerField()
#     english=models.IntegerField()
#     C=models.IntegerField()
#     DE=models.IntegerField()
#     DM=models.IntegerField()
#     c_programming_Lab=models.IntegerField()
#     DE_Lab=models.IntegerField()
#     environment=models.IntegerField()


class first_sem_model1(models.Model):
    id2 = models.IntegerField()
    arabic = models.IntegerField()
    english = models.IntegerField()
    C = models.IntegerField()
    DE = models.IntegerField()
    DM = models.IntegerField()
    c_programming_Lab = models.IntegerField()
    DE_Lab = models.IntegerField()
    environment = models.IntegerField()

class second_sem_model(models.Model):
    id2 = models.IntegerField()
    arabic=models.IntegerField()
    english=models.IntegerField()
    DS=models.IntegerField()
    DBMS=models.IntegerField()
    NSM=models.IntegerField()
    DS_Lab=models.IntegerField()
    DBMS_Lab=models.IntegerField()
    ICHR=models.IntegerField()


class third_sem_model(models.Model):
    id2 = models.IntegerField()
    arabic=models.IntegerField()
    english=models.IntegerField()
    Cpp=models.IntegerField()
    Accounting=models.IntegerField()
    OperatingSystem=models.IntegerField()
    Cpp_Lab=models.IntegerField()
    Accounting_Lab=models.IntegerField()
    CDS=models.IntegerField()


class fourth_sem_model(models.Model):
    id2 = models.IntegerField()
    arabic=models.IntegerField()
    english=models.IntegerField()
    Vprogramming=models.IntegerField()
    USprogramming=models.IntegerField()
    oR=models.IntegerField()
    Vp_Lab=models.IntegerField()
    UNIX_Lab=models.IntegerField()
    PD=models.IntegerField()


class fifth_sem_model(models.Model):
    id2 = models.IntegerField()
    DCN=models.IntegerField()
    SE=models.IntegerField()
    CA=models.IntegerField()
    JP=models.IntegerField()
    MP=models.IntegerField()
    Project=models.IntegerField()
    BF=models.IntegerField()

class sixth_sem_model(models.Model):
    id2 = models.IntegerField()
    TOC=models.IntegerField()
    SP=models.IntegerField()
    CNS=models.IntegerField()
    WP=models.IntegerField()
    WPL=models.IntegerField()
    Project=models.IntegerField()
    CAIT=models.IntegerField()
