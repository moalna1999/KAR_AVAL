from django.db import models
from datetime import datetime 

######################### My models  #########################
#######accesslevel#######
EMPLOYEE      = 'EMPLOYEE'
ADMINISTRATOR = 'ADMINISTRATOR'
accesslevel = [
    (EMPLOYEE, 'Employee'),
    (ADMINISTRATOR, 'Administrator'),]
######department########
CENTRAL = 'CENTRAL'
SOUTH   = 'SOUTH'
department = [
    (CENTRAL, 'Central'),
    (SOUTH, 'South'),]
#######unit########
MANAGEMENT = 'Management'
SERVICES   = 'Services'
unit = [
    (MANAGEMENT, 'Management'),
    (SERVICES, 'Services'),]
#######position########
EMPLOYEE = 'Employee'
BOSS   = 'Boss'
position = [
    (EMPLOYEE, 'Employee'),
    (BOSS, 'Boss'),]
#######activity########
Disabled = False
Active = True
activity = [
    (Disabled,'Disabled' ),
    (Active , 'Active'  ),]
#######point########
P0='0'
P1='1'
P2=''
P3='3'
P4='4'
P5='5'
P6='6'
P7='7'
P8='8'
P9='9'
P10='10'
pointe = [
    (P0,'0'),
    (P1,'1'),
    (P2,'2'),
    (P3,'3'),
    (P4,'4'),
    (P5,'5'),
    (P6,'6'),
    (P7,'7'),
    (P8,'8'),
    (P9,'9'),
    (P10,'10'),]
######################### Member #########################

class Members(models.Model):
    first_name  = models.CharField(max_length=6000,blank=True)
    last_name   = models.CharField(max_length=600,blank=True)
    user_name   = models.CharField(max_length=600,blank=True)
    password    = models.CharField(max_length=600,blank=False)
    accesslevel = models.CharField(max_length=600,choices=accesslevel,blank=True)
    department  = models.CharField(max_length=600,choices=department,blank=True)
    unit        = models.CharField(max_length=600,choices=unit,blank=True)
    position    = models.CharField(max_length=600,choices=position,blank=True)
    activity    = models.BooleanField(max_length=600,choices=activity)
    pointe      = models.IntegerField(choices=pointe)
    creator     = models.CharField(max_length=1200,blank=False)
    Updating    = models.CharField(max_length=1200,blank=False)
    email       = models.EmailField(max_length=2540,blank=True)
    phone       = models.CharField(max_length=150,blank=True )
    profile     = models.FileField(blank=True)
    date        = models.DateTimeField(auto_now_add=True)
    #file        = models.FileField(max_length=250, allow_empty_file=True, use_url=UPLOADED_FILES_USE_URL)
    def __str__(self):
        return self.first_name

class Adminstors(models.Model):
    name  = models.CharField(max_length=6000)
    ADM_ID = models.ManyToManyField(Members)
    def __str__(self):
        return self.name

class ForeignKey(models.Model):
    name  = models.CharField(max_length=6000)
    ADM_ID_ForeignKey = models.ForeignKey(Members,on_delete=models.CASCADE)
    def __str__(self):
        return self.ADM_ID_ForeignKey