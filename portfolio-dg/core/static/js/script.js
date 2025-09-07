document.addEventListener('DOMContentLoaded', function() {
    
    // animação de entrada
    const elements = document.querySelectorAll('.card, .blog-post, .section');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("fade-in");
                observer.unobserve(entry.target); 
            }
        });
    }, { threshold: 0.1 }); 
    elements.forEach(el => observer.observe(el));

    
    // navegação mobile
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // fecha menu ao clicar em um link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    
    // scroll suave
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // efeito scroll
    const header = document.querySelector('.main-header');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // header com efeito de transparencia
        if (header) {
            if (scrollTop > 100) {
                header.style.background = 'rgba(10, 10, 10, 0.98)';
                header.style.backdropFilter = 'blur(15px)';
            } else {
                header.style.background = 'rgba(10, 10, 10, 0.95)';
                header.style.backdropFilter = 'blur(10px)';
            }
        }
        
                
        lastScrollTop = scrollTop;
    });
    
    
    
    // efeitos de hover nos cards
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
            this.style.boxShadow = '0 25px 50px rgba(212, 175, 55, 0.2)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '0 20px 40px rgba(0, 0, 0, 0.5)';
        });
    });
    
    // efeito de digitação no nome
    const heroTitle = document.querySelector('.hero h1');
    if (heroTitle) {
        const text = heroTitle.textContent;
        heroTitle.textContent = '';
        heroTitle.style.borderRight = '2px solid var(--noir-gold)';
        
        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                heroTitle.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            } else {
                // remove cursor depois de terminar
                setTimeout(() => {
                    heroTitle.style.borderRight = 'none';
                }, 1000);
            }
        }
        
        setTimeout(typeWriter, 1000);
    }
    
    // efeito luz seguindo o mouse
    let mouseX = 0;
    let mouseY = 0;
    let lightBeam = document.querySelector('.light-beam');
    document.addEventListener('mousemove', function(e) {
        const lightBeam = document.querySelector('.light-beam');
        if (!lightBeam) return;

        const moveX = (e.clientX - window.innerWidth / 2) * 0.4;
        const moveY = (e.clientY - window.innerHeight / 2) * 0.4;

        lightBeam.style.transform = `translate(${moveX}px, ${moveY}px) rotate(${moveX * 0.2}deg)`;
    });

    
    // efeito de particulas
    function createParticle() {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: fixed;
            width: 2px;
            height: 2px;
            background: var(--noir-gold);
            pointer-events: none;
            z-index: -1;
            border-radius: 50%;
            opacity: 0.7;
            left: ${Math.random() * window.innerWidth}px;
            top: ${window.innerHeight + 10}px;
        `;
        
        document.body.appendChild(particle);
        
        // animar partícula
        let position = window.innerHeight + 10;
        const speed = Math.random() * 2 + 1;
        const drift = (Math.random() - 0.5) * 2;
        
        function animateParticle() {
            position -= speed;
            particle.style.top = position + 'px';
            particle.style.left = (parseFloat(particle.style.left) + drift) + 'px';
            particle.style.opacity = position / window.innerHeight;
            
            if (position < -10) {
                particle.remove();
            } else {
                requestAnimationFrame(animateParticle);
            }
        }
        
        animateParticle();
    }
    

    setInterval(createParticle, 3000);
    
    // lazy loading para imagens
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // efeito de sombra nas seções
    document.querySelectorAll('.section').forEach(section => {
        section.addEventListener('mouseenter', function() {
            this.style.boxShadow = 'inset 0 0 50px rgba(212, 175, 55, 0.1)';
        });
        
        section.addEventListener('mouseleave', function() {
            this.style.boxShadow = 'none';
        });
    });
    
    // contador animado para estatisticas
    function animateCounter(element, target) {
        let current = 0;
        const increment = target / 100;
        const timer = setInterval(() => {
            current += increment;
            element.textContent = Math.floor(current);
            
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            }
        }, 20);
    }
    
    // observar contadores e animar quando visiveis
    const counters = document.querySelectorAll('[data-count]');
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.dataset.count);
                animateCounter(entry.target, target);
                counterObserver.unobserve(entry.target);
            }
        });
    });
    
    counters.forEach(counter => counterObserver.observe(counter));
    
    // efeito de digitação em textos
    function typewriterEffect(element, text, speed = 50) {
        element.textContent = '';
        let i = 0;
        
        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        type();
    }
    
    
    // inicialização
    console.log('🔍 Portfolio Noir carregado com sucesso!');
    console.log('💼 Sistema de investigação digital ativo.');
    
    // executar animações iniciais
    setTimeout(() => {
        animateOnScroll();
    }, 500);
});

// utilitarios

// função para debounce (otimização de performance)
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// função para detectar dispositivo movel
function isMobile() {
    return window.innerWidth <= 768;
}

// função para smooth scroll personalizado
function smoothScrollTo(target, duration = 1000) {
    const targetElement = document.querySelector(target);
    if (!targetElement) return;
    
    const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;
    
    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
    }
    
    function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }
    
    requestAnimationFrame(animation);
}

