function toggleColor () {
  const header = document.querySelector('header');

  if (header.className === 'red') {
    header.className = 'green';
  } else {
    header.className = 'red';
  }
}

document.querySelector('#toggle_header').onclick = toggleColor;