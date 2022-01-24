export function createTopNav(){
    let homeButton = document.createElement('a');
    homeButton.setAttribute('href','/');
    homeButton.innerText = 'Home';
    let registrationButton = document.createElement('a');
    registrationButton.setAttribute('href','/registration');
    registrationButton.innerText = 'SignUP';
    let loginButton = document.createElement('a');
    loginButton.setAttribute('href','/login');
    loginButton.innerText = 'LogIN';
    let logoutButton = document.createElement('a');
    logoutButton.setAttribute('href','/');
    logoutButton.innerText = 'LogOUT';

    let topNav = document.getElementById('top_bar');
    topNav.appendChild(homeButton);
    topNav.appendChild(registrationButton);
    topNav.appendChild(loginButton);
    topNav.appendChild(logoutButton);
}
