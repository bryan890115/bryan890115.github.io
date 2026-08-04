(function () {
    'use strict';

    const root = document.documentElement;
    if (root) {
        root.classList.add('js');
    }

    const initialiseNavigation = function () {
        const toggle = document.getElementById('nav-toggle');
        const navigation = document.getElementById('primary-navigation');

        if (!toggle || !navigation) {
            return;
        }

        const desktopMedia = window.matchMedia('(min-width: 48.0625rem)');

        const navigationIsOpen = function () {
            return toggle.getAttribute('aria-expanded') === 'true';
        };

        const setNavigationOpen = function (isOpen) {
            toggle.setAttribute('aria-expanded', String(isOpen));
            navigation.dataset.open = String(isOpen);
        };

        const closeNavigation = function (restoreFocus) {
            if (!navigationIsOpen()) {
                return;
            }

            setNavigationOpen(false);

            if (restoreFocus) {
                toggle.focus();
            }
        };

        setNavigationOpen(false);

        toggle.addEventListener('click', function () {
            setNavigationOpen(!navigationIsOpen());
        });

        navigation.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                closeNavigation(false);
            });
        });

        document.addEventListener('keydown', function (event) {
            if (event.key !== 'Escape' || !navigationIsOpen()) {
                return;
            }

            event.preventDefault();
            closeNavigation(true);
        });

        const handleDesktopChange = function (event) {
            if (event.matches) {
                closeNavigation(false);
            }
        };

        if (typeof desktopMedia.addEventListener === 'function') {
            desktopMedia.addEventListener('change', handleDesktopChange);
        } else {
            desktopMedia.addListener(handleDesktopChange);
        }
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initialiseNavigation, { once: true });
    } else {
        initialiseNavigation();
    }
}());
