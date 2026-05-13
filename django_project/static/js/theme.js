//    THEME TOGGLE
document.addEventListener("DOMContentLoaded", () => {

      const themeToggle = document.getElementById("themeToggle");
      const themeIcon = document.getElementById("themeIcon");

      if (!themeToggle || !themeIcon) return;

      const html = document.documentElement;

      const setTheme = (theme) => {
            html.setAttribute("data-bs-theme", theme);
            themeIcon.className = theme === "dark" ? "bi bi-sun-fill fs-5" : "bi bi-moon-stars-fill fs-5";
      };

      setTheme(
            localStorage.getItem("theme") || "light"
      );

      themeToggle.addEventListener("click", () => {

            const currentTheme = html.getAttribute("data-bs-theme");
            const newTheme = currentTheme === "dark" ? "light" : "dark";

            localStorage.setItem("theme", newTheme);

            setTheme(newTheme);
      });
});