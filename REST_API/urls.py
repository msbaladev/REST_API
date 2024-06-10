from django.urls import  path
from .views import *
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    path('get_data/',get_data,name='get_data'),
    
    
    
    
     # Authentication
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/user/', user_detail_view, name='user-detail'),
    
]