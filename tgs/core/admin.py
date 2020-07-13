from django.contrib import admin
from core.models import Winner

# Register your models here.

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display=['id','team_name','team_img']