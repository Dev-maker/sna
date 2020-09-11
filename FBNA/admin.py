from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Source , Subject , Article , Profile , comment



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','link','date','source')
    list_filter = ['title']
    search_fields = ['title','link','date','source']




class commentAdmin(admin.ModelAdmin):
    list_display = ('date','comment','article','user')
    list_filter = ['article']
    search_fields =['date','comment','article','user']

class ProfiletAdmin(admin.ModelAdmin):
    list_display = ('name','email','facebook','location','phone')
    list_filter = ['name']
    search_fields = ['name','email','facebook','location','phone']



admin.site.register(Article,ArticleAdmin)

admin.site.register(Source)
admin.site.register(Subject)
admin.site.register(Profile,ProfiletAdmin)
admin.site.register(comment,commentAdmin)




