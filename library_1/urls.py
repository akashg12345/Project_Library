"""library_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from books import views
from books.views import homepage
from django.contrib import admin
from django.urls import  path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',homepage,name="homepage"),
    path('show_all_table/',views.show_all_table,name="show_all_table"),
    path('edit/<int:bid>/', views.edit_data, name="edit"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('Soft_Delete_All', views.Soft_Delete_All, name="Soft_Delete_All"),
    path('Show_All_Soft_Deleted', views.Show_All_Soft_Deleted, name="Show_Soft"),
    path('Soft_Delete/<int:id>/', views.Soft_Delete, name="Soft_Delete"),
    path('Restore/<int:id>/', views.Restore_Soft_Deleted, name="Restore_Deleted"),
    # path('__debug__/', include("debug_toolbar.urls")),



]
