// Enhanced JavaScript for better user experience
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling behavior for navigation links
    const navLinks = document.querySelectorAll('nav a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Add active state visual feedback
                navLinks.forEach(nl => nl.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });

    // Add intersection observer for fade-in animations
    const sections = document.querySelectorAll('section');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const sectionObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                entry.target.classList.add('section-visible');
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    // Add hover effects for cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Add sparkle effect for the love section
    const loveSection = document.querySelector('.love-section');
    if (loveSection) {
        // Create floating hearts animation
        function createHeart() {
            const heart = document.createElement('div');
            heart.innerHTML = '❤️';
            heart.style.position = 'absolute';
            heart.style.fontSize = '20px';
            heart.style.pointerEvents = 'none';
            heart.style.animation = 'floatUp 3s linear forwards';
            heart.style.left = Math.random() * 100 + '%';
            heart.style.zIndex = '1000';
            
            loveSection.style.position = 'relative';
            loveSection.appendChild(heart);
            
            setTimeout(() => {
                if (heart.parentNode) {
                    heart.parentNode.removeChild(heart);
                }
            }, 3000);
        }

        // Add floating hearts every 2 seconds
        setInterval(createHeart, 2000);
    }

    // Add typing effect for main heading
    const mainHeading = document.querySelector('#home h1');
    if (mainHeading) {
        const originalText = mainHeading.textContent;
        mainHeading.textContent = '';
        
        let i = 0;
        function typeWriter() {
            if (i < originalText.length) {
                mainHeading.textContent += originalText.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        
        // Start typing effect after a short delay
        setTimeout(typeWriter, 500);
    }
});

// Add CSS for floating hearts animation
const style = document.createElement('style');
style.textContent = `
    @keyframes floatUp {
        0% {
            transform: translateY(0px);
            opacity: 1;
        }
        100% {
            transform: translateY(-100px);
            opacity: 0;
        }
    }
    
    nav a.active {
        background: rgba(255, 255, 255, 0.3) !important;
        box-shadow: 0 2px 10px rgba(255, 255, 255, 0.3);
    }
    
    .section-visible {
        animation: sectionFadeIn 0.8s ease-out;
    }
    
    @keyframes sectionFadeIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);