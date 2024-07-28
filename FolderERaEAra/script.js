document.getElementById('modeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');

    const logo = document.getElementById('logo');
    if (document.body.classList.contains('dark-mode')) {
        logo.src = 'rainboweye.jpg';
    } else {
        logo.src = 'blueeye.png';
    }
});

document.getElementById('requestCameraPermission').addEventListener('click', function() {
    window.location.href = 'camera.html';
});
