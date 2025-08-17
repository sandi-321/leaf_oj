from django.contrib import admin

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'problem_id')
    ordering = ('problem_id',)
    search_fields = ["problem_id"]
# Register your models here.
from leaf_oj.models import *

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Submission)
admin.site.register(Contest)
admin.site.register(UserProfile)