from django.contrib import admin
from .models import Projeto, Certificacao

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


@admin.register(Certificacao)
class CertificacaoAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Certificacao.
    Interface otimizada para gerenciar certificações.
    """
    list_display = ('titulo', 'organizacao', 'data_obtencao', 'data_criacao')
    list_filter = ('organizacao', 'data_obtencao', 'data_criacao')
    search_fields = ('titulo', 'organizacao')
    readonly_fields = ('data_criacao',)
    date_hierarchy = 'data_obtencao'
    
    fieldsets = (
        ('Informações da Certificação', {
            'fields': ('titulo', 'organizacao', 'data_obtencao')
        }),
        ('Mídia e Links', {
            'fields': ('imagem', 'link')
        }),
        ('Metadados', {
            'fields': ('data_criacao',),
            'classes': ('collapse',)
        }),
    )