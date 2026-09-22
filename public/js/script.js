/**
 * RADHIKA BAROT — PREMIUM PORTFOLIO JAVASCRIPT
 * Code • Digital Marketing • Video Editing • AI/GenAI
 */

// 1. Form Endpoint Configuration
// Leave empty for demonstration / front-end success redirect flow.
// When an actual backend endpoint is ready, set the URL here.
const FORM_ENDPOINT = "";

// 2. DOM Ready Initialization
document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initPreloader();
  initScrollProgress();
  initCustomCursor();
  initNavigation();
  initHeroVideo();
  initProjectCardSkeletons();
  initProjectModal();
  initTestimonialsFilter();
  initContactForm();
  initBackToTop();
  initCardIntersectionObserver();
  initScrollReveal();
});

/* ==================================================
   PRELOADER
   ================================================== */
function initPreloader() {
  const preloader = document.getElementById('preloader');
  if (!preloader) return;

  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (isReducedMotion) {
    preloader.classList.add('preloader-hidden');
    setTimeout(() => preloader.remove(), 200);
    return;
  }

  const bar = document.querySelector('.preloader-bar');
  const tagCode = document.getElementById('preload-tag-code');
  const tagMarket = document.getElementById('preload-tag-market');
  const tagCreate = document.getElementById('preload-tag-create');

  if (bar) bar.style.width = '30%';

  setTimeout(() => {
    if (tagCode) tagCode.classList.add('active');
    if (bar) bar.style.width = '65%';
  }, 350);

  setTimeout(() => {
    if (tagMarket) tagMarket.classList.add('active');
    if (bar) bar.style.width = '85%';
  }, 700);

  setTimeout(() => {
    if (tagCreate) tagCreate.classList.add('active');
    if (bar) bar.style.width = '100%';
  }, 1050);

  setTimeout(() => {
    preloader.classList.add('preloader-hidden');
    setTimeout(() => preloader.remove(), 650);
  }, 1450);
}

/* ==================================================
   SCROLL PROGRESS BAR
   ================================================== */
function initScrollProgress() {
  const progressBar = document.getElementById('scroll-progress');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (totalHeight <= 0) return;
    const progress = (window.scrollY / totalHeight) * 100;
    progressBar.style.width = `${Math.min(100, Math.max(0, progress))}%`;
  }, { passive: true });
}

/* ==================================================
   CUSTOM CURSOR (DESKTOP)
   ================================================== */
function initCustomCursor() {
  if (window.matchMedia('(hover: none) and (pointer: coarse)').matches) return;

  const dot = document.querySelector('.custom-cursor-dot');
  const circle = document.querySelector('.custom-cursor-circle');
  if (!dot || !circle) return;

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let circleX = mouseX;
  let circleY = mouseY;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.transform = `translate(${mouseX}px, ${mouseY}px)`;
  });

  function animateCircle() {
    circleX += (mouseX - circleX) * 0.18;
    circleY += (mouseY - circleY) * 0.18;
    circle.style.transform = `translate(${circleX}px, ${circleY}px)`;
    requestAnimationFrame(animateCircle);
  }
  requestAnimationFrame(animateCircle);

  // Hover states
  const interactives = document.querySelectorAll('a, button, .btn, .pill, .skill-pill, .focus-card, .expertise-card, .project-card, .why-card');
  interactives.forEach((el) => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
  });

  const videoTargets = document.querySelectorAll('.hero-video-card, .reel-card');
  videoTargets.forEach((el) => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-video'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-video'));
  });
}

/* ==================================================
   NAVIGATION & MOBILE MENU
   ================================================== */
