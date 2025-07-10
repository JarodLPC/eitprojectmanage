from django.utils import timezone
from django.http import HttpResponse,JsonResponse
from rest_framework.viewsets import ModelViewSet # DRM中的类视图集
from django.views import View
from django.views.generic.detail import DetailView
from eitpm01.models import AdminInfo,OpcInfo,EngineerInfo,DatabaseInfo,ProjInfo,WbsInfo,PlcInfo,OsInfo,ServerInfo,MachineInfo,EitInfo,CustomerInfo,BusInfo,ProjStatus,WorkHourInfo
from eitpm01.serializers import EngineerInfoSerializer,DatabaseInfoSerializer,ProjInfoSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
#引入IsAuthenticated
from rest_framework.permissions import IsAuthenticated

#利用django的view类来定义视图
class AdminInfoView(View):
    def __init__(self, **kwargs):
        super(AdminInfoView,self).__init__(**kwargs)
        self.result = {
            'code': 200,
            'msg': 'success',
            'data': {}
        }
    def post(self,request):
        return HttpResponse('post')
    def get(self,request):
        result = self.result
        admins = AdminInfo.objects.all()
        json_data = [{'adminId':admin.adminId,'adminName':admin.adminName,'adminPwd':admin.adminPwd} for admin in admins]
        result['data'] =json_data      
        return JsonResponse(result, content_type='application/json')
    def get(self,request,id=None):
        result = self.result
        if id:
            try:
                admin = AdminInfo.objects.get(adminId=id)
                json_data = {'adminId':admin.adminId,'adminName':admin.adminName,'adminPwd':admin.adminPwd}
                result['data'] =json_data
            except AdminInfo.DoesNotExist:
                result['code'] = 404
                result['msg'] = 'Admin not found'
        else:
            admins = AdminInfo.objects.all()
            json_data = [{'adminId':admin.adminId,'adminName':admin.adminName,'adminPwd':admin.adminPwd} for admin in admins]
            result['data'] =json_data
        return JsonResponse(result, content_type='application/json')
    # def get(self,request):
     
    #     admins = AdminInfo.objects.all()
    #     print(admins)
    #     admins = [{'adminId':admin.adminId,'adminName':admin.adminName,'adminPwd':admin.adminPwd} for admin in admins]
    #     # json_data= json.dumps(admins)
    #     # print(json_data)
    #     return JsonResponse(admins, safe=False, content_type='application/json'
#利用DRF
class OpcInfoView(DetailView):
    #
    model = OpcInfo
    
    pk_url_kwarg = 'opc_id'  # 指定 URL 参数为 opc_id
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        print(context)
        return context


#利用DRF
class EngineerInfoView(ModelViewSet):
    #指定查询集
    queryset = EngineerInfo.objects.all()
    #指定序列化器
    serializer_class = EngineerInfoSerializer
    filterset_fields = ['engineerId', 'engineerName', 'engineerpwd', 'telephoneno']
    
    # filter_fields = ['engineerId', 'engineerName', 'engineerpwd', 'telephoneno']

    
class ProjectInfoView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProjInfo.objects.all()
    serializer_class = ProjInfoSerializer
    filterset_fields = ['projid', 'projno', 'projdescription', 'startingtime', 'plannedwh',
                         'projstatusid', 'customerid', 'databaseid', 'databasestatus', 
                         'serverid', 'serverstatus', 'opcidgroup', 'opcstatus', 'osstatus',
                           'kodate', 'location']
   
      
# class DatabaseInfoView(ListAPIView):
#     queryset = DatabaseInfo.objects.all()
#     serializer_class = DatabaseInfoSerializer
#     filter_fields = ['databasetype','databaseId']



