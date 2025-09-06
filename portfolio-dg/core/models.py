from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

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
    


class PostBlog(models.Model):
    """
    Modelo para posts do blog.
    Cada post é como uma 'investigação' ou 'relatório' no tema noir.
    """
    titulo = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug", 
                           help_text="URL amigável (será gerada automaticamente se deixar em branco)")
    conteudo = models.TextField(verbose_name="Conteúdo")
    autor = models.CharField(max_length=100, verbose_name="Autor", default="Investigador")
    data_publicacao = models.DateTimeField(default=timezone.now, verbose_name="Data de Publicação")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    publicado = models.BooleanField(default=True, verbose_name="Publicado")
    
    class Meta:
        verbose_name = "Post do Blog"
        verbose_name_plural = "Posts do Blog"
        ordering = ['-data_publicacao']
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        """Gera slug automaticamente se não fornecido"""
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """Retorna URL absoluta do post"""
        return reverse('blog_detail', kwargs={'slug': self.slug})