from django.contrib import admin
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Projeto.
    Interface otimizada para gerenciar projetos do portfólio.
    """
    list_display = ('titulo', 'tecnologias', 'data_criacao', 'link')
    list_filter = ('data_criacao',)
    search_fields = ('titulo', 'descricao', 'tecnologias')
    readonly_fields = ('data_criacao',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao')
        }),
        ('Detalhes Técnicos', {
            'fields': ('tecnologias', 'imagem', 'link')
        }),
        ('Metadados', {
            'fields': ('data_criacao',),
            'classes': ('collapse',)
        }),
    )