export default function () {
    const toggleMenu = document.getElementById('toggle-menu');
    const mainMenu = document.getElementById('main-menu');
    if (!toggleMenu || !mainMenu) return;

    const setOpen = (isOpen: boolean) => {
        mainMenu.classList.toggle('show', isOpen);
        document.body.classList.toggle('show-menu', isOpen);
        toggleMenu.classList.toggle('is-active', isOpen);
        toggleMenu.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    };

    setOpen(false);
    toggleMenu.addEventListener('click', () => {
        setOpen(toggleMenu.getAttribute('aria-expanded') !== 'true');
    });
}
