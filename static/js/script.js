import {addResponseOnClick} from "./changePageLogic.js";

// fetch('https://swapi.py4e.com/api/people/1')
//   .then(response => response.json())
//   .then(data => console.log(data));


// function sendUserInfo(){
//     let userInfo = {
//         'name': 'John Brown',
//         'type': 'Admin'
//     }
//     const request = new XMLHttpRequest();
//     request.open('POST', '/processUserInfo/'+JSON.stringify(userInfo))
//     request.onload =() => {
//         const flaskMessage = request.responseText
//         console.log(flaskMessage)
//     }
//     request.send();
// }
//
// sendUserInfo();
document.addEventListener("DOMContentLoaded", addResponseOnClick)