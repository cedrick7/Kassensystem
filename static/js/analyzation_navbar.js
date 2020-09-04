/* burger menu */
const hamburgerButton = document.getElementById('burger-button');
const hamburger = document.getElementsByClassName('animated-icon');
const navLinks = document.getElementsByClassName('navLink');

hamburgerButton.addEventListener('click', () => {
    $('.animated-icon').toggleClass('open');
});

for (var i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener('click', () => {
        $('.navbar-collapse').collapse('hide');
        $('.animated-icon').toggleClass('open');
    });
}