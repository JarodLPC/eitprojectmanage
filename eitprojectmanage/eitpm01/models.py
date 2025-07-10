from django.utils import timezone
from django.db import models
from datetime import datetime
# Create your models here.


class AdminInfo(models.Model):
    adminId = models.AutoField(primary_key=True)
    adminName = models.CharField(max_length=20)
    adminPwd = models.CharField(max_length=20)

    class Meta:
        db_table = 'admininfo'


class BusInfo(models.Model):
    busId = models.AutoField(primary_key=True)
    busType = models.CharField(max_length=20)

    class Meta:
        db_table = 'businfo'
    def __str__(self):
        return self.busType

class CustomerInfo(models.Model):
    customerId = models.AutoField(primary_key=True)
    customername = models.CharField(max_length=20)

    class Meta:
        db_table = 'customerinfo'
    def __str__(self):
        return self.customername

class DatabaseInfo(models.Model):
    databaseId = models.AutoField(primary_key=True)
    databasetype = models.CharField(max_length=20)

    class Meta:
        db_table = 'databaseinfo'
    def __str__(self):
        return self.databasetype


class EngineerInfo(models.Model):
    engineerId = models.AutoField(primary_key=True,verbose_name='工程师编号')
    engineerName = models.CharField(max_length=20,verbose_name='工程师名称')
    telephoneno = models.CharField(max_length=30,verbose_name='电话号码')
    engineerpwd = models.CharField(max_length=30,verbose_name='密码')

    class Meta:
        db_table = 'engineerinfo'


class MachineInfo(models.Model):
    machineid = models.AutoField(primary_key=True)
    machinetype = models.CharField(max_length=20)

    class Meta:
        db_table = 'machineinfo'


class OpcInfo(models.Model):
    opcid = models.AutoField(primary_key=True)
    opctype = models.CharField(max_length=20)

    class Meta:
        db_table = 'opcinfo'


class EitInfo(models.Model):
    eitid = models.AutoField(primary_key=True)
    eittype = models.CharField(max_length=20)

    class Meta:
        db_table = 'eitinfo'


class OsInfo(models.Model):
    osid = models.AutoField(primary_key=True)
    ostype = models.CharField(max_length=20)

    class Meta:
        db_table = 'osinfo'


class PlcInfo(models.Model):
    plcid = models.AutoField(primary_key=True)
    plctype = models.CharField(max_length=20)

    class Meta:
        db_table = 'plcinfo'
    def __str__(self):
        return self.plctype


class ProjStatus(models.Model):
    projStatusId = models.AutoField(primary_key=True)
    projstatustype = models.CharField(max_length=20)

    class Meta:
        db_table = 'projstatus'
    def __str__(self):
        return self.projstatustype

class ServerInfo(models.Model):
    serverid = models.AutoField(primary_key=True)
    servertype = models.CharField(max_length=20)

    class Meta:
        db_table = 'serverinfo'
    def __str__(self):
        return self.servertype

class WbsInfo(models.Model):
    wbsid = models.AutoField(primary_key=True)
    wbsno = models.CharField(max_length=20)

    class Meta:
        db_table = 'wbsinfo'

class ProjInfo(models.Model):
    projid = models.AutoField(primary_key=True,verbose_name='ID')
    projno = models.CharField(max_length=10,verbose_name='项目编号')
    plannedwh = models.IntegerField(default=0,verbose_name='计划工时')
    location = models.CharField(max_length=30,verbose_name='项目地点')
    projstatusid = models.ForeignKey(ProjStatus,on_delete=models.CASCADE,verbose_name='项目状态',db_column='projstatusid')
    projdescription = models.CharField(max_length=300,verbose_name='项目描述')
    # customerid = models.IntegerField(default=0)
    customerid = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE,db_column='customerid',verbose_name='客户ID')
    startingtime = models.DateTimeField(default=datetime.now,verbose_name='项目开始时间')
    opcstatus = models.CharField(max_length=10,verbose_name='OPC状态')
    serverstatus = models.CharField(max_length=10,verbose_name='服务器状态')
    osstatus = models.CharField(max_length=10,verbose_name='操作系统状态')
    databasestatus = models.CharField(max_length=10,verbose_name='数据库状态')
    opcidgroup = models.CharField(max_length=20,verbose_name='OPC组ID')
    serverid = models.ForeignKey(ServerInfo,on_delete=models.CASCADE,verbose_name='服务器ID',db_column='serverid')
    databaseid = models.ForeignKey(DatabaseInfo,on_delete=models.CASCADE,verbose_name='数据库ID',db_column='databaseid')
    kodate = models.DateField(default=timezone.now,verbose_name='KO日期')

    class Meta:
        db_table = 'projinfo'








class WorkHourInfo(models.Model):
    id = models.AutoField(primary_key=True)
    projid = models.IntegerField(default=0)
    workdate = models.DateField()
    onsite = models.CharField(max_length=10)
    engineerid = models.IntegerField(default=0)
    wbsid = models.IntegerField(default=0)
    wh = models.IntegerField(default=0)
    comment = models.CharField(max_length=50)
    weekno = models.IntegerField(default=0)

    class Meta:
        db_table = 'workhourinfo'
