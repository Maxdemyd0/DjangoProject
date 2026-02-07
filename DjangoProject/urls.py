"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('home/elements/<int:index>/<str:name>', views.page_elements),
    path('calc/', views.calc),
    path('calc/<str:operation>/<int:a>/<int:b>', views.calculate),
    path('', views.website),

    path('register/', views.post_handler),
    path('course/', views.courses),
    path('course/<str:level>', views.course_by_level),
]
