from django.contrib import admin
from .models import Choice, Question

# Register your models here.
#admin.site.register(Question)
#admin.site.register(Choice)

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question to Ask',                  {"fields":['question_text']}),
        ('Date Information',    {"fields":['pub_date'], "classes":['collapse']}),
    ]
    inlines = [ChoiceInline]
#    fields = ['pub_date', 'question_text']
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
