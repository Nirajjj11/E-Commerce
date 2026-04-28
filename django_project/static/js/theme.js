const themeToggle = () => {
      const htmlElement = document.documentElement;
      const currentTheme = htmlElement.getAttribute('data-bs-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';

      htmlElement.setAttribute('data-bs-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateIcon(newTheme);
};

const updateIcon = (theme) => {
      const icon = document.getElementById('themeIcon');
      if (icon) {
            if (theme === 'dark') {
                  icon.classList.replace('bi-moon-stars-fill', 'bi-sun-fill');
            } else {
                  icon.classList.replace('bi-sun-fill', 'bi-moon-stars-fill');
            }
      }
};

// Apply theme immediately to prevent white flash
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-bs-theme', savedTheme);

window.addEventListener('DOMContentLoaded', () => {
      updateIcon(savedTheme);
      const btn = document.getElementById('themeToggle');
      if (btn) btn.addEventListener('click', themeToggle);
});