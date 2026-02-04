/**
 * TuberSYS 3.0 - JavaScript Principal
 * Gestion de l'interactivité de l'interface
 */

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 TuberSYS 3.0 chargé');

    // Initialiser les composants
    initSidebar();
    initNotifications();
    initUserMenu();
    initFlashMessages();
});

/**
 * Gestion de la sidebar responsive
 */
function initSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.getElementById('menu-toggle');

    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', function() {
            sidebar.classList.toggle('open');
        });

        // Fermer la sidebar au clic en dehors (mobile)
        document.addEventListener('click', function(event) {
            if (window.innerWidth <= 768) {
                if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
                    sidebar.classList.remove('open');
                }
            }
        });
    }
}

/**
 * Gestion des notifications
 */
function initNotifications() {
    const notificationBell = document.querySelector('.notification-bell');

    if (notificationBell) {
        notificationBell.addEventListener('click', function() {
            // TODO: Afficher le panneau de notifications
            console.log('Notifications clicked');
        });
    }
}

/**
 * Gestion du menu utilisateur
 */
function initUserMenu() {
    const userProfile = document.querySelector('.user-profile');
    const userDropdown = document.querySelector('.user-dropdown');

    if (userProfile && userDropdown) {
        // Le dropdown est déjà géré par le CSS hover
        // Mais on peut ajouter un toggle au clic pour mobile
        const userMenuToggle = document.querySelector('.user-menu-toggle');

        if (userMenuToggle) {
            userMenuToggle.addEventListener('click', function(e) {
                e.stopPropagation();
                userDropdown.classList.toggle('show');
            });

            // Fermer au clic en dehors
            document.addEventListener('click', function(event) {
                if (!userProfile.contains(event.target)) {
                    userDropdown.classList.remove('show');
                }
            });
        }
    }
}

/**
 * Auto-fermeture des messages flash
 */
function initFlashMessages() {
    const alerts = document.querySelectorAll('.alert');

    alerts.forEach(alert => {
        // Auto-fermeture après 5 secondes
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
}

/**
 * Fonction utilitaire pour faire des requêtes AJAX
 */
function ajax(url, options = {}) {
    const defaults = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const config = { ...defaults, ...options };

    return fetch(url, config)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .catch(error => {
            console.error('Ajax error:', error);
            throw error;
        });
}

/**
 * Afficher une notification toast
 */
function showToast(message, type = 'info') {
    const iconMap = {
        success: 'fa-check-circle',
        danger: 'fa-exclamation-circle',
        warning: 'fa-exclamation-triangle',
        info: 'fa-info-circle'
    };

    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.innerHTML = `
        <i class="fas ${iconMap[type]}"></i>
        <span>${message}</span>
        <button class="alert-close" onclick="this.parentElement.remove()">×</button>
    `;

    let flashContainer = document.querySelector('.flash-messages');

    if (!flashContainer) {
        flashContainer = document.createElement('div');
        flashContainer.className = 'flash-messages';
        const pageContent = document.querySelector('.page-content');
        if (pageContent) {
            pageContent.insertBefore(flashContainer, pageContent.firstChild);
        } else {
            document.body.insertBefore(flashContainer, document.body.firstChild);
        }
    }

    flashContainer.appendChild(alert);

    // Auto-suppression après 5 secondes
    setTimeout(() => {
        alert.style.opacity = '0';
        setTimeout(() => alert.remove(), 300);
    }, 5000);
}

/**
 * Confirmer une action
 */
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

/**
 * Formater un nombre en devise
 */
function formatCurrency(amount) {
    return new Intl.NumberFormat('fr-FR', {
        style: 'currency',
        currency: 'EUR'
    }).format(amount);
}

/**
 * Formater une date
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('fr-FR').format(date);
}

/**
 * Formater une date avec heure
 */
function formatDateTime(dateString) {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('fr-FR', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    }).format(date);
}

/**
 * Filtrer un tableau
 */
function filterTable(tableId, searchValue) {
    const table = document.getElementById(tableId);
    if (!table) return;

    const rows = table.getElementsByTagName('tr');
    const filter = searchValue.toLowerCase();

    for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? '' : 'none';
    }
}

/**
 * Debounce function pour optimiser les recherches
 */
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

/**
 * Copier dans le presse-papier
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copié dans le presse-papier', 'success');
    }).catch(err => {
        console.error('Erreur de copie:', err);
        showToast('Erreur lors de la copie', 'danger');
    });
}

/**
 * Export des fonctions pour utilisation globale
 */
window.TuberSYS = {
    ajax,
    showToast,
    confirmAction,
    formatCurrency,
    formatDate,
    formatDateTime,
    filterTable,
    debounce,
    copyToClipboard
};

console.log('✅ TuberSYS JavaScript chargé avec succès');
