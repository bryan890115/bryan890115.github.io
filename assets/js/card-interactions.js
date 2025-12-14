document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card-item');
    let detailIdCounter = 0;

    cards.forEach((card, index) => {
        let detailSection = card.querySelector('.card-details');

        // If a navigation target exists, surface it inside the expandable area
        const href = card.getAttribute('data-href');
        if (href && !detailSection) {
            detailSection = document.createElement('div');
            detailSection.className = 'card-details';
            card.appendChild(detailSection);
        }

        if (href && detailSection && !detailSection.querySelector('.card-action')) {
            const actionLink = document.createElement('a');
            actionLink.href = href;
            actionLink.className = 'card-action';
            actionLink.textContent = 'Open link';
            actionLink.addEventListener('click', (event) => {
                event.stopPropagation();
            });
            detailSection.appendChild(actionLink);
        }

        // Accessibility attributes
        card.setAttribute('tabindex', '0');
        card.setAttribute('role', 'button');
        card.setAttribute('aria-expanded', 'false');
        if (detailSection) {
            detailIdCounter += 1;
            const detailId = `card-details-${detailIdCounter}`;
            detailSection.setAttribute('id', detailId);
            card.setAttribute('aria-controls', detailId);
        }

        // Add a chevron that is hidden from screen readers
        let chevron = card.querySelector('.card-chevron');
        if (!chevron) {
            chevron = document.createElement('span');
            chevron.className = 'card-chevron';
            chevron.setAttribute('aria-hidden', 'true');
            card.appendChild(chevron);
        }

        const toggleCard = () => {
            const expanded = card.classList.toggle('expanded');
            card.setAttribute('aria-expanded', expanded ? 'true' : 'false');
        };

        card.addEventListener('click', (event) => {
            if (event.target.closest('a')) {
                return;
            }
            toggleCard();
        });

        card.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                toggleCard();
            }
        });
    });
});
