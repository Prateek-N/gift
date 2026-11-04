/**
 * Role Ready - Job Roles Knowledge Guide
 * Single Page Static Application
 * Vanilla JS, Zero External Runtime Dependencies, Runs Offline & On Any Web Server
 */

(function () {
  'use strict';

  // Application State
  const state = {
    data: null,
    currentRoute: 'home',
    selectedCategory: 'all',
    liveCallMode: false,
    theme: localStorage.getItem('role_ready_theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'),
    searchQuery: '',
    searchResults: [],
    selectedSearchIndex: 0,
    quizState: {
      active: false,
      mode: 'random-20',
      questions: [],
      currentIndex: 0,
      score: 0,
      answers: [],
      completed: false
    }
  };

  // SVG Icons helper
  const icons = {
    cpu: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>',
    'bar-chart-2': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    shield: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    cloud: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>',
    'git-merge': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 21V9a9 9 0 0 0 9 9"/></svg>',
    code: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    'message-square': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    'hard-hat': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 18a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v2z"/><path d="M10 10V5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5"/><path d="M4 15v-3a8 8 0 0 1 16 0v3"/></svg>',
    briefcase: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    settings: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    zap: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    activity: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
    'check-circle': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
    'trending-up': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
    target: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    layers: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    truck: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
    database: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
    copy: '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>',
    phone: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    print: '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>',
    chevronDown: '<svg class="cq-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>'
  };

  function getIcon(name) {
    return icons[name] || icons.cpu;
  }

  // Toast Notification helper
  function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="M20 6L9 17l-5-5"/>
      </svg>
      <span>${escapeHTML(message)}</span>
    `;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 2500);
  }

  // Safe clipboard helper
  function copyToClipboard(text, successMsg = 'Copied to clipboard!') {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        showToast(successMsg, 'success');
      }).catch(() => fallbackCopy(text, successMsg));
    } else {
      fallbackCopy(text, successMsg);
    }
  }

  function fallbackCopy(text, successMsg) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();
    try {
      document.execCommand('copy');
      showToast(successMsg, 'success');
    } catch (e) {
      showToast('Unable to copy', 'error');
    }
    document.body.removeChild(textarea);
  }

  function escapeHTML(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // Initialize App
  function initApp() {
    // 1. Theme setup
    applyTheme(state.theme);
    const themeBtn = document.getElementById('btn-toggle-theme');
    if (themeBtn) {
      themeBtn.addEventListener('click', toggleTheme);
    }

    // 2. Mobile drawer setup
    const mobileBtn = document.getElementById('btn-mobile-menu');
    const drawer = document.getElementById('mobile-nav-drawer');
    if (mobileBtn && drawer) {
      mobileBtn.addEventListener('click', () => {
        const isOpen = drawer.style.display !== 'none';
        drawer.style.display = isOpen ? 'none' : 'flex';
        mobileBtn.setAttribute('aria-expanded', !isOpen);
      });
      // Close drawer on any link click
      drawer.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
          drawer.style.display = 'none';
          mobileBtn.setAttribute('aria-expanded', 'false');
        });
      });
    }

    // 3. Search Modal Setup
    initSearchModal();

    // 4. Data Loading
    loadData().then(data => {
      state.data = data;
      // Setup routing
      window.addEventListener('hashchange', handleRoute);
      handleRoute();
    }).catch(err => {
      console.error('Failed to load role data:', err);
      const app = document.getElementById('app-content');
      if (app) {
        app.innerHTML = `
          <div style="padding: 3rem; text-align: center; color: var(--danger);">
            <h2>Unable to load knowledge guide data</h2>
            <p>Please ensure data/roles.json or data/roles-data.js is present.</p>
          </div>
        `;
      }
    });
  }

  // Load data supporting both window.ROLES_DATA (instant, zero CORS) or fetch
  async function loadData() {
    if (window.ROLES_DATA && window.ROLES_DATA.roles) {
      return window.ROLES_DATA;
    }
    const response = await fetch('data/roles.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  }

  // Theme Management
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('role_ready_theme', theme);
  }

  function toggleTheme() {
    applyTheme(state.theme === 'light' ? 'dark' : 'light');
  }

  // Route Handler
  function handleRoute() {
    const rawHash = window.location.hash.slice(1) || '/';
    const [pathPart, anchorPart] = rawHash.split('#');
    const path = pathPart || '/';

    // Update active nav links
    document.querySelectorAll('.nav-link').forEach(link => {
      const routeAttr = link.getAttribute('data-route');
      let isActive = false;
      if (routeAttr === 'home' && (path === '/' || path === '/roles')) isActive = true;
      else if (routeAttr && path.startsWith('/' + routeAttr)) isActive = true;
      link.classList.toggle('active', isActive);
    });

    const appContent = document.getElementById('app-content');
    if (!appContent || !state.data) return;

    if (path === '/' || path === '/roles') {
      state.currentRoute = 'home';
      renderHomeView(appContent);
    } else if (path.startsWith('/role/')) {
      const roleId = path.split('/')[2];
      state.currentRoute = 'role';
      renderRoleDetailView(appContent, roleId, anchorPart);
    } else if (path === '/compare') {
      state.currentRoute = 'compare';
      renderCompareView(appContent);
    } else if (path === '/glossary') {
      state.currentRoute = 'glossary';
      renderGlossaryView(appContent);
    } else if (path === '/market-basics') {
      state.currentRoute = 'market-basics';
      renderMarketBasicsView(appContent);
    } else if (path === '/call-scripts') {
      state.currentRoute = 'call-scripts';
      renderCallScriptsView(appContent);
    } else if (path === '/quiz') {
      state.currentRoute = 'quiz';
      renderQuizView(appContent);
    } else {
      state.currentRoute = 'home';
      renderHomeView(appContent);
    }

    // Scroll to top or anchor
    if (anchorPart) {
      setTimeout(() => {
        const el = document.getElementById(anchorPart);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    } else {
      window.scrollTo(0, 0);
    }
  }

  // ==========================================================================
  // VIEW: Home Page (FR-1)
  // ==========================================================================
  function renderHomeView(container) {
    const { roles, categories } = state.data;

    // Filter roles
    const filteredRoles = state.selectedCategory === 'all'
      ? roles
      : roles.filter(r => {
        const catObj = categories.find(c => c.id === state.selectedCategory);
        return catObj && r.category === catObj.name;
      });

    let html = `
      <section class="home-hero">
        <div class="hero-badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
          </svg>
          Sales Enablement Guide • US & Canada Market
        </div>
        <h1 class="hero-title">Job Roles Knowledge Guide</h1>
        <p class="hero-desc">
          Instant 30-second pitches, day-to-day responsibilities, key terminology, toolkits, and approved candidate cross-question answers for all 17 supported job profiles.
        </p>

        <!-- Live Call Alert Banner -->
        <div class="live-call-banner">
          <div class="live-call-content">
            <div class="call-pulse-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
            </div>
            <div class="live-call-text">
              <h3>On a live call with a candidate right now?</h3>
              <p>Search any keyword with <kbd class="kbd-shortcut">/</kbd>, click a role below, or review our compliance scripts.</p>
            </div>
          </div>
          <div class="live-call-actions">
            <a href="#/call-scripts" class="btn-danger-pill">
              Call Scripts & Guardrails
            </a>
            <a href="#/compare" class="btn-outline">
              Compare Roles
            </a>
          </div>
        </div>

        <!-- Category Filters -->
        <div class="category-filter-bar" role="tablist">
          <button type="button" class="filter-tab ${state.selectedCategory === 'all' ? 'active' : ''}" data-cat="all">
            All Roles <span class="badge">17</span>
          </button>
          <button type="button" class="filter-tab ${state.selectedCategory === 'tech-ai' ? 'active' : ''}" data-cat="tech-ai">
            Tech & AI <span class="badge">7</span>
          </button>
          <button type="button" class="filter-tab ${state.selectedCategory === 'engineering' ? 'active' : ''}" data-cat="engineering">
            Engineering & Construction <span class="badge">6</span>
          </button>
          <button type="button" class="filter-tab ${state.selectedCategory === 'business' ? 'active' : ''}" data-cat="business">
            Business & Marketing <span class="badge">4</span>
          </button>
        </div>
      </section>

      <!-- Roles Grid Grouped by Category -->
    `;

    // Group roles by categories
    categories.forEach(cat => {
      const catRoles = filteredRoles.filter(r => r.category === cat.name);
      if (catRoles.length === 0) return;

      html += `
        <section class="category-section" id="cat-${cat.id}">
          <div class="category-header">
            <div class="category-title">
              <span class="cat-indicator ${cat.id}"></span>
              <h2>${cat.name}</h2>
            </div>
            <span style="font-size: 0.85rem; color: var(--text-subtle);">${catRoles.length} roles</span>
          </div>
          <div class="role-grid">
            ${catRoles.map(role => renderRoleCard(role)).join('')}
          </div>
        </section>
      `;
    });

    container.innerHTML = html;

    // Attach category filter event listeners
    container.querySelectorAll('.filter-tab').forEach(tab => {
      tab.addEventListener('click', (e) => {
        state.selectedCategory = tab.getAttribute('data-cat');
        renderHomeView(container);
      });
    });

    // Attach copy pitch button events
    container.querySelectorAll('.btn-copy-card-pitch').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const pitchText = btn.getAttribute('data-pitch');
        copyToClipboard(pitchText, 'Quick Pitch copied!');
      });
    });
  }

  function renderRoleCard(role) {
    const topAlt = role.altTitles.slice(0, 3);
    return `
      <article class="role-card" data-category="${escapeHTML(role.category)}">
        <div class="role-card-header">
          <div class="role-card-icon">
            ${getIcon(role.icon)}
          </div>
          <div class="role-card-title-wrap">
            <h3 class="role-card-title">
              <a href="#/role/${role.id}">${escapeHTML(role.name)}</a>
            </h3>
            <span class="role-card-category-tag">${escapeHTML(role.category)}</span>
          </div>
        </div>

        <p class="role-card-oneliner">${escapeHTML(role.oneLiner)}</p>

        <div class="role-card-pitch-snippet">
          "${escapeHTML(role.quickPitch.slice(0, 115))}..."
        </div>

        <div class="role-card-meta">
          <div class="role-card-alt-chips" title="Common alternate titles">
            ${topAlt.map(t => `<span class="chip-sm">${escapeHTML(t)}</span>`).join('')}
          </div>
          <div style="display: flex; gap: 0.35rem;">
            <button type="button" class="btn-toolbar btn-copy-card-pitch" data-pitch="${escapeHTML(role.quickPitch)}" title="Copy 30-sec pitch">
              ${icons.copy}
            </button>
            <a href="#/role/${role.id}" class="btn-open-role">
              View Guide →
            </a>
          </div>
        </div>
      </article>
    `;
  }

  // ==========================================================================
  // VIEW: Role Detail Page (Standard 13-Point PRD Template, FR-2, FR-3, FR-6)
  // ==========================================================================
  function renderRoleDetailView(container, roleId, anchorPart) {
    const role = state.data.roles.find(r => r.id === roleId);
    if (!role) {
      container.innerHTML = `
        <div style="padding: 4rem 1rem; text-align: center;">
          <h2>Role Not Found</h2>
          <p>The role ID "${escapeHTML(roleId)}" does not exist in our guide.</p>
          <a href="#/" class="btn-primary" style="margin-top: 1rem;">Back to Directory</a>
        </div>
      `;
      return;
    }

    // Toggle live call mode class on body if active
    if (state.liveCallMode) {
      document.body.classList.add('live-call-mode');
    } else {
      document.body.classList.remove('live-call-mode');
    }

    const html = `
      <div class="role-detail-layout">
        <!-- Sticky Table of Contents (FR-6) -->
        <aside class="toc-sidebar" aria-label="Table of Contents">
          <div class="toc-title">On this page</div>
          <ul class="toc-list" id="toc-list">
            <li><a href="#/role/${role.id}#sec-pitch" class="toc-link active">1. Quick Pitch (30s)</a></li>
            <li><a href="#/role/${role.id}#sec-day-to-day" class="toc-link">2. Day-to-Day Tasks</a></li>
            <li><a href="#/role/${role.id}#sec-examples" class="toc-link">3. Real-World Examples (2)</a></li>
            <li><a href="#/role/${role.id}#sec-alt-titles" class="toc-link">4. Alternate Titles</a></li>
            <li><a href="#/role/${role.id}#sec-key-terms" class="toc-link">5. Key Terms (${role.keyTerms.length})</a></li>
            <li><a href="#/role/${role.id}#sec-tools" class="toc-link">6. Tools & Tech</a></li>
            <li><a href="#/role/${role.id}#sec-certs" class="toc-link">7. Certifications</a></li>
            <li><a href="#/role/${role.id}#sec-roadmap" class="toc-link">8. Skills Roadmap</a></li>
            <li><a href="#/role/${role.id}#sec-background" class="toc-link">9. Education & BG</a></li>
            <li><a href="#/role/${role.id}#sec-industries" class="toc-link">10. Target Industries</a></li>
            <li><a href="#/role/${role.id}#sec-resume" class="toc-link">11. Resume Keywords</a></li>
            <li><a href="#/role/${role.id}#sec-cross-questions" class="toc-link">12. Cross-Questions (${role.crossQuestions.length})</a></li>
            <li><a href="#/role/${role.id}#sec-related" class="toc-link">13. Related Roles</a></li>
            <li><a href="#/role/${role.id}#sec-salary" class="toc-link">14. Sourced Salary Data</a></li>
          </ul>
        </aside>

        <!-- Role Main Content Body -->
        <div class="role-main-content">
          <!-- Role Header Card -->
          <div class="role-header-card">
            <nav class="breadcrumbs" aria-label="Breadcrumb">
              <a href="#/">Roles Directory</a>
              <span>/</span>
              <span>${escapeHTML(role.category)}</span>
              <span>/</span>
              <span style="color: var(--text-main); font-weight: 600;">${escapeHTML(role.name)}</span>
            </nav>

            <div class="role-title-row">
              <div class="role-title-left">
                <div class="role-avatar-icon">
                  ${getIcon(role.icon)}
                </div>
                <div>
                  <h1 class="role-heading">${escapeHTML(role.name)}</h1>
                  <span class="role-card-category-tag">${escapeHTML(role.category)}</span>
                </div>
              </div>

              <!-- Header Toolbar (FR-10, FR-11) -->
              <div class="role-toolbar">
                <button type="button" class="btn-toolbar btn-live-call-mode ${state.liveCallMode ? 'active' : ''}" id="btn-toggle-call-mode" title="Hides background sections for fast scanning during a call">
                  ${icons.phone}
                  <span>${state.liveCallMode ? 'Exit Live Call Mode' : 'Live Call Mode'}</span>
                </button>
                <button type="button" class="btn-toolbar" id="btn-print-role" title="Print this complete role guide (FR-11)">
                  ${icons.print}
                  <span>Print Role</span>
                </button>
              </div>
            </div>
            <p style="font-size: 1rem; color: var(--text-muted); margin-top: 0.5rem;">
              ${escapeHTML(role.oneLiner)}
            </p>
          </div>

          <!-- 1. Quick Pitch (30-second explanation) (FR-3, FR-14) -->
          <section class="quick-pitch-box" id="sec-pitch" aria-labelledby="heading-pitch">
            <div class="pitch-header">
              <span class="pitch-label" id="heading-pitch">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
                </svg>
                1. 30-Second Quick Pitch (Read to Candidate)
              </span>
              <button type="button" class="btn-copy-pitch" id="btn-copy-main-pitch" data-pitch="${escapeHTML(role.quickPitch)}">
                ${icons.copy}
                <span>Copy Pitch</span>
              </button>
            </div>
            <p class="quick-pitch-text">
              ${escapeHTML(role.quickPitch)}
            </p>
          </section>

          <!-- 2. What they do day-to-day -->
          <section class="detail-section" id="sec-day-to-day">
            <h2 class="section-heading">2. What They Do Day-to-Day</h2>
            <ul class="day-to-day-list">
              ${role.dayToDay.map(item => `
                <li class="day-to-day-item">
                  <span class="bullet-icon">✓</span>
                  <span>${escapeHTML(item)}</span>
                </li>
              `).join('')}
            </ul>
          </section>

          <!-- 3. Real-World Project Examples (In Real Life) -->
          <section class="detail-section" id="sec-examples">
            <h2 class="section-heading">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--primary);">
                <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
              </svg>
              <span>3. Real-World Project Examples (What They Do on the Job)</span>
            </h2>
            <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 1.25rem;">
              Detailed, practical walkthroughs designed to make explaining this role effortless on calls with candidates or stakeholders:
            </p>
            <div class="real-world-examples-grid">
              ${(role.realWorldExamples || []).map((ex, idx) => {
                const stepList = ex.stepByStep && ex.stepByStep.length ? ex.stepByStep : [ex.whatTheyDo];
                const fullText = `ROLE: ${role.name}\nPROJECT: ${ex.title} (${ex.industry})\n\nHOW TO EXPLAIN IT (SIMPLE ANALOGY):\n"${ex.simpleAnalogy || ''}"\n\nTHE REAL-WORLD PROBLEM:\n${ex.scenario}\n\nWHAT THEY DO DAY-TO-DAY:\n${stepList.map((s, i) => `${i + 1}. ${s}`).join('\n')}\n\nTECH STACK & TOOLS:\n${ex.toolsUsed || ''}\n\nMEASURABLE BUSINESS IMPACT:\n${ex.impact}\n\nSALES CALL TALKING TIP:\n${ex.talkingTip || ''}`;
                const scriptText = `HOW TO EXPLAIN ${role.name.toUpperCase()} (EASY ANALOGY):\n"${ex.simpleAnalogy || ''}"\n\nPRO-TIP TO SAY ON CALLS:\n"${ex.talkingTip || ''}"`;
                return `
                <div class="example-card">
                  <div class="example-card-header">
                    <div class="example-card-meta">
                      <span class="example-number-badge">Example ${idx + 1}</span>
                      <span class="example-industry-tag">${escapeHTML(ex.industry)}</span>
                    </div>
                    <div class="example-header-actions">
                      <button type="button" class="btn-copy-pitch-tip" data-pitch="${escapeHTML(scriptText)}" title="Copy quick analogy & talking tip for phone call">
                        ${icons.copy}
                        <span>Copy Rep Script</span>
                      </button>
                      <button type="button" class="btn-copy-example" data-example="${escapeHTML(fullText)}" title="Copy complete detailed project walkthrough">
                        ${icons.copy}
                        <span>Copy Full Story</span>
                      </button>
                    </div>
                  </div>

                  <h3 class="example-title">${escapeHTML(ex.title)}</h3>

                  <!-- Plain-English Analogy (Makes explanation effortless) -->
                  ${ex.simpleAnalogy ? `
                    <div class="example-analogy-box">
                      <div class="example-analogy-header">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                        </svg>
                        <span>How to Explain It Easily (Everyday Analogy):</span>
                      </div>
                      <p class="example-analogy-text">"${escapeHTML(ex.simpleAnalogy)}"</p>
                    </div>
                  ` : ''}

                  <div class="example-body">
                    <!-- Real-Life Business Context -->
                    <div class="example-scenario-block">
                      <span class="example-subheading">The Real-World Business Problem:</span>
                      <p>${escapeHTML(ex.scenario)}</p>
                    </div>

                    <!-- Step-by-Step What They Actually Do -->
                    <div class="example-action-block">
                      <span class="example-subheading">Step-by-Step: What This Person Actually Does on the Job:</span>
                      <ol class="example-steps-list">
                        ${stepList.map(step => `
                          <li><span>${escapeHTML(step)}</span></li>
                        `).join('')}
                      </ol>
                    </div>

                    <!-- Tools & Technologies Deployed -->
                    ${ex.toolsUsed ? `
                      <div class="example-tools-block">
                        <span class="example-subheading">Tech Stack & Tools Deployed:</span>
                        <div class="example-tools-pills">
                          ${ex.toolsUsed.split(',').map(t => `<span class="chip-sm">${escapeHTML(t.trim())}</span>`).join('')}
                        </div>
                      </div>
                    ` : ''}

                    <!-- Measurable Business Impact -->
                    <div class="example-impact-box">
                      <div class="example-impact-header">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                          <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
                          <polyline points="17 6 23 6 23 12"/>
                        </svg>
                        <span>Measurable Business Impact:</span>
                      </div>
                      <p class="example-impact-text">${escapeHTML(ex.impact)}</p>
                    </div>

                    <!-- Sales Rep Talking Tip -->
                    ${ex.talkingTip ? `
                      <div class="example-talking-tip-box">
                        <div class="example-talking-tip-header">
                          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
                          </svg>
                          <span>Sales Call Pro-Tip (Say this to sound like an industry insider):</span>
                        </div>
                        <p class="example-talking-tip-text">${escapeHTML(ex.talkingTip)}</p>
                      </div>
                    ` : ''}
                  </div>
                </div>
              `;
              }).join('')}
            </div>
          </section>

          <!-- 4. Common Job Titles / Alternate Names (FR-5) -->
          <section class="detail-section" id="sec-alt-titles">
            <h2 class="section-heading">4. Common Job Titles & Alternate Names</h2>
            <p style="font-size: 0.85rem; color: var(--text-subtle); margin-bottom: 0.75rem;">
              Candidates may introduce themselves with these titles. Searching any of these in Role Ready maps directly to this role:
            </p>
            <div class="alt-titles-wrap">
              ${role.altTitles.map(t => `<span class="alt-title-chip">${escapeHTML(t)}</span>`).join('')}
            </div>
          </section>

          <!-- 5. Key Terms to Know (8-10 terms with plain-English meaning) -->
          <section class="detail-section" id="sec-key-terms">
            <h2 class="section-heading">5. Key Technical Terms (Plain-English Definitions)</h2>
            <div class="terms-table-wrap">
              <table class="terms-table">
                <thead>
                  <tr>
                    <th style="width: 25%;">Term / Acronym</th>
                    <th>Plain-English Meaning (What it does in real life)</th>
                  </tr>
                </thead>
                <tbody>
                  ${role.keyTerms.map(kt => `
                    <tr>
                      <td class="term-name-cell">${escapeHTML(kt.term)}</td>
                      <td>${escapeHTML(kt.definition)}</td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </section>

          <!-- 6. Tools & Technologies -->
          <section class="detail-section" id="sec-tools">
            <h2 class="section-heading">6. Tools & Technologies</h2>
            <div class="tools-tags-wrap">
              ${role.toolsList.map(t => `<span class="tool-tag">${escapeHTML(t)}</span>`).join('')}
            </div>
          </section>

          <!-- 7. Popular Certifications -->
          <section class="detail-section" id="sec-certs">
            <h2 class="section-heading">7. Popular Industry Certifications</h2>
            <div class="certs-grid">
              ${role.certificationsList.map(cert => `
                <div class="cert-card">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--primary); flex-shrink: 0;">
                    <circle cx="12" cy="8" r="7"/>
                    <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>
                  </svg>
                  <span>${escapeHTML(cert)}</span>
                </div>
              `).join('')}
            </div>
          </section>

          <!-- 8. Skills Roadmap -->
          <section class="detail-section" id="sec-roadmap">
            <h2 class="section-heading">8. Skills Roadmap (Career Progression)</h2>
            <div class="roadmap-container">
              <div class="roadmap-stage-card stage-foundation">
                <span class="stage-badge">Stage 1: Foundation</span>
                <p class="roadmap-stage-desc">${escapeHTML(role.roadmap.foundation)}</p>
              </div>
              <div class="roadmap-stage-card stage-job-ready">
                <span class="stage-badge">Stage 2: Job-Ready (Entry/Mid)</span>
                <p class="roadmap-stage-desc">${escapeHTML(role.roadmap.jobReady)}</p>
              </div>
              <div class="roadmap-stage-card stage-advanced">
                <span class="stage-badge">Stage 3: Advanced (Senior)</span>
                <p class="roadmap-stage-desc">${escapeHTML(role.roadmap.advanced)}</p>
              </div>
            </div>
          </section>

          <!-- 9. Typical Background / Education -->
          <section class="detail-section" id="sec-background">
            <h2 class="section-heading">9. Typical Background & Degrees</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">
              ${escapeHTML(role.background)}
            </p>
          </section>

          <!-- 10. Target Industries That Hire -->
          <section class="detail-section" id="sec-industries">
            <h2 class="section-heading">10. Industries That Hire</h2>
            <div class="alt-titles-wrap">
              ${role.industries.map(ind => `<span class="tool-tag">${escapeHTML(ind)}</span>`).join('')}
            </div>
          </section>

          <!-- 11. What Employers Look For on a Resume -->
          <section class="detail-section" id="sec-resume">
            <h2 class="section-heading">11. What Employers Look for on a Resume</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">
              <strong>High-Priority Keywords & Proof Points:</strong> ${escapeHTML(role.resumeKeywordsSummary)}
            </p>
          </section>

          <!-- 12. Candidate Cross-Questions & Suggested Answers (FR-9) -->
          <section class="detail-section" id="sec-cross-questions">
            <h2 class="section-heading">12. Candidate Cross-Questions & Suggested Answers</h2>
            <p style="font-size: 0.85rem; color: var(--text-subtle); margin-bottom: 1rem;">
              Click any question to view and copy the approved response:
            </p>
            <div class="cq-list">
              ${role.crossQuestions.map((cq, i) => `
                <div class="cq-item ${i === 0 ? 'open' : ''}">
                  <button type="button" class="cq-question-btn" aria-expanded="${i === 0}">
                    <span>"${escapeHTML(cq.q)}"</span>
                    ${icons.chevronDown}
                  </button>
                  <div class="cq-answer-panel" style="display: ${i === 0 ? 'block' : 'none'};">
                    <p>${escapeHTML(cq.a)}</p>
                    <button type="button" class="btn-copy-answer" data-answer="${escapeHTML(cq.a)}">
                      Copy Script
                    </button>
                  </div>
                </div>
              `).join('')}
            </div>
          </section>

          <!-- 13. Related Roles -->
          <section class="detail-section" id="sec-related">
            <h2 class="section-heading">13. Related Roles & Cross-Paths</h2>
            <div class="related-roles-list">
              ${role.relatedRoles.map(relId => {
                const rel = state.data.roles.find(r => r.id === relId);
                return rel ? `<a href="#/role/${rel.id}" class="related-role-link">→ ${escapeHTML(rel.name)}</a>` : '';
              }).join('')}
              <a href="#/compare" class="related-role-link" style="color: var(--primary); font-weight: bold;">
                ⇄ Open Role Comparison Matrix
              </a>
            </div>
          </section>

          <!-- 14. Sourced Salary Data (FR-16) -->
          <section class="detail-section" id="sec-salary">
            <h2 class="section-heading">14. Market Salary Benchmarks (US & Canada)</h2>
            <div class="salary-grid">
              <div class="salary-card">
                <div class="salary-country-label">United States (Annual)</div>
                <div class="salary-value">${escapeHTML(role.salary.us || 'Pending verification')}</div>
                <div class="salary-meta">Source: ${escapeHTML(role.salary.source)} (as of ${escapeHTML(role.salary.asOf)})</div>
              </div>
              <div class="salary-card">
                <div class="salary-country-label">Canada (Annual)</div>
                <div class="salary-value">${escapeHTML(role.salary.ca || 'Pending verification')}</div>
                <div class="salary-meta">Source: ${escapeHTML(role.salary.source)} (as of ${escapeHTML(role.salary.asOf)})</div>
              </div>
            </div>
            <p style="font-size: 0.75rem; color: var(--text-subtle); margin-top: 0.75rem;">
              * Note: Salary figures are benchmark ranges for informational awareness only. Never quote fixed compensation guarantees to candidates.
            </p>
          </section>

          <!-- Compliance Guardrail Box (FR-15, Section 7.4) -->
          <div class="compliance-guardrail-box">
            <div class="guardrail-header">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
                <line x1="12" y1="9" x2="12" y2="13"/>
                <line x1="12" y1="17" x2="12.01" y2="17"/>
              </svg>
              <span>Sales Call Compliance Rules (Mandatory Guardrails)</span>
            </div>
            <ul class="guardrail-list">
              <li><strong>NEVER guarantee a job, interview count, salary, or visa outcome.</strong></li>
              <li><strong>NEVER give legal or immigration advice</strong> — refer candidates to official USCIS / IRCC links or licensed immigration counsel.</li>
              <li><strong>NEVER suggest misrepresenting experience, skills, dates, or visa status on a resume.</strong></li>
              <li>If you don't know an answer, say: <em>"That's a great, specific question — let me confirm with our technical specialist and get back to you today."</em> Never guess.</li>
            </ul>
          </div>
        </div>
      </div>
    `;

    container.innerHTML = html;

    // Attach Live Call Mode Toggle
    const btnCallMode = container.querySelector('#btn-toggle-call-mode');
    if (btnCallMode) {
      btnCallMode.addEventListener('click', () => {
        state.liveCallMode = !state.liveCallMode;
        if (state.liveCallMode) {
          document.body.classList.add('live-call-mode');
          btnCallMode.classList.add('active');
          btnCallMode.querySelector('span').textContent = 'Exit Live Call Mode';
          document.getElementById('header-call-badge').style.display = 'inline-flex';
          showToast('Live Call Mode active: Compact view focused on pitches, terms & scripts', 'info');
        } else {
          document.body.classList.remove('live-call-mode');
          btnCallMode.classList.remove('active');
          btnCallMode.querySelector('span').textContent = 'Live Call Mode';
          document.getElementById('header-call-badge').style.display = 'none';
        }
      });
    }

    // Attach Print Button (FR-11)
    const btnPrint = container.querySelector('#btn-print-role');
    if (btnPrint) {
      btnPrint.addEventListener('click', () => {
        window.print();
      });
    }

    // Attach Copy Main Pitch Button (FR-14)
    const btnCopyPitch = container.querySelector('#btn-copy-main-pitch');
    if (btnCopyPitch) {
      btnCopyPitch.addEventListener('click', () => {
        const text = btnCopyPitch.getAttribute('data-pitch');
        copyToClipboard(text, 'Quick Pitch copied to clipboard!');
      });
    }

    // Attach Copy Project Example Buttons
    container.querySelectorAll('.btn-copy-example').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const text = btn.getAttribute('data-example');
        copyToClipboard(text, 'Full Project Story copied to clipboard!');
      });
    });

    // Attach Copy Rep Script (Analogy + Talking Tip)
    container.querySelectorAll('.btn-copy-pitch-tip').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const text = btn.getAttribute('data-pitch');
        copyToClipboard(text, 'Rep Script & Analogy copied to clipboard!');
      });
    });

    // Attach Cross-Question Accordions (FR-9)
    container.querySelectorAll('.cq-item').forEach(item => {
      const qBtn = item.querySelector('.cq-question-btn');
      const panel = item.querySelector('.cq-answer-panel');
      const copyBtn = item.querySelector('.btn-copy-answer');

      qBtn.addEventListener('click', () => {
        const isOpen = item.classList.contains('open');
        item.classList.toggle('open', !isOpen);
        panel.style.display = isOpen ? 'none' : 'block';
        qBtn.setAttribute('aria-expanded', !isOpen);
      });

      if (copyBtn) {
        copyBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          const ans = copyBtn.getAttribute('data-answer');
          copyToClipboard(ans, 'Answer script copied!');
        });
      }
    });

    // In-page TOC Scrollspy (FR-6)
    initTocScrollSpy(container);
  }

  function initTocScrollSpy(container) {
    const tocLinks = container.querySelectorAll('.toc-link');
    const sections = container.querySelectorAll('.detail-section, .quick-pitch-box');
    if (!sections.length || !tocLinks.length) return;

    window.addEventListener('scroll', () => {
      let currentSectionId = '';
      sections.forEach(sec => {
        const top = sec.offsetTop - 120;
        if (window.scrollY >= top) {
          currentSectionId = sec.id;
        }
      });

      if (currentSectionId) {
        tocLinks.forEach(link => {
          const href = link.getAttribute('href');
          link.classList.toggle('active', href.endsWith('#' + currentSectionId));
        });
      }
    }, { passive: true });
  }

  // ==========================================================================
  // VIEW: Compare Roles Page (FR-7 & Section 7.1)
  // ==========================================================================
  function renderCompareView(container) {
    const { comparisons, roles } = state.data;

    let html = `
      <div class="compare-container">
        <div class="compare-hero">
          <h1 class="hero-title">Compare Commonly Confused Roles</h1>
          <p class="hero-desc">
            North American candidates frequently ask the difference between overlapping titles. Use these crisp one-line distinctions or select two roles to compare side-by-side.
          </p>
        </div>

        <!-- Interactive 2-Role Side-by-Side Comparator -->
        <div class="interactive-compare-box">
          <h2 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 1rem; text-align: center;">
            Interactive Role-to-Role Comparator
          </h2>
          <div class="comparator-selectors">
            <select id="compare-role-a" class="role-select-box" aria-label="Select first role to compare">
              ${roles.map((r, i) => `<option value="${r.id}" ${i === 0 ? 'selected' : ''}>${escapeHTML(r.name)}</option>`).join('')}
            </select>
            <span class="vs-badge">VS</span>
            <select id="compare-role-b" class="role-select-box" aria-label="Select second role to compare">
              ${roles.map((r, i) => `<option value="${r.id}" ${i === 1 ? 'selected' : ''}>${escapeHTML(r.name)}</option>`).join('')}
            </select>
          </div>

          <div id="side-by-side-result">
            <!-- Populated dynamically -->
          </div>
        </div>

        <!-- Pre-built Core Comparisons Table from PRD 7.1 -->
        <h2 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem;">
          Standard Industry Distinctions (11 Core Comparisons)
        </h2>
        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th style="width: 35%;">Commonly Confused Profiles</th>
                <th>One-Line Core Difference</th>
                <th style="width: 15%;">Quick Links</th>
              </tr>
            </thead>
            <tbody>
              ${comparisons.map(c => `
                <tr>
                  <td><strong>${escapeHTML(c.pair)}</strong></td>
                  <td>${escapeHTML(c.difference)}</td>
                  <td>
                    <div style="display: flex; gap: 0.5rem;">
                      <a href="#/role/${findRoleIdByName(c.roleA)}" style="font-size: 0.8rem; font-weight: 600;">View A</a>
                      ${c.roleB ? `<span>•</span> <a href="#/role/${findRoleIdByName(c.roleB)}" style="font-size: 0.8rem; font-weight: 600;">View B</a>` : ''}
                    </div>
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>
    `;

    container.innerHTML = html;

    const selectA = container.querySelector('#compare-role-a');
    const selectB = container.querySelector('#compare-role-b');

    function updateSideBySide() {
      const roleA = roles.find(r => r.id === selectA.value);
      const roleB = roles.find(r => r.id === selectB.value);
      const resContainer = container.querySelector('#side-by-side-result');
      if (!roleA || !roleB || !resContainer) return;

      resContainer.innerHTML = `
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 1rem;">
          <div style="background-color: var(--bg-subtle); padding: 1.25rem; border-radius: var(--radius-md);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--primary);">${escapeHTML(roleA.name)}</h3>
              <a href="#/role/${roleA.id}" style="font-size: 0.8rem; font-weight: 600;">Open Full Guide →</a>
            </div>
            <p style="font-size: 0.9rem; margin-bottom: 0.75rem;"><strong>30s Pitch:</strong> ${escapeHTML(roleA.quickPitch)}</p>
            <p style="font-size: 0.85rem; margin-bottom: 0.5rem;"><strong>Core Tools:</strong> ${escapeHTML(roleA.toolsSummary)}</p>
            <p style="font-size: 0.85rem;"><strong>Typical Salary (US):</strong> ${escapeHTML(roleA.salary.us)}</p>
          </div>

          <div style="background-color: var(--bg-subtle); padding: 1.25rem; border-radius: var(--radius-md);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
              <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--primary);">${escapeHTML(roleB.name)}</h3>
              <a href="#/role/${roleB.id}" style="font-size: 0.8rem; font-weight: 600;">Open Full Guide →</a>
            </div>
            <p style="font-size: 0.9rem; margin-bottom: 0.75rem;"><strong>30s Pitch:</strong> ${escapeHTML(roleB.quickPitch)}</p>
            <p style="font-size: 0.85rem; margin-bottom: 0.5rem;"><strong>Core Tools:</strong> ${escapeHTML(roleB.toolsSummary)}</p>
            <p style="font-size: 0.85rem;"><strong>Typical Salary (US):</strong> ${escapeHTML(roleB.salary.us)}</p>
          </div>
        </div>
      `;
    }

    selectA.addEventListener('change', updateSideBySide);
    selectB.addEventListener('change', updateSideBySide);
    updateSideBySide();
  }

  function findRoleIdByName(name) {
    if (!name) return 'ai-ml-engineer';
    const clean = name.toLowerCase().trim();
    const found = state.data.roles.find(r => r.name.toLowerCase().includes(clean) || clean.includes(r.name.toLowerCase()));
    return found ? found.id : 'ai-ml-engineer';
  }

  // ==========================================================================
  // VIEW: Glossary Page (FR-8 & Section 7.2)
  // ==========================================================================
  function renderGlossaryView(container) {
    const { glossary } = state.data;
    let selectedLetter = 'all';
    let searchQuery = '';

    function getFilteredGlossary() {
      return glossary.filter(item => {
        const matchesLetter = selectedLetter === 'all' || item.term.toUpperCase().startsWith(selectedLetter);
        const matchesSearch = !searchQuery || item.term.toLowerCase().includes(searchQuery.toLowerCase()) || item.definition.toLowerCase().includes(searchQuery.toLowerCase());
        return matchesLetter && matchesSearch;
      });
    }

    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

    container.innerHTML = `
      <div class="glossary-container">
        <div class="home-hero" style="padding-top: 1rem; padding-bottom: 1.5rem;">
          <h1 class="hero-title">A–Z Technical Terms Glossary</h1>
          <p class="hero-desc">
            All 167+ technical terms and acronyms across our 17 supported roles, explained in plain English for fast reference.
          </p>
        </div>

        <div class="glossary-search-bar">
          <input type="text" id="glossary-filter-input" class="glossary-input" placeholder="Search terms or definitions (e.g. RAG, CI/CD, P&ID, GAMP 5, CTR)..." autocomplete="off">
        </div>

        <!-- Alphabet Bar -->
        <div class="alphabet-bar" id="alphabet-bar">
          <button type="button" class="alphabet-letter-btn active" data-letter="all">All</button>
          ${alphabet.map(l => `<button type="button" class="alphabet-letter-btn" data-letter="${l}">${l}</button>`).join('')}
        </div>

        <!-- Terms Grid -->
        <div class="glossary-grid" id="glossary-grid">
          <!-- Populated dynamically -->
        </div>
      </div>
    `;

    const grid = container.querySelector('#glossary-grid');
    const input = container.querySelector('#glossary-filter-input');
    const alphaBtns = container.querySelectorAll('.alphabet-letter-btn');

    function renderTerms() {
      const items = getFilteredGlossary();
      if (items.length === 0) {
        grid.innerHTML = `
          <div style="grid-column: 1 / -1; padding: 3rem; text-align: center; color: var(--text-subtle);">
            <p style="font-size: 1.1rem;">No technical terms matched your filter.</p>
          </div>
        `;
        return;
      }

      grid.innerHTML = items.map(item => {
        let catClass = 'tech-ai';
        if (item.category && item.category.includes('Engineering')) catClass = 'engineering';
        else if (item.category && item.category.includes('Business')) catClass = 'business';

        return `
          <div class="glossary-term-card">
            <div class="glossary-term-header">
              <span class="glossary-term-title">${escapeHTML(item.term)}</span>
              <span class="glossary-term-cat-tag ${catClass}">${escapeHTML(item.category || '')}</span>
            </div>
            <p class="glossary-term-def">${escapeHTML(item.definition)}</p>
            <div class="glossary-term-roles">
              <span>Roles:</span>
              ${item.roles.map(rName => {
                const rObj = state.data.roles.find(r => r.name === rName);
                return rObj
                  ? `<a href="#/role/${rObj.id}" style="color: var(--primary); font-weight: 500;">${escapeHTML(rName)}</a>`
                  : `<span>${escapeHTML(rName)}</span>`;
              }).join(', ')}
            </div>
          </div>
        `;
      }).join('');
    }

    input.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim();
      renderTerms();
    });

    alphaBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        alphaBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedLetter = btn.getAttribute('data-letter');
        renderTerms();
      });
    });

    renderTerms();
  }

  // ==========================================================================
  // VIEW: US & Canada Job Market Basics (Section 7.3)
  // ==========================================================================
  function renderMarketBasicsView(container) {
    const { jobMarketBasics } = state.data;

    container.innerHTML = `
      <div class="market-basics-container">
        <div class="home-hero" style="padding-top: 1rem; padding-bottom: 2rem;">
          <h1 class="hero-title">US & Canada Job Market Basics</h1>
          <p class="hero-desc">
            Essential recruitment conventions, ATS parsing mechanisms, resume standards, employment tax classifications, and work authorization awareness for candidate conversations.
          </p>
        </div>

        <!-- 1. ATS (Applicant Tracking Systems) -->
        <div class="market-card">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            ${escapeHTML(jobMarketBasics.ats.title)}
          </h3>
          <p>${escapeHTML(jobMarketBasics.ats.summary)}</p>
          <ul class="market-points-list">
            ${jobMarketBasics.ats.keyPoints.map(p => `<li><span>•</span><span>${escapeHTML(p)}</span></li>`).join('')}
          </ul>
        </div>

        <!-- 2. US & Canada Resume Standards -->
        <div class="market-card">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            ${escapeHTML(jobMarketBasics.resumeNorms.title)}
          </h3>
          <p>${escapeHTML(jobMarketBasics.resumeNorms.summary)}</p>
          <ul class="market-points-list">
            ${jobMarketBasics.resumeNorms.keyPoints.map(p => `<li><span>•</span><span>${escapeHTML(p)}</span></li>`).join('')}
          </ul>
        </div>

        <!-- 3. LinkedIn Optimization -->
        <div class="market-card">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
            ${escapeHTML(jobMarketBasics.linkedin.title)}
          </h3>
          <p>${escapeHTML(jobMarketBasics.linkedin.summary)}</p>
          <ul class="market-points-list">
            ${jobMarketBasics.linkedin.keyPoints.map(p => `<li><span>•</span><span>${escapeHTML(p)}</span></li>`).join('')}
          </ul>
        </div>

        <!-- 4. Employment Types (US vs Canada) -->
        <div class="market-card">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            ${escapeHTML(jobMarketBasics.jobTypes.title)}
          </h3>
          <p>${escapeHTML(jobMarketBasics.jobTypes.summary)}</p>

          <h4 style="margin-top: 1rem; font-size: 1rem; color: var(--text-main);">United States Classifications:</h4>
          <div class="employment-types-grid">
            ${jobMarketBasics.jobTypes.usTypes.map(t => `
              <div class="emp-type-card">
                <div class="emp-type-title">${escapeHTML(t.type)}</div>
                <div class="emp-type-desc">${escapeHTML(t.detail)}</div>
              </div>
            `).join('')}
          </div>

          <h4 style="margin-top: 1.5rem; font-size: 1rem; color: var(--text-main);">Canada Classifications:</h4>
          <div class="employment-types-grid">
            ${jobMarketBasics.jobTypes.caTypes.map(t => `
              <div class="emp-type-card">
                <div class="emp-type-title">${escapeHTML(t.type)}</div>
                <div class="emp-type-desc">${escapeHTML(t.detail)}</div>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- 5. Six Hiring Stages -->
        <div class="market-card">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            Common 6-Stage North American Hiring Lifecycle
          </h3>
          <div class="hiring-stages-timeline">
            ${jobMarketBasics.hiringStages.map(s => `
              <div class="hiring-stage-row">
                <div class="stage-step-num">${escapeHTML(s.stage.split('.')[0])}</div>
                <div>
                  <strong>${escapeHTML(s.stage.split('.')[1] || s.stage)}</strong>
                  <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.2rem;">${escapeHTML(s.desc)}</p>
                </div>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- 6. Work Authorization Awareness -->
        <div class="market-card" style="border-left: 4px solid var(--primary);">
          <h3>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            ${escapeHTML(jobMarketBasics.workAuth.title)}
          </h3>
          <div style="background-color: var(--danger-bg); border: 1px solid var(--danger-border); padding: 0.75rem 1rem; border-radius: var(--radius-md); font-size: 0.85rem; color: var(--danger); font-weight: 600; margin-bottom: 1rem;">
            ${escapeHTML(jobMarketBasics.workAuth.disclaimer)}
          </div>

          <h4 style="font-size: 1rem; color: var(--text-main); margin-bottom: 0.5rem;">United States Statuses to Recognize:</h4>
          <div class="employment-types-grid" style="margin-bottom: 1.5rem;">
            ${jobMarketBasics.workAuth.usTerms.map(t => `
              <div class="emp-type-card">
                <div class="emp-type-title">${escapeHTML(t.code)} — ${escapeHTML(t.name)}</div>
                <div class="emp-type-desc">${escapeHTML(t.detail)}</div>
              </div>
            `).join('')}
          </div>

          <h4 style="font-size: 1rem; color: var(--text-main); margin-bottom: 0.5rem;">Canada Statuses to Recognize:</h4>
          <div class="employment-types-grid">
            ${jobMarketBasics.workAuth.caTerms.map(t => `
              <div class="emp-type-card">
                <div class="emp-type-title">${escapeHTML(t.code)} — ${escapeHTML(t.name)}</div>
                <div class="emp-type-desc">${escapeHTML(t.detail)}</div>
              </div>
            `).join('')}
          </div>

          <div style="margin-top: 1.5rem; font-size: 0.85rem; color: var(--text-subtle);">
            <strong>Official Government Resources:</strong>
            ${jobMarketBasics.workAuth.officialLinks.map(l => `
              <a href="${l.url}" target="_blank" rel="noopener noreferrer" style="margin-left: 0.75rem; color: var(--primary);">
                ${escapeHTML(l.name)} ↗
              </a>
            `).join('')}
          </div>
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // VIEW: Handling Cross-Questions & Call Scripts (Section 7.4)
  // ==========================================================================
  function renderCallScriptsView(container) {
    const { crossQuestionsGuide } = state.data;

    container.innerHTML = `
      <div class="scripts-container">
        <div class="home-hero" style="padding-top: 1rem; padding-bottom: 2rem;">
          <h1 class="hero-title">Handling Cross-Questions & Call Scripts</h1>
          <p class="hero-desc">
            4-step call technique, honest deferral scripts, mandatory compliance guardrails, and approved responses for tough candidate cross-questions.
          </p>
        </div>

        <!-- 4-Step Call Technique -->
        <h2 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 1rem;">The 4-Step Call Technique</h2>
        <div class="call-steps-grid">
          ${crossQuestionsGuide.techniqueSteps.map(step => `
            <div class="call-step-card">
              <div class="call-step-num">0${step.step}</div>
              <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 0.35rem;">${escapeHTML(step.title)}</h3>
              <p style="font-size: 0.875rem; color: var(--text-muted); line-height: 1.5;">${escapeHTML(step.desc)}</p>
            </div>
          `).join('')}
        </div>

        <!-- Deferral Script Callout Box -->
        <div class="script-highlight-box">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
            <strong style="color: var(--primary); text-transform: uppercase; font-size: 0.8rem; letter-spacing: 0.05em;">
              When You Don't Know the Answer (Honest Deferral Script)
            </strong>
            <button type="button" class="btn-copy-pitch" id="btn-copy-deferral">
              ${icons.copy}
              <span>Copy Script</span>
            </button>
          </div>
          <p class="script-highlight-quote" id="deferral-quote-text">
            "That is a great, specific question — let me confirm with our technical specialist and get back to you today."
          </p>
          <p style="font-size: 0.85rem; color: var(--text-muted);">
            Never guess or bluff technical specifications. Candidates respect honest domain specialization far more than incorrect guesses.
          </p>
        </div>

        <!-- Compliance Guardrails Box -->
        <div class="compliance-guardrail-box">
          <div class="guardrail-header">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"/>
              <line x1="12" y1="8" x2="12" y2="12"/>
              <line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
            <span>Absolute Compliance Guardrails (What Sales Reps Must NEVER Say)</span>
          </div>
          <ul class="guardrail-list" style="margin-top: 0.75rem;">
            ${crossQuestionsGuide.complianceGuardrails.mustNotSay.map(rule => `
              <li style="font-size: 0.95rem; font-weight: 500;">${escapeHTML(rule)}</li>
            `).join('')}
          </ul>
        </div>

        <!-- Common Objections & Approved Rep Responses -->
        <h2 style="font-size: 1.25rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem;">
          Approved Responses to Sensitive Candidate Cross-Questions
        </h2>
        <div class="cq-list">
          ${crossQuestionsGuide.complianceGuardrails.approvedResponses.map((item, idx) => `
            <div class="cq-item ${idx === 0 ? 'open' : ''}">
              <button type="button" class="cq-question-btn" aria-expanded="${idx === 0}">
                <span>Candidate asks: <strong>"${escapeHTML(item.candidateSays)}"</strong></span>
                ${icons.chevronDown}
              </button>
              <div class="cq-answer-panel" style="display: ${idx === 0 ? 'block' : 'none'};">
                <p><strong>Approved Response:</strong></p>
                <p style="margin-top: 0.35rem; font-style: italic;">"${escapeHTML(item.repResponse)}"</p>
                <button type="button" class="btn-copy-answer" data-answer="${escapeHTML(item.repResponse)}">
                  Copy Response
                </button>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;

    // Copy deferral script event
    const copyDeferral = container.querySelector('#btn-copy-deferral');
    if (copyDeferral) {
      copyDeferral.addEventListener('click', () => {
        const text = container.querySelector('#deferral-quote-text').innerText.trim();
        copyToClipboard(text, 'Deferral script copied!');
      });
    }

    // Accordions
    container.querySelectorAll('.cq-item').forEach(item => {
      const qBtn = item.querySelector('.cq-question-btn');
      const panel = item.querySelector('.cq-answer-panel');
      const copyBtn = item.querySelector('.btn-copy-answer');

      qBtn.addEventListener('click', () => {
        const isOpen = item.classList.contains('open');
        item.classList.toggle('open', !isOpen);
        panel.style.display = isOpen ? 'none' : 'block';
        qBtn.setAttribute('aria-expanded', !isOpen);
      });

      if (copyBtn) {
        copyBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          copyToClipboard(copyBtn.getAttribute('data-answer'), 'Approved response copied!');
        });
      }
    });
  }

  // ==========================================================================
  // VIEW: Self-Quiz Engine (FR-12 & Section 7.5)
  // ==========================================================================
  function renderQuizView(container) {
    const { roles } = state.data;
    const lastScore = localStorage.getItem('role_ready_last_quiz_score');

    if (!state.quizState.active) {
      // Quiz Setup Screen
      container.innerHTML = `
        <div class="quiz-container">
          <div class="quiz-setup-card">
            <h1 style="font-size: 1.85rem; font-weight: 800; margin-bottom: 0.75rem;">
              Sales Rep Knowledge Self-Quiz
            </h1>
            <p style="color: var(--text-muted); max-width: 550px; margin: 0 auto 1.5rem;">
              Test your understanding of role definitions, key terminology, tools, and objection handling. Passing target is ≥ 80% per company onboarding standards.
            </p>

            ${lastScore ? `
              <div style="background-color: var(--bg-subtle); padding: 0.75rem 1rem; border-radius: var(--radius-md); display: inline-block; margin-bottom: 1.5rem; font-size: 0.9rem;">
                <strong>Your Previous Quiz Score:</strong> ${escapeHTML(lastScore)}
              </div>
            ` : ''}

            <div style="display: flex; flex-direction: column; align-items: center; gap: 0.75rem;">
              <label for="quiz-mode-select" style="font-size: 0.95rem; font-weight: 600;">
                Choose Quiz Topic:
              </label>
              <select id="quiz-mode-select" class="quiz-mode-select">
                <option value="random-20">🎯 Mixed Challenge: Random 20 Questions (All Roles)</option>
                ${roles.map(r => `<option value="${r.id}">${escapeHTML(r.name)} (${r.quiz.length} Questions)</option>`).join('')}
              </select>
              <button type="button" class="btn-primary" id="btn-start-quiz" style="padding: 0.75rem 2rem; font-size: 1.05rem;">
                Start Quiz Now →
              </button>
            </div>
          </div>
        </div>
      `;

      const startBtn = container.querySelector('#btn-start-quiz');
      const modeSelect = container.querySelector('#quiz-mode-select');
      startBtn.addEventListener('click', () => {
        startQuiz(modeSelect.value, container);
      });
      return;
    }

    if (state.quizState.completed) {
      // Quiz Results Screen
      renderQuizResults(container);
      return;
    }

    // Question Screen
    const qIndex = state.quizState.currentIndex;
    const currentQ = state.quizState.questions[qIndex];
    const progressPercent = Math.round(((qIndex + 1) / state.quizState.questions.length) * 100);

    container.innerHTML = `
      <div class="quiz-container">
        <div class="quiz-progress-bar-wrap" role="progressbar" aria-valuenow="${progressPercent}" aria-valuemin="0" aria-valuemax="100">
          <div class="quiz-progress-bar" style="width: ${progressPercent}%;"></div>
        </div>

        <div class="quiz-question-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <div class="quiz-q-num">
              Question ${qIndex + 1} of ${state.quizState.questions.length} • ${escapeHTML(currentQ.roleName || '')}
            </div>
            <span style="font-size: 0.85rem; font-weight: 600; color: var(--text-subtle);">
              Score: ${state.quizState.score}
            </span>
          </div>

          <h2 class="quiz-q-text">${escapeHTML(currentQ.q)}</h2>

          <div class="quiz-options-list" id="quiz-options-list">
            ${currentQ.options.map((opt, optIndex) => `
              <button type="button" class="quiz-option-btn" data-index="${optIndex}">
                <span style="width: 1.5rem; height: 1.5rem; border-radius: 50%; border: 1px solid var(--border-medium); display: flex; align-items: center; justify-content: center; font-size: 0.75rem; flex-shrink: 0;">
                  ${String.fromCharCode(65 + optIndex)}
                </span>
                <span>${escapeHTML(opt)}</span>
              </button>
            `).join('')}
          </div>

          <div id="quiz-explanation-box" style="display: none;"></div>

          <div style="display: flex; justify-content: flex-end; margin-top: 1.5rem;">
            <button type="button" class="btn-primary" id="btn-next-question" style="display: none;">
              ${qIndex + 1 === state.quizState.questions.length ? 'View Final Results →' : 'Next Question →'}
            </button>
          </div>
        </div>
      </div>
    `;

    const optButtons = container.querySelectorAll('.quiz-option-btn');
    const explBox = container.querySelector('#quiz-explanation-box');
    const nextBtn = container.querySelector('#btn-next-question');

    let answered = false;

    optButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        if (answered) return;
        answered = true;

        const selectedIndex = parseInt(btn.getAttribute('data-index'), 10);
        const isCorrect = selectedIndex === currentQ.answer;

        if (isCorrect) {
          btn.classList.add('selected-correct');
          state.quizState.score++;
        } else {
          btn.classList.add('selected-wrong');
          // Highlight correct option
          optButtons[currentQ.answer].classList.add('show-correct');
        }

        // Record response
        state.quizState.answers.push({
          question: currentQ.q,
          selected: selectedIndex,
          correct: currentQ.answer,
          isCorrect,
          explanation: currentQ.explanation,
          roleId: currentQ.roleId
        });

        // Show Explanation
        explBox.className = `quiz-feedback-box ${isCorrect ? 'correct' : 'wrong'}`;
        explBox.innerHTML = `
          <strong>${isCorrect ? '✓ Correct!' : '✗ Not quite.'}</strong>
          <p style="margin-top: 0.25rem;">${escapeHTML(currentQ.explanation)}</p>
        `;
        explBox.style.display = 'block';

        // Show Next button
        nextBtn.style.display = 'inline-flex';
        nextBtn.focus();
      });
    });

    nextBtn.addEventListener('click', () => {
      if (state.quizState.currentIndex + 1 < state.quizState.questions.length) {
        state.quizState.currentIndex++;
        renderQuizView(container);
      } else {
        state.quizState.completed = true;
        renderQuizView(container);
      }
    });
  }

  function startQuiz(mode, container) {
    const { roles } = state.data;
    let questions = [];

    if (mode === 'random-20') {
      // Collect all questions across all roles
      const allQ = [];
      roles.forEach(r => {
        r.quiz.forEach(q => {
          allQ.push({ ...q, roleId: r.id, roleName: r.name });
        });
      });
      // Shuffle and pick 20
      questions = allQ.sort(() => 0.5 - Math.random()).slice(0, 20);
    } else {
      const selectedRole = roles.find(r => r.id === mode);
      if (selectedRole) {
        questions = selectedRole.quiz.map(q => ({ ...q, roleId: selectedRole.id, roleName: selectedRole.name }));
      }
    }

    state.quizState = {
      active: true,
      mode,
      questions,
      currentIndex: 0,
      score: 0,
      answers: [],
      completed: false
    };

    renderQuizView(container);
  }

  function renderQuizResults(container) {
    const { score, questions, answers } = state.quizState;
    const total = questions.length;
    const percent = Math.round((score / total) * 100);
    const passed = percent >= 80;

    // Save in localStorage
    const scoreStr = `${score}/${total} (${percent}%) - ${passed ? 'PASSED' : 'NEEDS REVIEW'}`;
    localStorage.setItem('role_ready_last_quiz_score', scoreStr);

    const incorrect = answers.filter(a => !a.isCorrect);

    container.innerHTML = `
      <div class="quiz-container">
        <div class="quiz-results-card">
          <div class="quiz-score-circle" style="border-color: ${passed ? 'var(--success)' : 'var(--danger)'};">
            <span class="quiz-score-num" style="color: ${passed ? 'var(--success)' : 'var(--danger)'};">${percent}%</span>
            <span class="quiz-score-percent">${score} of ${total}</span>
          </div>

          <h2 style="font-size: 1.75rem; font-weight: 800; margin-bottom: 0.5rem;">
            ${passed ? '🎉 Congratulations! You Passed' : '📚 Good Effort — Time to Review'}
          </h2>
          <p style="color: var(--text-muted); max-width: 500px; margin: 0 auto 2rem;">
            ${passed
              ? 'You have reached the company benchmark (≥ 80%). You understand the role profiles, technical requirements, and candidate objection handling.'
              : 'The target score for live candidate calling is ≥ 80%. Review the missed questions below and re-test to build confidence.'}
          </p>

          <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin-bottom: 2.5rem;">
            <button type="button" class="btn-primary" id="btn-retake-quiz">
              Take Another Quiz ↺
            </button>
            <a href="#/" class="btn-outline">
              Back to Roles Directory
            </a>
          </div>

          ${incorrect.length > 0 ? `
            <div style="text-align: left; border-top: 1px solid var(--border-light); padding-top: 2rem;">
              <h3 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 1rem;">
                Questions to Review (${incorrect.length}):
              </h3>
              <div style="display: flex; flex-direction: column; gap: 1rem;">
                ${incorrect.map(item => `
                  <div style="background-color: var(--bg-subtle); padding: 1.25rem; border-radius: var(--radius-md); border-left: 3px solid var(--danger);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
                      <strong>${escapeHTML(item.question)}</strong>
                      ${item.roleId ? `<a href="#/role/${item.roleId}" style="font-size: 0.8rem; font-weight: 600; white-space: nowrap;">Review Role Guide →</a>` : ''}
                    </div>
                    <p style="font-size: 0.875rem; color: var(--text-muted);">
                      <strong>Explanation:</strong> ${escapeHTML(item.explanation)}
                    </p>
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}
        </div>
      </div>
    `;

    container.querySelector('#btn-retake-quiz').addEventListener('click', () => {
      state.quizState.active = false;
      renderQuizView(container);
    });
  }

  // ==========================================================================
  // GLOBAL SEARCH MODAL (FR-4, FR-5, FR-13)
  // ==========================================================================
  function initSearchModal() {
    const modal = document.getElementById('search-modal');
    const input = document.getElementById('global-search-input');
    const resultsContainer = document.getElementById('search-results-list');
    const openBtn = document.getElementById('btn-open-search');
    const closeBtn = document.getElementById('btn-close-search');

    if (!modal || !input) return;

    function openModal() {
      modal.classList.add('open');
      input.value = '';
      state.searchQuery = '';
      state.searchResults = [];
      state.selectedSearchIndex = 0;
      renderSearchResults();
      setTimeout(() => input.focus(), 50);
    }

    function closeModal() {
      modal.classList.remove('open');
    }

    openBtn.addEventListener('click', openModal);
    closeBtn.addEventListener('click', closeModal);

    // Click outside to close
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });

    // Keyboard Shortcut "/" to open search, Escape to close (FR-13)
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && !modal.classList.contains('open') && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openModal();
      } else if (e.key === 'Escape' && modal.classList.contains('open')) {
        closeModal();
      } else if (modal.classList.contains('open')) {
        // Arrow navigation
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          if (state.searchResults.length > 0) {
            state.selectedSearchIndex = (state.selectedSearchIndex + 1) % state.searchResults.length;
            highlightSearchResult();
          }
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (state.searchResults.length > 0) {
            state.selectedSearchIndex = (state.selectedSearchIndex - 1 + state.searchResults.length) % state.searchResults.length;
            highlightSearchResult();
          }
        } else if (e.key === 'Enter') {
          e.preventDefault();
          if (state.searchResults[state.selectedSearchIndex]) {
            const selected = state.searchResults[state.selectedSearchIndex];
            closeModal();
            window.location.hash = selected.url;
          }
        }
      }
    });

    // Instant search input listener
    input.addEventListener('input', (e) => {
      const q = e.target.value.trim().toLowerCase();
      state.searchQuery = q;
      state.selectedSearchIndex = 0;
      performSearch(q);
      renderSearchResults();
    });

    function normalize(str) {
      if (!str) return '';
      return String(str).toLowerCase().replace(/[\s\/\-_.,()]+/g, '');
    }

    function performSearch(q) {
      if (!q || !state.data) {
        state.searchResults = [];
        return;
      }

      const qNorm = normalize(q);
      const results = [];
      const { roles, glossary } = state.data;

      // Helper matcher
      function matches(text) {
        if (!text) return false;
        const lower = text.toLowerCase();
        return lower.includes(q) || (qNorm.length >= 2 && normalize(lower).includes(qNorm));
      }

      // 1. Search Role Names & Alternate Titles (FR-5)
      roles.forEach(role => {
        const nameMatch = matches(role.name);
        if (nameMatch) {
          results.push({
            title: role.name,
            type: 'Role',
            subtext: role.category + ' — ' + role.oneLiner,
            url: `#/role/${role.id}`
          });
        }

        // Match alternate titles
        role.altTitles.forEach(alt => {
          if (matches(alt)) {
            results.push({
              title: `${alt} → ${role.name}`,
              type: 'Alternate Title',
              subtext: `Maps to ${role.name} (${role.category})`,
              url: `#/role/${role.id}`
            });
          }
        });

        // Match key terms
        role.keyTerms.forEach(kt => {
          if (matches(kt.term) || matches(kt.definition)) {
            results.push({
              title: `${kt.term} (${role.name})`,
              type: 'Key Term',
              subtext: kt.definition,
              url: `#/role/${role.id}#sec-key-terms`
            });
          }
        });

        // Match tools
        if (matches(role.toolsSummary)) {
          results.push({
            title: `Tools in ${role.name}`,
            type: 'Tool / Tech',
            subtext: role.toolsSummary.slice(0, 100) + '...',
            url: `#/role/${role.id}#sec-tools`
          });
        }

        // Match certifications
        if (matches(role.certificationsSummary)) {
          results.push({
            title: `Certifications in ${role.name}`,
            type: 'Certification',
            subtext: role.certificationsSummary.slice(0, 100) + '...',
            url: `#/role/${role.id}#sec-certs`
          });
        }

        // Match real-world project examples
        if (role.realWorldExamples) {
          role.realWorldExamples.forEach(ex => {
            if (matches(ex.title) || matches(ex.scenario) || matches(ex.whatTheyDo) || matches(ex.impact)) {
              results.push({
                title: `${ex.title} (${role.name})`,
                type: 'Project Example',
                subtext: `${ex.industry}: ${ex.whatTheyDo.slice(0, 95)}...`,
                url: `#/role/${role.id}#sec-examples`
              });
            }
          });
        }
      });

      // Deduplicate by URL and limit to top 15 results
      const seen = new Set();
      state.searchResults = results.filter(item => {
        const key = item.title + item.url;
        if (seen.has(key)) return false;
        seen.add(key);
        return true;
      }).slice(0, 15);
    }

    function renderSearchResults() {
      if (!state.searchQuery) {
        resultsContainer.innerHTML = `
          <div style="padding: 2rem; text-align: center; color: var(--text-subtle);">
            <p>Type to search across 18 roles, alternate titles (e.g. SRE, SOC, ETL, Airflow), key terms, project examples, and tools.</p>
          </div>
        `;
        return;
      }

      if (state.searchResults.length === 0) {
        resultsContainer.innerHTML = `
          <div style="padding: 2rem; text-align: center; color: var(--text-subtle);">
            <p>No results found for "<strong>${escapeHTML(state.searchQuery)}</strong>"</p>
          </div>
        `;
        return;
      }

      resultsContainer.innerHTML = state.searchResults.map((item, idx) => `
        <a href="${item.url}" class="search-result-item ${idx === state.selectedSearchIndex ? 'highlighted' : ''}" data-index="${idx}">
          <div>
            <div class="search-result-title">${escapeHTML(item.title)}</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.15rem;">${escapeHTML(item.subtext)}</div>
          </div>
          <span class="search-result-type-badge">${escapeHTML(item.type)}</span>
        </a>
      `).join('');

      // Click event on item
      resultsContainer.querySelectorAll('.search-result-item').forEach(el => {
        el.addEventListener('click', () => {
          closeModal();
        });
      });
    }

    function highlightSearchResult() {
      const items = resultsContainer.querySelectorAll('.search-result-item');
      items.forEach((item, idx) => {
        item.classList.toggle('highlighted', idx === state.selectedSearchIndex);
        if (idx === state.selectedSearchIndex) {
          item.scrollIntoView({ block: 'nearest' });
        }
      });
    }
  }

  // Start on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

})();
