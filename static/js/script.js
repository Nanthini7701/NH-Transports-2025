/* ============================================
   NH TRANSPORTS - Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all features
    initializeScrollAnimations();
    initializeNavbar();
    initializeButtons();
    initializeSlideshow();
    dismissAlerts();
    initializeHeroAnimations();
});

/* ============================================
   HERO ANIMATIONS
   ============================================ */

function initializeHeroAnimations() {
    const heroTitle = document.querySelector('.hero-title');
    const heroSubtitle = document.querySelector('.hero-subtitle');
    const heroDescription = document.querySelector('.hero-description');
    const heroButtons = document.querySelector('.hero-buttons');
    const heroContactStrip = document.querySelector('.hero-contact-strip');

    if (heroTitle) {
        setTimeout(() => heroTitle.style.animation = 'fadeInUp 0.8s ease-out forwards', 200);
    }
    if (heroSubtitle) {
        setTimeout(() => heroSubtitle.style.animation = 'fadeInUp 0.8s ease-out 0.15s forwards', 400);
    }
    if (heroDescription) {
        setTimeout(() => heroDescription.style.animation = 'fadeInUp 0.8s ease-out 0.3s forwards', 600);
    }
    if (heroButtons) {
        setTimeout(() => heroButtons.style.animation = 'fadeInUp 0.8s ease-out 0.45s forwards', 800);
    }
    if (heroContactStrip) {
        setTimeout(() => heroContactStrip.style.animation = 'fadeInUp 0.8s ease-out 0.6s forwards', 1000);
    }
}

/* ============================================
   SCROLL ANIMATIONS
   ============================================ */

function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all cards and sections
    const elements = document.querySelectorAll(
        '.feature-card, .service-item, .service-detail-card, ' +
        '.testimonial-card, .contact-info-card, .team-member, ' +
        '.value-card, .achievement-item, .process-step, .fleet-item, ' +
        '.fade-in-section'
    );

    elements.forEach(el => {
        observer.observe(el);
    });
}

/* ============================================
   NAVBAR FUNCTIONALITY
   ============================================ */

function initializeNavbar() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    // Sticky navbar on scroll
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.2)';
        } else {
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        }
    });

    // Close navbar on link click
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            const navbarToggle = document.querySelector('.navbar-toggler');
            const navbarCollapse = document.querySelector('.navbar-collapse');
            
            if (navbarCollapse.classList.contains('show')) {
                navbarToggle.click();
            }
        });
    });

    // Highlight active link
    const currentLocation = location.pathname;
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (currentLocation === href || currentLocation.startsWith(href + '/')) {
            link.style.color = '#f39c12';
        }
    });
}

/* ============================================
   BUTTON ANIMATIONS
   ============================================ */

function initializeButtons() {
    const buttons = document.querySelectorAll('.btn-hover');

    buttons.forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });

        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

/* ============================================
   SLIDESHOW/BANNER
   ============================================ */

function initializeSlideshow() {
    const carousel = document.querySelector('.carousel');
    if (carousel) {
        const bsCarousel = new bootstrap.Carousel(carousel, {
            interval: 5000,
            wrap: true,
            pause: 'hover'
        });
    }
}

/* ============================================
   AUTO-DISMISS ALERTS
   ============================================ */

function dismissAlerts() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
}

/* ============================================
   SMOOTH SCROLL FOR ANCHOR LINKS
   ============================================ */

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

/* ============================================
   COUNTER ANIMATION
   ============================================ */

let statsAnimated = false;

window.addEventListener('scroll', () => {
    const statsSection = document.querySelector('.statistics');
    if (statsSection && !statsAnimated) {
        const rect = statsSection.getBoundingClientRect();
        if (rect.top < window.innerHeight) {
            animateCounters();
            statsAnimated = true;
        }
    }
});

function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target') || counter.textContent);
        const increment = target / 50;
        let count = 0;

        const interval = setInterval(() => {
            count += increment;
            if (count >= target) {
                counter.textContent = counter.textContent;
                clearInterval(interval);
            } else {
                counter.textContent = Math.ceil(count) + '+';
            }
        }, 40);
    });
}

/* ============================================
   FORM VALIDATION ENHANCEMENT
   ============================================ */

const form = document.querySelector('.needs-validation');
if (form) {
    form.addEventListener('submit', function(event) {
        // Clear previous error messages
        const errorMessages = form.querySelectorAll('.error-message');
        errorMessages.forEach(msg => msg.remove());

        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        
        form.classList.add('was-validated');
    });

    // Real-time validation feedback
    const inputs = form.querySelectorAll('.form-control');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            if (this.value) {
                this.classList.remove('is-invalid');
            }
        });
    });
}

/* ============================================
   PHONE NUMBER FORMATTING
   ============================================ */

const phoneInput = document.querySelector('input[name="phone"]');
if (phoneInput) {
    phoneInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        
        if (value.length >= 6) {
            value = '+' + value.slice(0, 1) + '-' + 
                   value.slice(1, 4) + '-' + 
                   value.slice(4, 7) + '-' + 
                   value.slice(7, 11);
        }
        
        e.target.value = value;
    });
}

/* ============================================
   SCROLL TO TOP BUTTON
   ============================================ */

// Create scroll to top button
const scrollTopBtn = document.createElement('button');
scrollTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
scrollTopBtn.className = 'scroll-to-top';
scrollTopBtn.style.cssText = `
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(135deg, #003d82 0%, #005fa3 100%);
    color: white;
    border: none;
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    z-index: 999;
    transition: all 0.3s ease;
    box-shadow: 0 5px 15px rgba(0, 61, 130, 0.4);
`;

document.body.appendChild(scrollTopBtn);

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        scrollTopBtn.style.display = 'flex';
    } else {
        scrollTopBtn.style.display = 'none';
    }
});

scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

scrollTopBtn.addEventListener('mouseover', function() {
    this.style.transform = 'scale(1.1)';
});

scrollTopBtn.addEventListener('mouseout', function() {
    this.style.transform = 'scale(1)';
});

/* ============================================
   ENHANCE TESTIMONIAL DISPLAY
   ============================================ */

function enhanceTestimonials() {
    const testimonials = document.querySelectorAll('.testimonial-card');
    
    testimonials.forEach((testimonial, index) => {
        // Add staggered animation delay
        testimonial.style.animationDelay = `${index * 0.1}s`;
    });
}

enhanceTestimonials();

/* ============================================
   WHATSAPP LINK GENERATOR
   ============================================ */

window.getWhatsAppLink = function(phoneNumber, message = '') {
    const encodedMessage = encodeURIComponent(message);
    return `https://wa.me/${phoneNumber}?text=${encodedMessage}`;
};

/* ============================================
   UTILITY FUNCTIONS
   ============================================ */

// Format phone number for display
window.formatPhoneNumber = function(phoneString) {
    const cleaned = ('' + phoneString).replace(/\D/g, '');
    const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
    if (match) {
        return '(' + match[1] + ') ' + match[2] + '-' + match[3];
    }
    return phoneString;
};

// Get current date
window.getCurrentYear = function() {
    return new Date().getFullYear();
};

// Debounce function for scroll events
window.debounce = function(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
};

/* ============================================
   LOGGER FOR DEBUGGING
   ============================================ */

window.log = function(message, type = 'log') {
    if (window.DEBUG) {
        console[type](`[NH Transports] ${message}`);
    }
};

window.DEBUG = false; // Set to true for debugging

// Log page load
window.log('Page loaded successfully');
