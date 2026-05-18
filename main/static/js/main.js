/* ==========================================================================
   M.S. CATERING SERVICES — Main JavaScript
   Single source of truth for all client-side behaviour.
   ========================================================================== */

(function () {
    'use strict';

    /* ============ INIT LUCIDE ICONS ============ */
    function initIcons() {
        if (window.lucide && typeof window.lucide.createIcons === 'function') {
            window.lucide.createIcons();
        }
    }

    /* ============ INIT AOS (Animate On Scroll) ============ */
    function initAOS() {
        if (window.AOS && typeof window.AOS.init === 'function') {
            const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            window.AOS.init({
                duration: 800,
                easing: 'ease-out-cubic',
                once: true,
                offset: 60,
                delay: 0,
                disable: function () {
                    return prefersReducedMotion || window.innerWidth < 480;
                }
            });
        }
    }

    /* ============ NAVBAR SCROLL EFFECT ============ */
    function initNavbarScroll() {
        const navbar = document.getElementById('navbar');
        if (!navbar) return;

        function handleScroll() {
            if (window.pageYOffset > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }

        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();
    }

    /* ============ MOBILE NAVIGATION ============ */
    function initMobileNav() {
        const toggle   = document.getElementById('navToggle');
        const closeBtn = document.getElementById('navClose');
        const menu     = document.getElementById('navMenu');
        const backdrop = document.getElementById('navBackdrop');
        const body     = document.body;

        if (!toggle || !menu) return;

        function setToggleIcon(name) {
            const icon = toggle.querySelector('i');
            if (icon) {
                icon.setAttribute('data-lucide', name);
                initIcons();
            }
        }

        function openMenu() {
            menu.classList.add('active');
            backdrop && backdrop.classList.add('active');
            body.classList.add('nav-open');
            toggle.setAttribute('aria-expanded', 'true');
            setToggleIcon('x');
        }

        function closeMenu() {
            menu.classList.remove('active');
            backdrop && backdrop.classList.remove('active');
            body.classList.remove('nav-open');
            toggle.setAttribute('aria-expanded', 'false');
            setToggleIcon('menu');
        }

        function toggleMenu(e) {
            if (e) e.stopPropagation();
            if (menu.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        }

        toggle.addEventListener('click', toggleMenu);
        closeBtn && closeBtn.addEventListener('click', closeMenu);
        backdrop && backdrop.addEventListener('click', closeMenu);

        // Close menu when a nav link is tapped
        menu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', closeMenu);
        });

        // Close on outside click (anywhere outside menu + toggle)
        document.addEventListener('click', function (e) {
            if (!menu.classList.contains('active')) return;
            if (!menu.contains(e.target) && !toggle.contains(e.target)) {
                closeMenu();
            }
        });

        // Close on Escape
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && menu.classList.contains('active')) {
                closeMenu();
            }
        });

        // Auto-close on resize to desktop
        let resizeTimer;
        window.addEventListener('resize', function () {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function () {
                if (window.innerWidth > 1024 && menu.classList.contains('active')) {
                    closeMenu();
                }
            }, 150);
        });
    }

    /* ============ ANIMATED COUNTERS ============ */
    function initCounters() {
        const counters = document.querySelectorAll('.stat-number[data-count]');
        if (!counters.length) return;

        const animateCounter = function (el) {
            const target = parseInt(el.getAttribute('data-count'), 10);
            const originalText = el.textContent.trim();
            const isThousand = originalText.toLowerCase().includes('k');

            const duration = 2000;
            const startTime = performance.now();

            function update(now) {
                const elapsed = now - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
                const current = Math.floor(target * eased);

                if (isThousand && target >= 1000) {
                    el.textContent = (current / 1000).toFixed(0) + 'K+';
                } else {
                    el.textContent = current + '+';
                }

                if (progress < 1) {
                    requestAnimationFrame(update);
                } else {
                    el.textContent = originalText;
                }
            }

            requestAnimationFrame(update);
        };

        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.4 });

        counters.forEach(function (c) {
            observer.observe(c);
        });
    }

    /* ============ FAQ ACCORDION (close others when one opens) ============ */
    function initFAQ() {
        const items = document.querySelectorAll('.faq-item');
        items.forEach(function (item) {
            item.addEventListener('toggle', function () {
                if (item.open) {
                    items.forEach(function (other) {
                        if (other !== item) {
                            other.open = false;
                        }
                    });
                }
            });
        });
    }

    /* ============ SMOOTH SCROLL FOR ANCHOR LINKS ============ */
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function (link) {
            link.addEventListener('click', function (e) {
                const targetId = link.getAttribute('href');
                if (!targetId || targetId === '#' || targetId.length < 2) return;

                // Skip link should still work natively (jump-to-content for a11y)
                if (link.classList.contains('skip-link')) return;

                const target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    const offset = 80;
                    const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
                    window.scrollTo({ top: top, behavior: 'smooth' });
                }
            });
        });
    }

    /* ============ DOM READY ============ */
    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }

    ready(function () {
        initIcons();
        initAOS();
        initNavbarScroll();
        initMobileNav();
        initCounters();
        initFAQ();
        initSmoothScroll();
    });

    // Re-init icons after full load (in case AOS swaps in animated elements)
    window.addEventListener('load', function () {
        initIcons();
        if (window.AOS && typeof window.AOS.refresh === 'function') {
            window.AOS.refresh();
        }
    });

})();