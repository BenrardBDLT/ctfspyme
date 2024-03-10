const menuHamburger = document.querySelector(".menu-hamburger");
    const navLinks = document.querySelector(".nav-links");


    menuHamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        menuHamburger.classList.toggle('active');


    
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

        // Activer l'effet de fondu
        setTimeout(function() {
            popup.classList.add('open');
        }, 10);
        }
        popupClose.onclick = function() {
            popup.classList.remove('open'); // Supprimer la classe 'open' pour déclencher l'effet de fondu
            setTimeout(function() {
                document.body.removeChild(popup);
            }, 500); // Attendre la fin de la transition avant de supprimer le popup
        };
        
        
        
        document.addEventListener('DOMContentLoaded', function() {
            const menuItems = document.querySelectorAll('.menu li a');
            const displayedImage = document.getElementById('displayed-image');
        
            // Fonction pour changer l'image affichée
            function changeImage(event) {
                event.preventDefault();
                const imageSrc = event.target.getAttribute('data-image');
                displayedImage.src = imageSrc;
            }
        
            // Ajouter un gestionnaire d'événement à chaque élément du menu
            menuItems.forEach(function(item) {
                item.addEventListener('click', changeImage);
            });
        });

        function openDialog(imageSrc) {
    const imagePopup = document.getElementById('imagePopup');
    const popupImage = document.getElementById('popupImage');

    popupImage.src = "{{ url_for('static', filename='img/epreuve/') }}" + imageSrc;
    imagePopup.style.display = 'block';
}

function closeDialog() {
    const imagePopup = document.getElementById('imagePopup');
    imagePopup.style.display = 'none';
} 

