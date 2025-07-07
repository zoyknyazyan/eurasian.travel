document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.getElementById('primary-toggle-button');
  const nav = document.getElementById('site-navigation');

  if (toggleButton && nav) {
    const toggleMenu = function () {
      nav.classList.toggle('active');
    };

    toggleButton.addEventListener('click', toggleMenu);
    toggleButton.addEventListener('touchstart', toggleMenu);
  }
});
