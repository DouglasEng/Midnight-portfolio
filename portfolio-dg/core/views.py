from django.shortcuts import render, get_object_or_404
from .models import Projeto, Certificacao

def home(request):
    """
    View principal do portfólio.
    Exibe projetos, certificações e posts recentes do blog.
    """
    projetos = Projeto.objects.all()[:6]      # busca de projeto - limite de 6
    
    certificacoes = Certificacao.objects.all()[:4]     # busca de certificações - limite 4

    
    context = {
        'projetos': projetos,
        'certificacoes': certificacoes,
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