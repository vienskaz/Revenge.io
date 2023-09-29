var updateBtns = document.getElementsByClassName('update-cart');
var sizeSelect = document.getElementById('size-select');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var itemId = sizeSelect.value;
        var action = this.dataset.action;
        var itemIdButtons = this.dataset.item;

        console.log('itemId:', itemId, 'action:', action);

        if (!itemId && itemIdButtons) {
            itemId = itemIdButtons;
        }

        if (user === 'AnonymousUser') {
            addCookieItem(itemId, action);
        } else {
            updateUserOrder(itemId, action);
        }
    });
}

function addCookieItem(itemId, action){
	console.log('User is not authenticated')

	if(action == 'add'){
		if (cart[itemId] == undefined){
		cart[itemId] = {'quantity':1}
      
		}else{
			cart[itemId]['quantity'] += 1
		}
	}

	if(action == 'remove'){
		cart[itemId]['quantity'] -= 1

		if(cart[itemId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[itemId];
		}
	}
	console.log('Cart:', cart)
	document.cookie='cart=' + JSON.stringify(cart) + ";domain=;path=/";
	
	location.reload()
}

function updateUserOrder(itemId, action) {
    console.log('User is logged in, sending data');
    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'itemId': itemId, 'action': action })
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data);
            location.reload();
        });
}