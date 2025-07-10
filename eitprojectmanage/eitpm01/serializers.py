from rest_framework import serializers
from .models import ProjInfo, AdminInfo, BusInfo, CustomerInfo, DatabaseInfo, EngineerInfo, MachineInfo, OpcInfo, EitInfo, OsInfo, PlcInfo, ProjStatus, ServerInfo, WbsInfo, WorkHourInfo

class ProjInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjInfo
        fields = '__all__'

class AdminInfoSerializer(serializers.ModelSerializer):
    """
    序列化器中的字段可以比模型中多，也可以比模型中少
    序列化器中的字段名称必须与模型找那个的字段名称相同
    AdminInfoSerializer(data=request.data)
    序列化器的主要功能就是把数据转成json(序列化),把json转成数据（反序列化）
    使用时AdminInfoSerializer(instance,data),序列化时传入instance参数，反序列化时需传入data参数
    """

    adminId = serializers.IntegerField(read_only= True,label='管理员ID')
    adminName = serializers.CharField(max_length=20, label='管理员名称',required=True) #requeired=True表示必填,默认不写的时候也是 True
    adminPwd = serializers.CharField(max_length=20, label='管理员密码')

class BusInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusInfo
        fields = '__all__'
class CustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInfo
        fields = '__all__'
class DatabaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseInfo
        fields = '__all__'
class EngineerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineerInfo
        fields = '__all__'

class WbsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WbsInfo
        fields = '__all__'
class OsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OsInfo
        fields = '__all__'

class PlcInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlcInfo
        fields = '__all__'
class ProjInfoSerializer(serializers.ModelSerializer):
    customername = serializers.CharField(source='customerid.customername', read_only=True)
    servertype = serializers.CharField(source='serverid.servertype', read_only=True)
    databasetype = serializers.CharField(source='databaseid.databasetype', read_only=True)
    ProjStatus = serializers.CharField(source='projstatusid.projstatustype', read_only=True)
    class Meta:
        model = ProjInfo
        fields = '__all__'

class WorkHourInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHourInfo
        fields = '__all__'

    class Meta:
        model = BusInfo
        fields = '__all__'
class ProjStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjStatus
        fields = '__all__'
class MachineInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineInfo
        fields = '__all__'
class ServerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfo
        fields = '__all__'


    class Meta:
        model = ProjInfo
        fields = '__all__'


class OpcInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcInfo
        fields = '__all__'
class EitInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EitInfo
        fields = '__all__'
class AdminInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminInfo
        fields = '__all__'