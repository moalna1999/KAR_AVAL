from django.urls import include, path
from rest_framework import routers 
from . import views
from django.conf import settings
from django.conf.urls import  url
from .views import AdminstorsViewSet,FileView,ForeignKeyViewSet ,MyObtainTokenPairView,RegisterView
#from .views import UploadViewSet
from rest_framework_simplejwt.views import TokenRefreshView
router = routers.DefaultRouter()
router.register(r'member', views.MembersViewSet)
router.register(r'adminstor', AdminstorsViewSet)
router.register(r'ForeignKey', ForeignKeyViewSet)

#router.register(r'member1', views.MembersList)
#router.register(r'member1', views.MembersDetail)
urlpatterns = [
     path('', include(router.urls)),
     path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
     #path('member/', views.MembersList.as_view()),
     path('member/<int:pk>/', views.MembersDetail.as_view()),
     url(r'^upload/$', FileView.as_view(), name='file-upload'),
     path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
     path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('register/', RegisterView.as_view(), name='auth_register'),
]