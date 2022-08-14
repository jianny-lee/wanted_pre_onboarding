from django.urls import include, path

from . import views

app_name = 'wanted'
urlpatterns = [
    path('', views.company_list, name = 'company'),
    path('<int:company_id>/',views.company_detail, name='detail'),
    path('create/', views.company_create, name='create'),
    path('edit/<int:company_id>/',views.company_edit, name='edit'),
    path('delete/<int:company_id>',views.company_delete, name='delete')
]