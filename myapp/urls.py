from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.dashbaord,name='dashbaord'),
     path('home/',views.home,name='home'),
     path('home/manual/',views.manual,name='manual'),
     path('home/layout/',views.layout,name='layout'),
     path('viewlayout/',views.view_layout,name='view_layout'),
      path('edit-layout/<int:layout_id>/', views.edit_layout, name='edit_layout'),
     path('delete/<int:layout_id>/', views.delete_layout, name='delete_layout'),
     path('search_layout/',views.search_layout,name='search_layout'),
    path('edit/',views.editpage,name='editpage'),
      path('update/', views.update_details, name='update_details'),

]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
