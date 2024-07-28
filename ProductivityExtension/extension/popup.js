document.getElementById('fetchData').addEventListener('click', () => {
  fetch(`${CONFIG.BACKEND_URL}/data`)
    .then(response => response.json())
    .then(data => {
      document.getElementById('seconds').innerText = JSON.stringify(data);
    })
    .catch(error => console.error('Error:', error));
});