function initNavigation() {
  const navbar = document.getElementById('navbar');
  const hamburger = document.getElementById('hamburger-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const navLinks = document.querySelectorAll('.nav-link, .mobile-menu-link');

  // Scroll effect
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('nav-scrolled');
    } else {
      navbar.classList.remove('nav-scrolled');
    }
  }, { passive: true });

  // Mobile menu toggle
  if (hamburger && mobileMenu) {
    const toggleMenu = () => {
      const isOpen = hamburger.classList.toggle('open');
      mobileMenu.classList.toggle('open');
      document.body.classList.toggle('scroll-locked', isOpen);
    };

    hamburger.addEventListener('click', toggleMenu);

    navLinks.forEach((link) => {
      link.addEventListener('click', () => {
        if (mobileMenu.classList.contains('open')) {
          toggleMenu();
        }
      });
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileMenu.classList.contains('open')) {
        toggleMenu();
      }
    });
  }

  // Active section indicator using IntersectionObserver
  const sections = document.querySelectorAll('section[id]');
  if ('IntersectionObserver' in window && sections.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinks.forEach((link) => {
            const href = link.getAttribute('href');
            if (href === `#${id}`) {
              link.classList.add('active');
            } else if (href && href.startsWith('#')) {
              link.classList.remove('active');
            }
          });
        }
      });
    }, { threshold: 0.3 });

    sections.forEach((sec) => observer.observe(sec));
  }
}

/* ==================================================
   HERO VIDEO CONTROLS
   ================================================== */
function initHeroVideo() {
  const video = document.getElementById('hero-video');
  const soundBtn = document.getElementById('hero-video-sound-toggle');
  const playBtn = document.getElementById('hero-video-play-toggle');

  if (!video) return;

  // Sound Toggle
  if (soundBtn) {
    soundBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      video.muted = !video.muted;
      if (video.muted) {
        soundBtn.innerHTML = '<span>UNMUTE ↗</span>';
      } else {
        soundBtn.innerHTML = '<span>MUTE ✕</span>';
      }
    });
  }

  // Play / Pause Toggle
  if (playBtn) {
    playBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (video.paused) {
        video.play();
        playBtn.innerHTML = '<span>PAUSE ⏸</span>';
      } else {
        video.pause();
        playBtn.innerHTML = '<span>PLAY ▶</span>';
      }
    });
  }

  // Clicking the video container plays/pauses
  const card = document.querySelector('.hero-video-card');
  if (card) {
    card.addEventListener('click', () => {
      if (video.paused) {
        video.play();
        if (playBtn) playBtn.innerHTML = '<span>PAUSE ⏸</span>';
      } else {
        video.pause();
        if (playBtn) playBtn.innerHTML = '<span>PLAY ▶</span>';
      }
    });
  }
}

/* ==================================================
   PROJECT DETAIL MODAL & DATA
   ================================================== */
const PROJECTS_DATA = {
  'p1': {
    number: '01',
    category: 'Web Development',
    title: 'E-Commerce Website',
    techStack: ['HTML', 'CSS', 'Responsive Layouts', 'UI/UX'],
    description: 'A responsive e-commerce interface focused on product presentation, intuitive navigation, and a clean shopping experience. Features modular product cards, price filters, category switching, and a structured checkout preview design.',
    outcome: 'Created a structured front-end shopping experience with responsive layouts and clear product-focused navigation.',
    image: 'assets/images/project-ecommerce.jpg',
    role: 'Front-End UI Design & Architecture'
  },
  'p2': {
    number: '02',
    category: 'Web Development',
    title: 'Airline Booking System',
    techStack: ['PHP', 'MySQL', 'Web Architecture', 'HTML/CSS'],
    description: 'A booking-oriented web project designed around airline flight schedules, passenger itineraries, and reservation-related workflows. Implements origin-destination search parameters, flight availability reviews, and ticket confirmation states.',
    outcome: 'Built a functional project structure around booking interactions and user-facing reservation information.',
    image: 'assets/images/project-airline.jpg',
    role: 'Full-Stack Development & Workflow Design'
  },
  'p3': {
    number: '03',
    category: 'Web Application',
    title: 'Gym Management System',
    techStack: ['Laravel', 'PHP', 'MySQL', 'Blade', 'Role Management'],
    description: 'A management-focused web application concept designed to organize gym-related operations and member data. Organizes membership tiers, check-in schedules, trainer bookings, and renewal alerts in a unified administrative dashboard.',
    outcome: 'Created a structured application workflow using Laravel for practical fitness facility management functionality.',
    image: 'assets/images/project-gym.jpg',
    role: 'Backend Engineering & CRUD Architecture'
  },
  'p4': {
    number: '04',
    category: 'Automation / API',
    title: 'Social Media Auto Posting',
    techStack: ['Django', 'Python', 'APIs', 'Celery/Queue Logic'],
    description: 'A Django-based social media project exploring automated content publishing and scheduling workflows. Incorporates API integration logic to organize queued posts, format media payloads, and trigger scheduled distribution across digital channels.',
    outcome: 'Implemented an API-driven workflow for connecting social media publishing with scheduling and content management.',
    image: 'assets/images/project-socialhub.jpg',
    role: 'API Integration & Scheduling Pipeline'
  },
  'p5': {
    number: '05',
    category: 'AI / Android',
    title: 'Aicruit',
    techStack: ['Kotlin', 'Firebase', 'AI / GenAI', 'Android SDK'],
    description: 'An AI-focused job matching application concept designed to help users analyze resumes, identify relevant skills, and organize job opportunities. Combines resume parsing workflows, skill-gap analysis, and tailored career discovery.',
    outcome: 'Created an AI-oriented workflow combining resume analysis, skill extraction, job tracking and interview preparation features.',
    image: 'assets/images/project-aicruit.jpg',
    role: 'Android App Concept & AI Logic Design'
  }
};

