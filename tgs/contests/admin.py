from django.contrib import admin
from contests.models import Daily,Weekly,Monthly,TGS_Weeks,Djoin,Wjoin,Mjoin

# Register your models here.

@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display=['id','date','match_type','fees','total_games']

@admin.register(Weekly)
class WeeklyAdmin(admin.ModelAdmin):
    list_display=['id','date','match_type','fees','total_games']

@admin.register(Monthly)
class DailyAdmin(admin.ModelAdmin):
    list_display=['id','date','match_type','fees','total_games']

@admin.register(TGS_Weeks)
class TGS_WeeksAdmin(admin.ModelAdmin):
    list_display=['id','date','match_type','fees','total_games']

@admin.register(Djoin)
class DjoinAdmin(admin.ModelAdmin):
    list_display=['id','cid','date_time','team_name','leader_pname','second_pname','third_pname','fourth_pname','fifth_pname','whats_num','email','pay_ss','team_logo']

@admin.register(Wjoin)
class WjoinAdmin(admin.ModelAdmin):
    list_display=['id','cid','date_time','team_name','leader_pname','second_pname','third_pname','fourth_pname','fifth_pname','whats_num','email','pay_ss','team_logo']

@admin.register(Mjoin)
class MjoinAdmin(admin.ModelAdmin):
    list_display=['id','cid','date_time','team_name','leader_pname','second_pname','third_pname','fourth_pname','fifth_pname','whats_num','email','pay_ss','team_logo']
