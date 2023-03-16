# Отправка AJAX запроса
```javascript
const apiBlock = document.querySelector('.api__block');


const state = {
    options: []
}


const request = async (url, method) => {
    await fetch(url, {
        method: method,
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        }
    })
    .then((response) => {
        return response.json()
    })
    .then((response) =>{
        state.options = state.options.concat(response)
    });
}


document.addEventListener('DOMContentLoaded', ()=>{
    request('http://localhost/api/users', 'OPTIONS');
    console.log(state);
})
```