/* ==================================================
   PROJECT CARD SKELETON LOADING
   ================================================== */
function initProjectCardSkeletons() {
  const wrappers = document.querySelectorAll('.project-visual-wrapper');
  wrappers.forEach((wrapper) => {
    const img = wrapper.querySelector('.project-img');
    if (!img) return;

    const setLoaded = () => {
      wrapper.classList.add('image-loaded');
    };

    if (img.complete && img.naturalHeight !== 0) {
      setLoaded();
    } else {
      img.addEventListener('load', setLoaded);
      img.addEventListener('error', setLoaded);
    }
  });
}

function initProjectModal() {
  const modal = document.getElementById('project-modal');
  const closeBtn = document.getElementById('modal-close-btn');
  if (!modal) return;

  const modalContainer = modal.querySelector('.modal-container');
  const modalImg = document.getElementById('modal-img');
  const modalCategory = document.getElementById('modal-category');
  const modalTitle = document.getElementById('modal-title');
  const modalDesc = document.getElementById('modal-desc');
  const modalTech = document.getElementById('modal-tech');
  const modalOutcome = document.getElementById('modal-outcome');
  const modalRole = document.getElementById('modal-role');

  const openModal = (projectId) => {
    const data = PROJECTS_DATA[projectId];
    if (!data) return;

    // Activate skeleton loading state on modal
    if (modalContainer) {
      modalContainer.classList.remove('is-loaded');
      modalContainer.classList.add('is-loading');
    }

    modal.classList.add('active');
    document.body.classList.add('scroll-locked');

    if (modalImg) {
      modalImg.src = data.image;
      modalImg.alt = `${data.title} Case Study Preview`;
    }
    if (modalCategory) modalCategory.textContent = `${data.number} // ${data.category}`;
    if (modalTitle) modalTitle.textContent = data.title;
    if (modalDesc) modalDesc.textContent = data.description;
    if (modalOutcome) modalOutcome.textContent = data.outcome;
    if (modalRole) modalRole.textContent = data.role;

    if (modalTech) {
      modalTech.innerHTML = '';
      data.techStack.forEach((t) => {
        const span = document.createElement('span');
        span.className = 'pill';
        span.textContent = t;
        modalTech.appendChild(span);
      });
    }

    // Gracefully transition from skeleton to populated case study details
    const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const finishLoading = () => {
      if (modalContainer) {
        modalContainer.classList.remove('is-loading');
        modalContainer.classList.add('is-loaded');
      }
    };

    if (isReducedMotion) {
      finishLoading();
    } else {
      setTimeout(finishLoading, 260);
    }
  };

  const closeModal = () => {
    modal.classList.remove('active');
    document.body.classList.remove('scroll-locked');
    if (modalContainer) {
      modalContainer.classList.remove('is-loading', 'is-loaded');
    }
  };

  // Triggers
  document.querySelectorAll('[data-project-id]').forEach((trigger) => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const id = trigger.getAttribute('data-project-id');
      openModal(id);
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });
}

