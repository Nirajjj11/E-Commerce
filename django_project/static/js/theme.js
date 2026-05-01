document.addEventListener("DOMContentLoaded", function () {
      const btn = document.getElementById("themeToggle");
      const icon = btn.querySelector("i");
      const body = document.body;

      if (!btn) return;

      function updateIcon() {
            if (body.classList.contains("dark-mode")) {
                  icon.classList.remove("bi-moon");
                  icon.classList.add("bi-sun");
            } else {
                  icon.classList.remove("bi-sun");
                  icon.classList.add("bi-moon");
            }
      }

      // Load saved theme
      if (localStorage.getItem("theme") === "dark") {
            body.classList.add("dark-mode");
      }

      updateIcon();

      btn.addEventListener("click", () => {
            body.classList.toggle("dark-mode");

            if (body.classList.contains("dark-mode")) {
                  localStorage.setItem("theme", "dark");
            } else {
                  localStorage.setItem("theme", "light");
            }

            updateIcon();
      });
});