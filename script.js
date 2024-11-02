document.getElementById('db_type').addEventListener('change', function () {
    const extraFields = document.getElementById('extra_fields');
    if (this.value === 'sqlite') {
        extraFields.style.display = 'none';
    } else {
        extraFields.style.display = 'block';
    }
});