function sayHello () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      document.querySelector('#hello').textContent = data.hello;
    });
}

document.addEventListener('DOMContentLoaded', sayHello);