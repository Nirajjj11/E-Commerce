const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const htmlElement = document.documentElement;

// Initialize theme from localStorage immediately to prevent "flash"
if (localStorage.getItem('theme') === 'dark') {
      htmlElement.setAttribute('data-bs-theme', 'dark');
      if (themeIcon) themeIcon.classList.replace('bi-moon-stars-fill', 'bi-sun-fill');
}

if (themeToggle) {
      themeToggle.addEventListener('click', () => {
            if (htmlElement.getAttribute('data-bs-theme') === 'dark') {
                  htmlElement.setAttribute('data-bs-theme', 'light');
                  themeIcon.classList.replace('bi-sun-fill', 'bi-moon-stars-fill');
                  localStorage.setItem('theme', 'light');
            } else {
                  htmlElement.setAttribute('data-bs-theme', 'dark');
                  themeIcon.classList.replace('bi-moon-stars-fill', 'bi-sun-fill');
                  localStorage.setItem('theme', 'dark');
            }
      });
}
