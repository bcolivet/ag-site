/* ===================================================
   AUTONOMOUS GROWTH — v0 Site Scripts
   =================================================== */

// --- NAV SCROLL EFFECT ---
const nav = document.getElementById('nav');
let lastScroll = 0;

function handleNavScroll() {
  const currentScroll = window.scrollY;
  if (currentScroll > 20) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
  lastScroll = currentScroll;
}

window.addEventListener('scroll', handleNavScroll, { passive: true });


// --- SMOOTH SCROLL FOR ANCHOR LINKS ---
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href');
    if (targetId === '#') return;

    const target = document.querySelector(targetId);
    if (target) {
      e.preventDefault();
      const navHeight = 72;
      const targetPosition = target.getBoundingClientRect().top + window.scrollY - navHeight;
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  });
});


// --- SCROLL REVEAL ANIMATIONS ---
const revealElements = document.querySelectorAll(
  '.hero-headline, .hero-sub, .hero .btn, ' +
  '.section-label, .section-headline, .body-text, ' +
  '.card, .step, .testimonial, .pricing-card'
);

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      revealObserver.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.1,
  rootMargin: '0px 0px -40px 0px'
});

// Add initial hidden state and observe
revealElements.forEach((el, index) => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = `opacity 0.6s ease ${index % 4 * 0.1}s, transform 0.6s ease ${index % 4 * 0.1}s`;
  revealObserver.observe(el);
});

// CSS class for revealed state
const style = document.createElement('style');
style.textContent = `
  .revealed {
    opacity: 1 !important;
    transform: translateY(0) !important;
  }
`;
document.head.appendChild(style);


// --- LOGO SCROLL DUPLICATION (ensures seamless loop) ---
const scrollInner = document.querySelector('.logo-scroll-inner');
if (scrollInner) {
  // The logos are already duplicated in HTML for seamless scrolling
  // This ensures the animation width is correct
  const scrollWidth = scrollInner.scrollWidth;
  const halfWidth = scrollWidth / 2;

  // Pause on hover
  const scrollWrapper = document.querySelector('.logo-scroll-wrapper');
  if (scrollWrapper) {
    scrollWrapper.addEventListener('mouseenter', () => {
      scrollInner.style.animationPlayState = 'paused';
    });
    scrollWrapper.addEventListener('mouseleave', () => {
      scrollInner.style.animationPlayState = 'running';
    });
  }
}