/* ==================================================
   CONTACT FORM & META PIXEL WORKFLOW
   ================================================== */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const nameInput = document.getElementById('form-name');
  const emailInput = document.getElementById('form-email');
  const phoneInput = document.getElementById('form-phone');
  const serviceInput = document.getElementById('form-service');
  const messageInput = document.getElementById('form-message');
  const submitBtn = document.getElementById('form-submit-btn');

  // Modular validation rules
  const validators = {
    fullName: (value) => {
      const trimmed = (value || '').trim();
      if (!trimmed) {
        return 'Please enter your full name.';
      }
      if (trimmed.length < 2) {
        return 'Full name must be at least 2 characters long.';
      }
      if (!/[a-zA-Z\u00C0-\u024F\u1E00-\u1EFF]/.test(trimmed)) {
        return 'Please enter a valid name containing alphabetical letters.';
      }
      return null;
    },

    email: (value) => {
      const trimmed = (value || '').trim();
      if (!trimmed) {
        return 'Please enter your email address.';
      }
      // Strict standard-compliant regex check for email format
      const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$/;
      if (!emailRegex.test(trimmed)) {
        return 'Please enter a valid email format (e.g., name@domain.com).';
      }
      return null;
    },

    phone: (value) => {
      const trimmed = (value || '').trim();
      if (!trimmed) {
        return 'Please enter your phone number.';
      }
      const digitsOnly = trimmed.replace(/\D/g, '');
      if (digitsOnly.length < 7) {
        return 'Phone number must contain at least 7 digits.';
      }
      if (digitsOnly.length > 16) {
        return 'Please enter a valid phone number (up to 16 digits).';
      }
      const phoneRegex = /^[\+]?[(]?[0-9]{1,4}[)]?[-\s\.]?[0-9]{1,4}[-\s\.]?[0-9]{2,6}[-\s\.]?[0-9]{2,6}$/;
      if (!phoneRegex.test(trimmed) && !/^\+?[0-9\s\-()]{7,20}$/.test(trimmed)) {
        return 'Please enter a valid phone number format (e.g. +91 98765 43210).';
      }
      return null;
    },

    service: (value) => {
      if (!value || value.trim() === '') {
        return 'Please select a service interest from the list.';
      }
      return null;
    },

    message: (value) => {
      const trimmed = (value || '').trim();
      if (!trimmed) {
        return 'Please enter a message describing your project.';
      }
      if (trimmed.length < 10) {
        return `Message must be at least 10 characters long (${trimmed.length}/10 entered).`;
      }
      return null;
    }
  };

  const getValidatorForInput = (input) => {
    if (input === nameInput) return validators.fullName;
    if (input === emailInput) return validators.email;
    if (input === phoneInput) return validators.phone;
    if (input === serviceInput) return validators.service;
    if (input === messageInput) return validators.message;
    return null;
  };

  const setError = (input, message) => {
    const parent = input.closest('.form-group');
    if (!parent) return;
    parent.classList.add('has-error');
    parent.classList.remove('is-valid');
    input.setAttribute('aria-invalid', 'true');

    let errorMsg = parent.querySelector('.form-error-msg');
    if (!errorMsg) {
      errorMsg = document.createElement('div');
      errorMsg.className = 'form-error-msg';
      errorMsg.id = `${input.id}-error`;
      errorMsg.setAttribute('role', 'alert');
      errorMsg.setAttribute('aria-live', 'polite');
      parent.appendChild(errorMsg);
    }
    input.setAttribute('aria-describedby', errorMsg.id);

    errorMsg.innerHTML = `
      <span class="form-error-icon" aria-hidden="true">
        <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="12" y1="8" x2="12" y2="12"></line>
          <line x1="12" y1="16" x2="12.01" y2="16"></line>
        </svg>
      </span>
      <span>${message}</span>
    `;
  };

  const clearError = (input) => {
    const parent = input.closest('.form-group');
    if (!parent) return;
    parent.classList.remove('has-error');
    input.removeAttribute('aria-invalid');
    input.removeAttribute('aria-describedby');

    const errorMsg = parent.querySelector('.form-error-msg');
    if (errorMsg) {
      errorMsg.innerHTML = '';
    }

    if (input.value && input.value.trim().length > 0) {
      parent.classList.add('is-valid');
    } else {
      parent.classList.remove('is-valid');
    }
  };

  const validateInput = (input) => {
    const validator = getValidatorForInput(input);
    if (!validator) return true;
    const error = validator(input.value);
    if (error) {
      setError(input, error);
      return false;
    } else {
      clearError(input);
      return true;
    }
  };

  // Real-time inline validation on blur and input
  const allInputs = [nameInput, emailInput, phoneInput, serviceInput, messageInput].filter(Boolean);

  allInputs.forEach((input) => {
    // Validate on blur once user has interacted with the field
    input.addEventListener('blur', () => {
      input.dataset.touched = 'true';
      validateInput(input);
    });

    // Real-time re-validation while typing if field currently has an error or was touched
    input.addEventListener('input', () => {
      const parent = input.closest('.form-group');
      if (parent && (parent.classList.contains('has-error') || input.dataset.touched === 'true')) {
        validateInput(input);
      }
    });

    // Handle select dropdown changes immediately
    input.addEventListener('change', () => {
      input.dataset.touched = 'true';
      validateInput(input);
    });
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    let hasError = false;
    let firstInvalidInput = null;

    // Validate every required field and render inline errors
    allInputs.forEach((input) => {
      input.dataset.touched = 'true';
      const isValid = validateInput(input);
      if (!isValid) {
        hasError = true;
        if (!firstInvalidInput) {
          firstInvalidInput = input;
        }
        // Micro-interaction: trigger input shake on invalid fields
        input.classList.remove('input-shake');
        void input.offsetWidth; // force browser layout reflow
        input.classList.add('input-shake');
        setTimeout(() => input.classList.remove('input-shake'), 450);
      }
    });

    // If validation fails, focus the first problematic input and stop
    if (hasError) {
      if (firstInvalidInput) {
        firstInvalidInput.focus();
      }
      return;
    }

    const nameVal = nameInput ? nameInput.value.trim() : '';
    const emailVal = emailInput ? emailInput.value.trim() : '';
    const phoneVal = phoneInput ? phoneInput.value.trim() : '';
    const serviceVal = serviceInput ? serviceInput.value : '';
    const messageVal = messageInput ? messageInput.value.trim() : '';

    // Prepare payload
    const formData = {
      fullName: nameVal,
      email: emailVal,
      phone: phoneVal,
      service: serviceVal,
      message: messageVal,
      submittedAt: new Date().toISOString()
    };

    const originalBtnText = submitBtn.innerHTML;
    submitBtn.innerHTML = '<span>SENDING INQUIRY...</span>';
    submitBtn.disabled = true;

    try {
      if (FORM_ENDPOINT && FORM_ENDPOINT.trim() !== '') {
        const response = await fetch(FORM_ENDPOINT, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(formData)
        });

        if (!response.ok) {
          throw new Error('Form submission failed. Please try again.');
        }
      } else {
        // Front-end demonstration / preview mode: simulated network delay
        await new Promise((resolve) => setTimeout(resolve, 600));
      }

      // Track Meta Pixel Lead event if pixel is present
      if (typeof window.fbq === 'function') {
        try {
          window.fbq('track', 'Lead');
          console.log('[Meta Pixel] Lead event tracked successfully.');
        } catch (pixelErr) {
          console.warn('[Meta Pixel] Tracking failed:', pixelErr);
        }
      }

      // Set session flags for thank-you page personalization and Meta Pixel Lead tracking
      sessionStorage.setItem('radhikaLeadPending', 'true');
      const firstName = nameVal.trim().split(' ')[0] || '';
      if (firstName) {
        sessionStorage.setItem('radhikaLeadName', firstName);
      }

      // Reset form inputs and clear valid states
      form.reset();
      allInputs.forEach((input) => {
        delete input.dataset.touched;
        const parent = input.closest('.form-group');
        if (parent) {
          parent.classList.remove('is-valid', 'has-error');
        }
      });

      // Redirect directly to the existing thank-you.html page
      window.location.href = 'thank-you.html';
    } catch (err) {
      showToast({
        type: 'error',
        title: 'Submission Failed',
        message: err.message || 'An error occurred while submitting your message. Please try again or email directly.',
        linkText: 'Email Directly ↗',
        linkUrl: 'mailto:barotradhika8@gmail.com',
        meta: 'barotradhika8@gmail.com',
        duration: 6500
      });
      submitBtn.innerHTML = originalBtnText;
      submitBtn.disabled = false;
    }
  });
}

