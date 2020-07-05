from django.urls import path

from index import views

urlpatterns =[
    path("register/",views.UserAPIView.as_view()),
    path("emp/",views.EmployeeAPIView.as_view()),
    path("emp/<str:id>/",views.EmployeeAPIView.as_view()),
    path("up/<str:id>/",views.UpdateAPIView.as_view()),

]