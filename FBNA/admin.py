from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Source , Subject , Articl , User , commant
@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    pass

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass

@admin.register(commant)
class commantAdmin(ImportExportModelAdmin):
    pass

@admin.register(Articl)
class SArticlAdmin(ImportExportModelAdmin):
    pass

@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    pass



