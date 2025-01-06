document.addEventListener('DOMContentLoaded', function () {
    const startLevel = document.getElementById('start-level');
    if (startLevel) {
        startLevel.addEventListener('click', (e) => {
            window.location.href = 'weather.html'
        });
    } else {
        console.error('Button with id "start-level" not found!');
    }
})