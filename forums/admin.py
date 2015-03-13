from django.contrib import admin
from forums.models import Subject
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_title','subject_desc','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Subject,SubjectAdmin)
