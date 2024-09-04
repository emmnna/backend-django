from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# patterns = [
#     path('', include('crm.urls')),
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
#     path('', include('authentification.urls')),
#     ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('api/', include('authentification.urls')),
    path('api/', include('crm.urls')),

]
