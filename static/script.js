const menuHamburger = document.querySelector(".menu-hamburger");
    const navLinks = document.querySelector(".nav-links");


    menuHamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        menuHamburger.classList.toggle('active');


    
    });
    document.addEventListener('DOMContentLoaded', function() {
        const epreuves = document.querySelectorAll('.container');

        epreuves.forEach(epreuve => {
            epreuve.addEventListener('click', function() {
                // Trouve le contenu de l'épreuve dans ce container
                const epreuveContent = this.querySelector('.epreuve-content');

                // Toggle la classe 'open' pour afficher ou cacher le contenu
                epreuveContent.classList.toggle('open');
            });
        });
    });
    function hideErrorMessage() {
        var errorMessage = document.getElementById('error-message');
        errorMessage.style.display = 'none';
    }

    // Vérifie si le message d'erreur est affiché et le masque après 3 secondes
    window.addEventListener('DOMContentLoaded', function() {
        var errorMessage = document.getElementById('error-message');
        if (errorMessage.style.display === 'block') {
            setTimeout(hideErrorMessage, 1800); // Masquer le message après 3 secondes (3000 ms)
        }
        
    });

    function showPopup(content) {
        // Créer le popup
        var popup = document.createElement('div');
        popup.classList.add('popup');
    
        // Créer le contenu du popup
        var popupContent = document.createElement('div');
        popupContent.classList.add('popup-content');
        popupContent.innerHTML = content;
    
        // Créer le bouton de fermeture du popup
        var popupClose = document.createElement('span');
        popupClose.classList.add('popup-close');
        popupClose.innerHTML = '&times;';
        popupClose.onclick = function() {
            document.body.removeChild(popup);
        };
    
        // Ajouter le contenu et le bouton de fermeture au popup
        popup.appendChild(popupContent);
        popup.appendChild(popupClose);
    
        // Ajouter le popup à la page
        document.body.appendChild(popup);
    }