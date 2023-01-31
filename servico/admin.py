from django.contrib import admin

from servico.models import Servico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['horario', 'funcionario', 'cliente', 'situacao']
    search_fields = ('cliente', 'funcionario')
    list_filter = ('horario', 'situacao',)
