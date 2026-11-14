fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const list = document.querySelector('#list_movies');

    for (const movie of data.results) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      list.appendChild(li);
    }
  });