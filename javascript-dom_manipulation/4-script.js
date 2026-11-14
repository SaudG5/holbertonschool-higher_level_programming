function addItem () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('.my_list').appendChild(li);
}

document.querySelector('#add_item').onclick = addItem;