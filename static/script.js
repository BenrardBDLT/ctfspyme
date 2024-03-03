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