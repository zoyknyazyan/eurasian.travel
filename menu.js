document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.getElementById('primary-toggle-button');
  const nav = document.getElementById('site-navigation');

  if (toggleButton && nav) {
    toggleButton.addEventListener('click', function (e) {
      e.preventDefault();

      const isActive = nav.classList.toggle('active');

      // Optional: for accessibility
      toggleButton.setAttribute('aria-expanded', isActive ? 'true' : 'false');
    });
  }
});
