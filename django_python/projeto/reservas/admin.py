from django.contrib import admin
from .models import Cliente, Reservas

# Register your models here.
class Reservas_inline(admin.StackedInline):
    model = Reservas
    extra = 3

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'registro_eh_antigo')

    list_filter = ['registrado_em']
    search_fields = ['nome']

    fieldsets = [
        (None, {'fields': ['nome', 'email', 'telefone', 'endereco']}),
        ('Datas', {'fields': ['registrado_em'],
                   'classes':['collapse']})]
    inlines = [Reservas_inline]

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reservas)
