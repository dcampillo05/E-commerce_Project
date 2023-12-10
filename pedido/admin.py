from django.contrib import admin
from . import models

class itemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1

class pedidoAdmin(admin.ModelAdmin):
    inline = {
        itemPedidoInline
    }

admin.site.register(models.Pedido, pedidoAdmin)
admin.site.register(models.ItemPedido)
