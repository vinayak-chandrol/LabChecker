from django.urls import path
from .views import upload_report,report_list,delete

urlpatterns =[
    path('upload/',upload_report,name='upload_report'),
    path('reports/',report_list,name='report_list'),
    path('delete/<int:id>/',delete,name='delete')
]