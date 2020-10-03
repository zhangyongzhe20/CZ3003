from django.contrib import admin

# Register your models here.
from .models import World, Section, questionHistory


class questionHistoryInline(admin.TabularInline):
	model = questionHistory

class gameAdmin(admin.ModelAdmin):
	inlines = [questionHistoryInline,]

admin.site.register(questionHistory)
admin.site.register(World)
admin.site.register(Section)


