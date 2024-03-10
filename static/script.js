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
        function openDialog(imagePath) {
            var dialogBox = document.getElementById("dialog-box");
            var placeInput = document.getElementById("placeInput");
            var resultText = document.getElementById("result-text");
        
            placeInput.value = "";
            resultText.innerHTML = "";
        
            document.getElementById("dialog-image").src = imagePath;
            dialogBox.style.display = "block";
        }
        
        function submitPlace() {
            var placeInput = document.getElementById("placeInput");
            var resultText = document.getElementById("result-text");
        
            var userInput = placeInput.value.toLowerCase().trim();
        
            if (userInput === "pl. du chateau, jumilhac-le-grand") {
                resultText.innerHTML = "Félicitations, vous avez trouvé ! Voici le flag : {RoBineStenFerMED@nsLePéRig0rD}";
            } else {
                resultText.innerHTML = "Ce n'est pas la bonne adresse ou vous l'avez mal écrit (vérifiez bien le format)";
            }
        }