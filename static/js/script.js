function showAlert() {
    alert("SWAPI");
}

showAlert();

fetch('https://swapi.py4e.com/api/people/1')
//fetch('https://swapi.py4e.com/api/planets/1/?format=wookiee')
  .then(response => response.json())
  .then(data => console.log(data));