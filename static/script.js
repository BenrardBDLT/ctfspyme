const menuHamburger = document.querySelector(".menu-hamburger");
    const navLinks = document.querySelector(".nav-links");

    menuHamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        menuHamburger.classList.toggle('active');
    });
    
    