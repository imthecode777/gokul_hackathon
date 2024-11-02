document.getElementById('db_type').addEventListener('change', function () {
    const extraFields = document.getElementById('extra_fields');
    if (this.value === 'sqlite') {
        extraFields.style.display = 'none';
    } else {
        extraFields.style.display = 'block';
    }
});

    const isDesktop = window.innerWidth > 768;

    AOS.init({
        once: isDesktop,
        duration: 1000,
    });
