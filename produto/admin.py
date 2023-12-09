from django.contrib import admin
from . import models


class varInLine(admin.TabularInline):
    model = models.Var
    extra = 1

class produtoAdmin(admin.ModelAdmin):
    inlines = [
        varInLine
    ]

admin.site.register(models.Produto, produtoAdmin)
admin.site.register(models.Var)