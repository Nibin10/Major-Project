"""blind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    path("",views.home,name='home'),
    #url(r'^logout/$', 'django_social_app.views.logout'),
    #path('logout/',views.logout,name='logout'),
    path('send/',views.send,name='send'),
    path('search/',views.search,name='search'),
    path('email/',views.email,name='email'),
    path('calculator/',views.calculator,name='calculator'),
    path('book/',views.book,name='book'),
    path('inbox/',views.inbox,name='inbox'),
    path('compose/',views.compose,name='compose'),
    path('readmail/',views.readmail,name='readmail'),
    path('bookplay/',views.bookplay,name='bookplay'),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
