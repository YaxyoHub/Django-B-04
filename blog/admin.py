from django.contrib import admin
from .models import Student

# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'familiya', 'yosh', 'manzil', 'is_active', 'created_at')
    list_editable = ('yosh', 'is_active')
    list_display_links = ('ism', 'familiya',)
