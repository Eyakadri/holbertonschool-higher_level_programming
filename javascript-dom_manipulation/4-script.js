const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
        document.querySelector('.my_list').appendChild(newItem);
});