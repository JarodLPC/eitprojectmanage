from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # django 类视图的路由绑定
    path('admins/<int:id>/', views.AdminInfoView.as_view(), name='admins_detail'),
    path('admins/', views.AdminInfoView.as_view(), name='admins_list'),
    path('opcs/<int:opc_id>/', views.OpcInfoView.as_view(), name='opcs_detail'),
    # path('databases/', views.DatabaseInfoView.as_view(), name='databases_list')
    # path('engineers/<int:id>/', views.EngineerInfoView.as_view(), name='engineers_detail'), 
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   

]

router = DefaultRouter()  # 创建路由器
router.register(r'engineers', views.EngineerInfoView,
                basename='engineers')  # 注册路由
router.register(r'projects', views.ProjectInfoView, basename='projects')
# router.register(r'databases',views.DatabaseInfoView,basename='databases')
urlpatterns += router.urls  # 把生成好的路由拼接到urlpatterns中
