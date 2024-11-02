document.getElementById('db_type').addEventListener('change', function () {
    const extraFields = document.getElementById('extra_fields');
    if (this.value === 'sqlite') {
        extraFields.style.display = 'none';
    } else {
        extraFields.style.display = 'block';
    }
});

    const isDesktop = window.innerWidth > 768; // Set the breakpoint for desktop screens

    AOS.init({
        once: isDesktop, // Trigger animations only once if on desktop
        duration: 1000,
    });
