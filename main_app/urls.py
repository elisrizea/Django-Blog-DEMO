"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from django.urls import path,include
from rest_framework.routers import SimpleRouter

from . import views

from .views import PostApiVewSet

router = SimpleRouter()
router.register('', PostApiVewSet)

urlpatterns = [
    path('', views.posts,name='home'),

    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('add_post/', views.add_post, name='add_post'),
    path('posts/', views.posts, name='posts'),
    path('api/', include(router.urls)),

]

