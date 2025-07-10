from django.contrib import admin

# Register your models here.
from .models import *

# 方法一
@admin.register(EngineerInfo)
class EngineerInfoAdmin(admin.ModelAdmin):
    list_display = ['engineerId', 'engineerName']
    actions_on_top = False
    actions_on_bottom = True
    admin.site.site_title="项目信息管理1"
    admin.site.site_header="项目信息管理2"
    admin.site.index_title="项目信息管理3"
    list_per_page = 5
#方法二，要将两个类关联起来
# admin.site.register(EngineerInfo,EngineerInfoAdmin)
@admin.register(OpcInfo)
class OpcInfoAdmin(admin.ModelAdmin):
    list_display = ['opcid', 'opctype']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(MachineInfo)
class MachineInfoAdmin(admin.ModelAdmin):
    list_display = ['machineid', 'machinetype']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(DatabaseInfo)
class DatabaseInfoAdmin(admin.ModelAdmin):
    list_display = ['databaseId', 'databasetype']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(CustomerInfo)
class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ['customerId', 'customername']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(BusInfo)
class BusInfoAdmin(admin.ModelAdmin):
    list_display = ['busId', 'busType']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(AdminInfo)
class AdminInfoAdmin(admin.ModelAdmin):
    list_display = ['adminId', 'adminName']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(PlcInfo)
class PlcInfoAdmin(admin.ModelAdmin):
    list_display = ['plcid', 'plctype']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(EitInfo)
class EitInfoAdmin(admin.ModelAdmin):
    list_display = ['eitid', 'eittype']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(ProjInfo)
class ProjInfoAdmin(admin.ModelAdmin):

    list_display = [
    'projid',
    'projno' ,
    'plannedwh' ,
    'location',
    'projstatusid' ,
    'projdescription' ,
    'customerid' ,
    'startingtime' ,
    'opcstatus' ,
    'serverstatus',
    'osstatus' ,
    'databasestatus' ,
    'opcidgroup' ,
    'serverid' ,
    'databaseid' ,
    'kodate',
    'customername' ,
    'servertype',
    'databasetype',
    ]
     
     
    #  如果你想在 admin 列表页显示外键（如 customerid）对应的 customername，
    #  需要在 ProjInfoAdmin 里自定义一个方法，然后在 list_display 里写这个方法名。
    
    def customername(self, obj):
        return obj.customerid.customername
    customername.short_description = '客户名称'
    
    def projstatus(self, obj):
        return obj.projstatusid.projstatustype
    projstatus.short_description = '项目状态'
    def databasetype(self, obj):
        return obj.databaseid.databasetype
    databasetype.short_description = '数据库类型'
    def servertype(self, obj):
        return obj.serverid.servertype
    servertype.short_description = '服务器类型'
    
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5

#在admin站点中定义OsInfo
@admin.register(OsInfo)
class OsInfoAdmin(admin.ModelAdmin):
    list_display = ['osid', 'ostype']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(ServerInfo)
class ServerInfoAdmin(admin.ModelAdmin):
    list_display = ['serverid', 'servertype']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(ProjStatus)
class ProjStatusAdmin(admin.ModelAdmin):
    list_display = ['projStatusId', 'projstatustype']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5
@admin.register(WorkHourInfo)
class WorkHourInfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'projid',
        'wbsid',
        'engineerid',
        'workdate',
        'weekno',
        'wh',
        'onsite',
        'comment' 
    ]
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5