from django.contrib import admin
from contests.models import Daily,Weekly,Monthly

# Register your models here.

@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display=['id','d_date','d_type','d_fees','d_tgames']

@admin.register(Weekly)
class WeeklyAdmin(admin.ModelAdmin):
    list_display=['id','w_date','w_type','w_fees','w_tgames']

@admin.register(Monthly)
class DailyAdmin(admin.ModelAdmin):
    list_display=['id','m_date','m_type','m_fees','m_tgames']