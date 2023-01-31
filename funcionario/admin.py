from django.contrib import admin
from django.utils.html import format_html
from funcionario.models import Funcionario


@admin.register(Funcionario)
class FunconarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fone', 'endereco', 'cpf', 'foto', 'fotografia')
    search_fields = ('nome', 'fone')
    list_filter = ('nome',)

    def fotografia(self, obj):
        if obj.foto:
            return format_html('<img width="75px" src"{}" />', obj.foto.url)
        pass
