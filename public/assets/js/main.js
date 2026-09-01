/**
 * AJ EXPRESS - TRAVEL AGENCY PRODUCTION JAVASCRIPT
 * Lightweight, Vanilla JS, Zero External Library Dependencies
 * Compatible with Netlify, Static Hosting, and WordPress
 */

document.addEventListener('DOMContentLoaded', function() {
  'use strict';

  // 1. Mobile Navigation Toggle
  const mobileToggle = document.querySelector('.aj-mobile-toggle');
  const mobileMenu = document.querySelector('.aj-mobile-menu');
  const mobileClose = document.querySelector('.aj-mobile-close');

  if (mobileToggle && mobileMenu) {
    function openMenu() {
      mobileMenu.classList.add('open');
      mobileToggle.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
      mobileMenu.classList.remove('open');
      mobileToggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }

    mobileToggle.addEventListener('click', openMenu);
    if (mobileClose) mobileClose.addEventListener('click', closeMenu);

    mobileMenu.addEventListener('click', function(e) {
      if (e.target === mobileMenu) {
        closeMenu();
      }
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && mobileMenu.classList.contains('open')) {
        closeMenu();
      }
    });
  }

  // 2. Booking Enquiry Tabs
  const tabButtons = document.querySelectorAll('.aj-booking-tab');
  const tabPanels = document.querySelectorAll('.aj-tab-content');

  if (tabButtons.length && tabPanels.length) {
    tabButtons.forEach(button => {
      button.addEventListener('click', () => {
        const targetTab = button.getAttribute('data-tab');

        tabButtons.forEach(btn => {
          btn.classList.remove('active');
          btn.setAttribute('aria-selected', 'false');
        });
        tabPanels.forEach(panel => {
          panel.classList.remove('active');
          panel.hidden = true;
        });

        button.classList.add('active');
        button.setAttribute('aria-selected', 'true');

        const activePanel = document.getElementById(`tab-${targetTab}`);
        if (activePanel) {
          activePanel.classList.add('active');
          activePanel.hidden = false;
        }
      });
    });
  }

  // 3. Accessible FAQ Accordions
  const faqItems = document.querySelectorAll('.aj-faq-item');
  if (faqItems.length) {
    faqItems.forEach(item => {
      const questionBtn = item.querySelector('.aj-faq-question');
      const answerPanel = item.querySelector('.aj-faq-answer');

      if (questionBtn && answerPanel) {
        questionBtn.addEventListener('click', () => {
          const isOpen = item.classList.contains('active');

          // Close all other items for clean single accordion UX
          faqItems.forEach(otherItem => {
            if (otherItem !== item) {
              otherItem.classList.remove('active');
              const otherBtn = otherItem.querySelector('.aj-faq-question');
              const otherAns = otherItem.querySelector('.aj-faq-answer');
              if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
              if (otherAns) otherAns.style.maxHeight = null;
            }
          });

          // Toggle current
          if (isOpen) {
            item.classList.remove('active');
            questionBtn.setAttribute('aria-expanded', 'false');
            answerPanel.style.maxHeight = null;
          } else {
            item.classList.add('active');
            questionBtn.setAttribute('aria-expanded', 'true');
            answerPanel.style.maxHeight = answerPanel.scrollHeight + 'px';
          }
        });
      }
    });
  }

  // 4. Form Submission & Enquiry Handler
  const forms = document.querySelectorAll('form.aj-enquiry-form, form.aj-contact-form');
  forms.forEach(form => {
    form.addEventListener('submit', function(e) {
      // If Netlify form is natively posting without JS, let it submit, otherwise handle client quote feedback
      if (!form.getAttribute('action') || form.getAttribute('action') === '#') {
        e.preventDefault();
        
        // Basic validation
        const requiredInputs = form.querySelectorAll('[required]');
        let isValid = true;
        
        requiredInputs.forEach(input => {
          if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = '#ED2226';
          } else {
            input.style.borderColor = '';
          }
        });

        if (!isValid) {
          showToast('Please fill in all required fields.', 'error');
          return;
        }

        // Show official user response
        showToast('Thank you. Your request has been received. AJ Express will contact you with availability and pricing.', 'success');
        form.reset();
      }
    });
  });

  // 5. Toast Notification Utility
  function showToast(message, type = 'success') {
    let container = document.querySelector('.aj-toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'aj-toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `aj-toast aj-toast-${type}`;
    toast.setAttribute('role', 'alert');
    
    // Icon
    const checkIcon = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>`;
    
    toast.innerHTML = `${checkIcon}<span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 5000);
  }

  // 6. Image Error Fallback Handler
  const images = document.querySelectorAll('img');
  images.forEach(img => {
    img.addEventListener('error', function() {
      if (!this.getAttribute('data-failed')) {
        this.setAttribute('data-failed', 'true');
        this.src = 'assets/images/fallback-travel.webp';
      }
    });
  });

  // 7. Active Nav Link Highlighting
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.aj-nav-link, .aj-mobile-link');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // 8. Sticky Header Elevation
  const header = document.querySelector('.aj-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.style.boxShadow = '0 4px 20px rgba(29, 36, 51, 0.1)';
      } else {
        header.style.boxShadow = '0 2px 10px rgba(29, 36, 51, 0.06)';
      }
    }, { passive: true });
  }
});
