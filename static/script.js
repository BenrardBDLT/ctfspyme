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
    // script.js
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Empêcher le formulaire d'être soumis normalement

    const flag = document.querySelector('.flag-input').value;

    // Soumettre les données du formulaire à la route Flask
    fetch('/validate-flag', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'flag=' + encodeURIComponent(flag),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Flag valide, effectuez les actions nécessaires ici
            console.log('Flag valide');
            // Réinitialiser le champ du drapeau
            document.querySelector('.flag-input').value = '';
        } else {
            // Flag invalide, effectuez les actions nécessaires ici
            console.log('Flag invalide');
        }
    })
    .catch(error => console.error('Erreur lors de la soumission du formulaire :', error));
});
