from django.shortcuts import render, get_object_or_404
from .models import Projeto, Certificacao, PostBlog
from django.core.paginator import Paginator


def home(request):
    """
    View principal do portfólio.
    Exibe projetos, certificações e posts recentes do blog.
    """
    projetos = Projeto.objects.all()[:6]      # busca de projeto - limite de 6
    
    certificacoes = Certificacao.objects.all()[:4]     # busca de certificações - limite 4

    posts_recentes = PostBlog.objects.filter(publicado=True)[:3]  # 3 posts mais recentes

    context = {
        'projetos': projetos,
        'certificacoes': certificacoes,
        'posts_recentes': posts_recentes,

        'page_title': 'DouglasEng - Investigador Digital'
    }
    
    return render(request, 'index.html', context)

def projetos(request):
    """
    View para listar todos os projetos.
    Página dedicada aos projetos com mais detalhes.
    """
    projetos = Projeto.objects.all()
    
    context = {
        'projetos': projetos,
        'page_title': 'Casos Resolvidos - Projetos'
    }
    
    return render(request, 'projetos_list.html', context)

def certificacoes(request):
    """
    View para listar todas as certificações.
    Página dedicada às certificações com mais detalhes.
    """
    certificacoes = Certificacao.objects.all()
    
    context = {
        'certificacoes': certificacoes,
        'page_title': 'Credenciais do Investigador - Certificações'
    }
    
    return render(request, 'certificacoes_list.html', context)



def blog_detalhes(request, slug):
    """
    View para exibir um post específico do blog.
    Usa slug para URLs amigáveis.
    """
    post = get_object_or_404(PostBlog, slug=slug, publicado=True)
    
    posts_relacionados = PostBlog.objects.filter(
        publicado=True
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'posts_relacionados': posts_relacionados,
        'page_title': f'{post.titulo} - Blog'
    }
    
    return render(request, 'blog_detalhes.html', context)