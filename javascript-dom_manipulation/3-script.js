const redHeader = document.getElementById('toggle_header');

redHeader.addEventListener('click', () => {
    if (redHeader.classList.contains('red')) {
        redHeader.classList.remove('red');
        redHeader.classList.add('green');
    } else {
        redHeader.classList.remove('green');
        redHeader.classList.add('red');
    }
});
