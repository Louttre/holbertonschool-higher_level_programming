function fetchAndDisplayHello() {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const helloTranslation = data.hello;
      document.getElementById('hello').textContent = helloTranslation;
    })
    .catch(error => {
      console.error('There has been a problem with your fetch operation:', error);
    });
}

document.addEventListener('DOMContentLoaded', fetchAndDisplayHello);
