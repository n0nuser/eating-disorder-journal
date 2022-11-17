from django.contrib import admin
from web.models import Journal, Thought, Sport, Measurements, Food, ForTheBetterLife, HealReasons, ProsCons
from import_export.admin import ImportExportMixin


class JournalAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("ocurred_at", "user", "number_of_times", "situation_emotion", "afterwards_feeling")

class ThoughtAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("created_at", "user", "thought")

class SportAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "ocurred_at", "sport", "duration")

class MeasurementsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "ocurred_at", "weight", "height")

class FoodAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "ocurred_at", "meal", "food", "amount")

class ForTheBetterLifeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "text")
    
class HealReasonsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "reason")

class ProsConsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "type", "text")

admin.site.register(Journal, JournalAdmin)
admin.site.register(Thought, ThoughtAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Measurements, MeasurementsAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(ForTheBetterLife, ForTheBetterLifeAdmin)
admin.site.register(HealReasons, HealReasonsAdmin)
admin.site.register(ProsCons, ProsConsAdmin)

admin.site.site_header = "Journal"
admin.site.site_title = "Journal"
