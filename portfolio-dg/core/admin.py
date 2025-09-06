from django.contrib import admin
from .models import Projeto, Certificacao, PostBlog

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


@admin.register(PostBlog)
class PostBlogAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo PostBlog.
    Interface otimizada para gerenciar posts do blog.
    """
    list_display = ('titulo', 'autor', 'publicado', 'data_publicacao', 'data_atualizacao')
    list_filter = ('publicado', 'data_publicacao', 'autor')
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
    readonly_fields = ('data_criacao', 'data_atualizacao')
    date_hierarchy = 'data_publicacao'
    
    fieldsets = (
        ('Conteúdo do Post', {
            'fields': ('titulo', 'slug', 'conteudo', 'autor')
        }),
        ('Configurações de Publicação', {
            'fields': ('publicado', 'data_publicacao')
        }),
        ('Metadados', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Personaliza o salvamento do modelo no admin"""
        if not change:  # Se é um novo objeto
            obj.autor = request.user.get_full_name() or request.user.username
        super().save_model(request, obj, form, change)


# personalização do site admin
admin.site.site_header = "Portfolio Noir - Administração"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Painel de Controle do Investigador"