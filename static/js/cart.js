var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.produit
        var action = this.dataset.action
        console.log('productId:', productId, 'action: ', action)

        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log('Utilisateur n\' pas connecté')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('Utilisateur est connecté, Transfère des donnees')

    var url = '/update_item/'
    
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) => {
        return response.json()
    }) 
    .then((data) => {
        console.log('data:',data)
        location.reload()
    });
}