from django.contrib import admin

from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ["text",]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("text",)
    search_fields = ("text",)


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
admin.site.register(models.Vote)
