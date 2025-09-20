# 🕵️ Portfolio Noir

Este é um portfólio de projetos estilo **noir**, com visual elegante e escuro, pensado para você que deseja apresentar seu trabalho de forma impactante. Ele reúne seus projetos, posts autorais e demonstrações de código, oferecendo tanto uma exibição pública quanto um ambiente privado para desenvolvimento e testes.

<h1 style="font-size:100px;">
 <a href="https://douglaseng.pythonanywhere.com">douglaseng.pythonanywhere.com</a>
</h1>

<p align="center">
  <img src="midnight-portfolio.png" alt="Portfólio Noir" width="100%">
</p>

## 📑 Sumário
- [Funcionalidades Técnicas](#-funcionalidades-técnicas)
- [Estrutura do Site](#-estrutura-do-site)
- [Design Noir](#-design-noir)
- [Configuração e Uso](#-configuração-e-uso)
- [Contribuindo](#-contribuindo-e-testando)
- [Licença](#-licença)
- [Autor](#-autor)


## 📊 Funcionalidades Técnicas

* **Frontend**: responsivo, performance otimizada, acessível, SEO-friendly.
* **Backend**: Django moderno, URLs amigáveis, modelos robustos.
* **JavaScript**: menu mobile, scroll suave, animações e interatividade dinâmica.

## 📱 Estrutura do Site

* **Página Inicial**: hero section, biografia, projetos em destaque, certificações, posts recentes e contato.
* **Projetos**: `/projetos/` — lista completa com estatísticas.
* **Certificações**: `/certificacoes/` — timeline com datas e especialidades.
* **Blog**: `/blog/` e `/blog/<slug>/` — posts com conteúdo técnico detalhado e relacionados.

## 🎨 Design Noir

* **Paleta de cores**: Preto (#0a0a0a), Cinza Escuro (#1a1a1a), Dourado (#d4af37), Âmbar (#ffb347), Vermelho Escuro (#8b0000)
* **Efeitos visuais**: sombras, fade-in/out, digitação no título, transições suaves e interações dinâmicas.

## 🔧 Personalização

* Alterar cores pelo CSS em `portfolio/static/css/style.css`.
* Atualizar conteúdos editando templates ou usando o Admin.
* Adicionar novas funcionalidades como formulário de contato, comentários no blog ou categorias de projetos.

## 📂 Estrutura de Arquivos

* `portfolio/`: configurações do Django.
* `core/`: app principal com models, views, admin, templates e static.
* `media/`: uploads de usuário.
* `manage.py`: script principal Django.

## 🛠️ Administração

* Interface Django Admin personalizada com tema noir.
* Modelos: Projeto, Certificação, Post do Blog.
* Funcionalidades: busca avançada, filtros, slugs automáticos e organização por datas.

## 🛠️ Configuração e Uso

* Coloque sua SECRET\_KEY DJANGO em `settings.py`:

```python
from .settings_base import *

# Segurança
SECRET_KEY = 'your-public-placeholder-key'
DEBUG = True
ALLOWED_HOSTS = ['*']  # ou deixar vazio

# Banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

> Para rodar o portfólio durante o desenvolvimento, descomente no `urls.py` principal:
>
> ```python
> if settings.DEBUG:
>     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
> ```

### Executando o servidor

1. Navegue até a pasta do projeto: `cd portfolio-dg`
2. Execute o servidor: `python manage.py runserver`
3. Acesse o site principal: `http://127.0.0.1:8000/`
4. Painel Admin: `http://127.0.0.1:8000/admin/`

   * Usuário: `admin`
   * Email: `admin@portfolionoir.com`
   * Senha: `investigador123`

## 🤝 Contribuindo e Testando

Se você deseja contribuir para o projeto ou testá-lo localmente, siga estes passos detalhados:

1. **Fork do repositório**

   * Clique em "Fork" no GitHub para criar uma cópia do projeto na sua conta.
2. **Clone o fork localmente**

   * `git clone https://github.com/douglaseng/midnight-portfolio.git`
3. **Crie uma branch para desenvolvimento**

   * `git checkout -b minha-feature`
4. **Instale dependências**

   * Crie um ambiente virtual: `python -m venv venv`
   * Ative o ambiente e instale dependências: `pip install -r requirements.txt`
5. **Configurar settings para teste**

   * Copie `settings_public.py` para `settings_local.py` e insira sua própria SECRET\_KEY e configurações de banco de dados.
6. **Executar o servidor local**

   * `python manage.py runserver`
   * Teste suas alterações acessando `http://127.0.0.1:8000/`
7. **Commit e Push das alterações**

   * `git add .`
   * `git commit -m "Descrição das alterações"`
   * `git push origin minha-feature`
8. **Abrir Pull Request**

   * No GitHub, abra um Pull Request para integrar suas alterações ao repositório principal.

> **Atenção:** Nunca inclua chaves ou credenciais sensíveis nos commits ou PRs.

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Douglas Rodrigues**  
Estudante de Desenvolvimento de Sistemas e Ciência de Dados  
[LinkedIn](https://www.linkedin.com/in/douglas-rodrigues-44364b316/) | [GitHub](https://github.com/douglaseng)


---

**🕵️ “Caso encerrado com sucesso. O investigador digital está pronto para ação!”**
