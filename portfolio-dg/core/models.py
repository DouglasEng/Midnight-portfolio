from django.db import models
from django.utils import timezone


class Projeto(models.Model):
    """
    Modelo para representar projetos do portfólio.
    Cada projeto é apresentado como um 'caso' no tema noir.
    """

    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    imagem = models.ImageField(upload_to='projetos/', verbose_name="Imagem", blank=True, null=True)
    tecnologias = models.CharField(max_length=300, verbose_name="Tecnologias Utilizadas", 
                                 help_text="Separe as tecnologias por vírgula")
    link = models.URLField(blank=True, null=True, verbose_name="Link do Projeto")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.titulo
    
    def listar_tecnologias(self):
        """Retorna lista de tecnologias separadas por vírgula"""
        return [tech.strip() for tech in self.tecnologias.split(',') if tech.strip()]


class Certificacao(models.Model):
    """
    Modelo para representar certificações e cursos.
    """
    
    titulo = models.CharField(max_length=200, verbose_name="Título da Certificação")
    organizacao = models.CharField(max_length=200, verbose_name="Organização")
    imagem = models.ImageField(upload_to='certificacoes/', verbose_name="Imagem", blank=True, null=True)
    link = models.URLField(blank=True, null=True, verbose_name="Link da Certificação")
    data_obtencao = models.DateField(blank=True, null=True, verbose_name="Data de Obtenção")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    
    class Meta:
        verbose_name = "Certificação"
        verbose_name_plural = "Certificações"
        ordering = ['-data_obtencao', '-data_criacao']
    
    def __str__(self):
        return f"{self.titulo} - {self.organizacao}"