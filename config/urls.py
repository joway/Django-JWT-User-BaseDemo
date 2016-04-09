"""GeneralUser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

# JWT

# API
from .router import router

"""
/admin
/api/v1/auth jwt 用户认证
/api/v1/oauth oauth 用户认证
"""

jwt_urlpatterns = [
    url(r'^$', obtain_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
    url(r'^verify/', verify_jwt_token),
    url(r'^register/', 'users.apis.register'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', include(jwt_urlpatterns)),
    url(r'^api/v1/oauth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include(router.urls)),
    url(r'$', 'users.views.index'),
]
