function getClickedPlanetName(){
    const clickedButton = document.querySelector(".clicked");
    let planetName;
    const table = document.getElementById("table");
    const tbody = table.children[1];

    for (const tr of tbody.children){

        for (const th of tr.children){
            if (th === clickedButton){
                planetName = tr.children[0].innerText;
                return planetName;
            }
        }
   }
}


function getPlanetResidentsTableData(planet_name){
    let planet = {
        'name': planet_name
    }
    const request = new XMLHttpRequest();
    request.open('POST', '/planetResidents/' + JSON.stringify(planet))
    request.onload =() => {
        const flaskResponse = request.responseText;
        const headers = JSON.parse(flaskResponse).headers;
        const content = JSON.parse(flaskResponse).content;
        let residentsTableData = [headers, content];

        const table = createResidentsTable(residentsTableData);
        console.log(table)
        createPopupModal(table,planet_name);
        const modal = document.querySelector(".modal");
        showModal(modal);
        const closeButton = document.querySelector(".close-button");
        closeButton.addEventListener("click", hideModal);
    }
    request.send();
}


function createResidentsTable(residentsTableData){
    const headers = residentsTableData[0];
    const content = residentsTableData[1];

    let table = document.createElement('table');
    let thead = document.createElement('thead');

    for (const header of headers){
        let th = document.createElement('th');
        th.innerText = header;
        thead.appendChild(th);
    }

    let tbody = document.createElement('tbody');

    for (const row of content){
        let tr = document.createElement('tr');

        for (const cell of row){
            let th = document.createElement('th');
            th.innerText = cell;
            tr.appendChild(th);
        }
        tbody.appendChild(tr);
    }
    table.appendChild(thead);
    table.appendChild(tbody);

    const wrapper = document.createElement('div');
    wrapper.classList.add("residents-table");
    return table;
}


function createPopupModal(table, planet_name){
    let divModal = document.createElement('div');
    divModal.classList.add('modal');
    let divContent = document.createElement('div');
    divContent.classList.add('modal-content');
    let closeButton = document.createElement('span');
    closeButton.classList.add('close-button');
    closeButton.textContent = "X";
    let text = document.createElement('h1');
    text.textContent = planet_name + "  residents: \n";
    divContent.appendChild(closeButton);
    divContent.appendChild(text);
    divContent.appendChild(table);
    divModal.appendChild(divContent);

    const modal = document.querySelector('body>.modal');
    if (!!modal){
        document.body.replaceChild(divModal, modal);
    } else {
      document.body.appendChild(divModal);
    }
}


function showModal(modal) {
    modal.classList.toggle("show-modal");
}


function hideModal() {
    const modal = document.querySelector(".modal");
    modal.classList.remove("show-modal");
    const clickedButton = document.querySelector(".clicked");
    clickedButton.classList.remove("clicked");
}


export function onClickResponse(){
    this.classList.add("clicked");
    const planet_name = getClickedPlanetName();
    getPlanetResidentsTableData(planet_name);
    // createPopupModal(tableDataDeepCopy);
    // const modal = document.querySelector(".modal");
    // showModal(modal);
    // const closeButton = document.querySelector(".close-button");
    // closeButton.addEventListener("click", hideModal);
}