/* ==================================================
   TOAST NOTIFICATION ENGINE
   ================================================== */
function showToast({
  type = 'success',
  title = 'Inquiry Sent Successfully!',
  message = 'Thank you for reaching out. Your project inquiry has been received. Radhika will review your details and respond within 24–48 hours.',
  linkText = 'View Confirmation Page ↗',
  linkUrl = 'thank-you.html',
  meta = 'Direct Email: barotradhika8@gmail.com',
  duration = 7000
} = {}) {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    container.setAttribute('aria-live', 'polite');
    container.setAttribute('role', 'region');
    container.setAttribute('aria-label', 'Notifications');
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast-card toast-${type}`;
  toast.setAttribute('role', type === 'error' ? 'alert' : 'status');

  const iconSvg = type === 'error'
    ? `<svg class="toast-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="12" y1="8" x2="12" y2="12"></line>
        <line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>`
    : `<svg class="toast-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M20 6 9 17l-5-5"></path>
      </svg>`;

  const actionHtml = linkText && linkUrl
    ? `<div class="toast-actions">
        <a href="${linkUrl}" class="toast-action-link">${linkText}</a>
        ${meta ? `<span class="toast-separator">•</span><span class="toast-meta">${meta}</span>` : ''}
      </div>`
    : (meta ? `<div class="toast-actions"><span class="toast-meta">${meta}</span></div>` : '');

  toast.innerHTML = `
    <div class="toast-icon-wrapper">
      ${iconSvg}
    </div>
    <div class="toast-content">
      <div class="toast-header">
        <h4 class="toast-title">${title}</h4>
        <button type="button" class="toast-close-btn" aria-label="Dismiss notification">✕</button>
      </div>
      <p class="toast-message">${message}</p>
      ${actionHtml}
    </div>
    <div class="toast-progress-bar">
      <div class="toast-progress-fill" style="animation-duration: ${duration}ms;"></div>
    </div>
  `;

  container.appendChild(toast);

  let isPaused = false;
  let remainingTime = duration;
  let startTime = Date.now();
  let dismissTimer = null;

  const removeToast = () => {
    if (toast.classList.contains('toast-hiding')) return;
    toast.classList.add('toast-hiding');
    setTimeout(() => {
      if (toast.parentElement) {
        toast.parentElement.removeChild(toast);
      }
    }, 380);
  };

  const startTimer = (time) => {
    clearTimeout(dismissTimer);
    startTime = Date.now();
    dismissTimer = setTimeout(removeToast, time);
  };

  startTimer(duration);

  // Pause timer when hovered so user has ample time to read or click
  toast.addEventListener('mouseenter', () => {
    isPaused = true;
    clearTimeout(dismissTimer);
    remainingTime -= (Date.now() - startTime);
    const progressFill = toast.querySelector('.toast-progress-fill');
    if (progressFill) {
      progressFill.style.animationPlayState = 'paused';
    }
  });

  toast.addEventListener('mouseleave', () => {
    if (isPaused) {
      isPaused = false;
      const progressFill = toast.querySelector('.toast-progress-fill');
      if (progressFill) {
        progressFill.style.animationPlayState = 'running';
      }
      startTimer(Math.max(remainingTime, 1200));
    }
  });

  const closeBtn = toast.querySelector('.toast-close-btn');
  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      clearTimeout(dismissTimer);
      removeToast();
    });
  }

  return toast;
}

/* ==================================================
   BACK TO TOP
   ================================================== */
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 450) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ==================================================
   CARD INTERSECTION OBSERVERS (EXPERTISE & WORK)
   ================================================== */
function initCardIntersectionObserver() {
  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const expertiseCards = document.querySelectorAll('#expertise .expertise-card');
  const projectCards = document.querySelectorAll('#work .project-card');

  if (isReducedMotion || !('IntersectionObserver' in window)) {
    expertiseCards.forEach((card) => card.classList.add('card-revealed', 'revealed'));
    projectCards.forEach((card) => card.classList.add('card-revealed', 'revealed'));
    return;
  }

  // 1. Observer for Expertise Cards (staggered cascade)
  const expertiseObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('card-revealed', 'revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.15
  });

  expertiseCards.forEach((card) => {
    expertiseObserver.observe(card);
  });

  // 2. Observer for Work Section Cards (graceful fade and slide)
  const workObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('card-revealed', 'revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    rootMargin: '0px 0px -60px 0px',
    threshold: 0.12
  });

  projectCards.forEach((card) => {
    workObserver.observe(card);
  });
}

/* ==================================================
   SCROLL REVEAL (INTERSECTION OBSERVER)
   ================================================== */
function initScrollReveal() {
  const elements = document.querySelectorAll('.reveal-fade-up:not(.expertise-card):not(.project-card)');
  if (!('IntersectionObserver' in window)) {
    elements.forEach((el) => el.classList.add('revealed'));
    return;
  }

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    rootMargin: '0px 0px -40px 0px',
    threshold: 0.1
  });

  elements.forEach((el) => observer.observe(el));
}

/* ==================================================
   TESTIMONIALS CATEGORY FILTER
   ================================================== */
function initTestimonialsFilter() {
  const filterBtns = document.querySelectorAll('.t-filter-btn');
  const cards = document.querySelectorAll('.testimonial-card');
  if (!filterBtns.length || !cards.length) return;

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const selectedFilter = btn.getAttribute('data-filter');

      // Update button active state & aria attributes
      filterBtns.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      // Filter cards with smooth fade
      cards.forEach((card) => {
        const category = card.getAttribute('data-category');
        const shouldShow = selectedFilter === 'all' || category === selectedFilter;

        if (shouldShow) {
          card.classList.remove('hidden');
          // Trigger subtle entrance animation
          card.style.opacity = '0';
          card.style.transform = 'translateY(12px)';
          requestAnimationFrame(() => {
            card.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          });
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });
}

/* ==================================================
   GLOBAL THEME TOGGLE (LIGHT / DARK MODE)
   ================================================== */
function initThemeToggle() {
  const THEME_STORAGE_KEY = 'radhika-theme';
  const toggleBtns = document.querySelectorAll('.theme-toggle-btn');
  const root = document.documentElement;

  // Retrieve current active theme
  const getCurrentTheme = () => {
    return root.getAttribute('data-theme') || localStorage.getItem(THEME_STORAGE_KEY) || 'dark';
  };

  // Update button ARIA attributes and title tooltips
  const updateToggleUI = (theme) => {
    const isDark = theme === 'dark';
    const nextThemeLabel = isDark ? 'Switch to Light mode' : 'Switch to Dark mode';
    toggleBtns.forEach((btn) => {
      btn.setAttribute('aria-label', nextThemeLabel);
      btn.setAttribute('title', nextThemeLabel);
      btn.setAttribute('aria-pressed', isDark ? 'false' : 'true');

      const labelSpan = btn.querySelector('.mobile-theme-label');
      if (labelSpan) {
        labelSpan.textContent = isDark ? 'Light Mode' : 'Dark Mode';
      }
    });
  };

  // Apply theme with DOM attribute, localStorage, and meta tags
  const applyTheme = (theme, notify = false) => {
    root.setAttribute('data-theme', theme);
    try {
      localStorage.setItem(THEME_STORAGE_KEY, theme);
    } catch (e) {
      console.warn('[Theme] Failed writing to localStorage:', e);
    }
    updateToggleUI(theme);

    // Update mobile status bar theme-color
    let metaThemeColor = document.querySelector('meta[name="theme-color"]');
    if (!metaThemeColor) {
      metaThemeColor = document.createElement('meta');
      metaThemeColor.name = 'theme-color';
      document.head.appendChild(metaThemeColor);
    }
    metaThemeColor.content = theme === 'light' ? '#F7F8FA' : '#080808';

    // Optional user feedback toast
    if (notify && typeof showToast === 'function') {
      showToast({
        type: 'info',
        title: theme === 'light' ? 'Light Theme Active' : 'Dark Theme Active',
        message: `Switched display to ${theme === 'light' ? 'Light' : 'Dark'} mode. Preference saved.`,
        duration: 2500
      });
    }
  };

  // Ensure current UI state matches document theme
  const initialTheme = getCurrentTheme();
  updateToggleUI(initialTheme);

  // Attach click listener to all theme buttons
  toggleBtns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const current = getCurrentTheme();
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next, true);
    });
  });

  // System OS color scheme change listener (if user hasn't explicitly set preference)
  if (window.matchMedia) {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    mediaQuery.addEventListener('change', (e) => {
      if (!localStorage.getItem(THEME_STORAGE_KEY)) {
        applyTheme(e.matches ? 'dark' : 'light', false);
      }
    });
  }
}

