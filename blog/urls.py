from django.urls import path
from .views import (
    home_view,
    about_view, 
    students_view, 
    detailt_student_view,
    create_student_view,
    edit_student_view,
    delete_student_view
)

from foydalanuvchi.views import (
    login_view,
    logout_view,
    register_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('students/', students_view, name='students'),

    path('detail-student/<int:id>/', detailt_student_view, name='detail_student'),
    path('create-student/', create_student_view, name='create_student'),
    path('edit-student/<int:id>/', edit_student_view, name='edit_student'),
    path('delete-student/<int:id>/', delete_student_view, name='delete_student'),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]