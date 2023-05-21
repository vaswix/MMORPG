// const emailForm = document.getElementById('email-verify')
// const container = document.getElementById('main')
//
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
//
// const csrftoken = getCookie('csrftoken');
//
// async function handleForm(event) {
//     event.preventDefault()
//     let email = document.getElementById('email-confirm')
//     email.disabled = true
//     let data = {'email': email.value}
//     await fetch('http://127.0.0.1:8000/account/confirmation/send_one_time_code/', {
//         method: 'POST',
//         headers: {
//             'Accept': 'application/json',
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify(data)
//     })
//         .then(function (response) {
//             return response.json();
//         })
//
//         .then(function (json) {
//             if (json['status'] === 'ok') {
//                 let br = document.createElement('br')
//                 let newInput = document.createElement('input')
//                 let newBtn = document.createElement('button')
//
//                 newBtn.appendChild(document.createTextNode('Отправить код'))
//
//                 newInput.setAttribute('placeholder', 'Введите код')
//                 newInput.setAttribute('id', 'email-code')
//
//
//                 container.appendChild(br)
//                 container.appendChild(newInput)
//                 container.appendChild(newBtn)
//             }
//         })
// }
//
// emailForm.addEventListener('submit', handleForm)