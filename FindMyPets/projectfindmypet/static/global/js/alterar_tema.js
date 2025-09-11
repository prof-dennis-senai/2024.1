const html = document.documentElement;
const btn = document.getElementById("themeToggle");
const icon = btn.querySelector("i");
const logo = document.getElementById("logo");

// URLs dos logos
const logoLight = "static/global/images/logo_tratada_fundo_claro.svg";
const logoDark = "static/global/images/logo_tratada_fundo_escuro.svg";

// Atualiza ícone e logo
function updateThemeVisuals(theme) {
    // ícone
    icon.className = theme === "dark" ? "fa-solid fa-sun" : "fa-solid fa-moon";
    // logo
    logo.src = theme === "dark" ? logoDark : logoLight;
}

// Carregar preferência salva
const savedTheme = localStorage.getItem("theme") || "light";
html.setAttribute("data-mdb-theme", savedTheme);
updateThemeVisuals(savedTheme);

// Alternar tema ao clicar no botão
btn.addEventListener("click", () => {
    const newTheme = html.getAttribute("data-mdb-theme") === "dark" ? "light" : "dark";
    html.setAttribute("data-mdb-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    updateThemeVisuals(newTheme);
});
