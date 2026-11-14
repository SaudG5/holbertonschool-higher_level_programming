function updateHeader () {
  document.querySelector('header').textContent = 'New Header!!!';
}

document.querySelector('#update_header').onclick = updateHeader;