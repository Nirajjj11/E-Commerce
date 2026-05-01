document.addEventListener("DOMContentLoaded", function () {
      const btn = document.getElementById("themeToggle");
      const icon = document.getElementById("themeIcon");
      const htmlElement = document.documentElement;

      if (!btn || !icon) {
            console.warn("Theme toggle elements not found on this page.");
            return;
      }

      // Function to change the icon and theme attribute
      function updateThemeUI(theme) {
            htmlElement.setAttribute("data-bs-theme", theme);

            if (theme === "dark") {
                  icon.classList.remove("bi-moon-stars-fill");
                  icon.classList.add("bi-sun-fill");
            } else {
                  icon.classList.remove("bi-sun-fill");
                  icon.classList.add("bi-moon-stars-fill");
            }
      }

      // Initialize UI based on what was set in the <head>
      const currentSavedTheme = localStorage.getItem("theme") || "light";
      updateThemeUI(currentSavedTheme);

      // Event listener for the click
      btn.addEventListener("click", (e) => {
            e.preventDefault();
            const currentTheme = htmlElement.getAttribute("data-bs-theme");
            const newTheme = currentTheme === "dark" ? "light" : "dark";

            localStorage.setItem("theme", newTheme);
            updateThemeUI(newTheme);
      });
});