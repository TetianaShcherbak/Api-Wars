export function setViewResidentsButton(){
   const residentsColumnIndex = getResidentsColumnIndex();
   const table = document.getElementById("table");
   const tbody = table.children[1];
   for (const tr of tbody.children){
       let columnNumber = 0;
       for (const th of tr.children){
           if (columnNumber === residentsColumnIndex){
               setButtonForNotNonCell(th);
           }
           columnNumber ++;
       }
   }
}


function setButtonForNotNonCell(cell){
    let cellContent = cell.innerText;

    if (cellContent !== 'No known residents'){
       let viewResidentsButton = document.createElement('button');
       viewResidentsButton.classList.add('trigger')
       viewResidentsButton.addEventListener("click", onClickResponse);
       viewResidentsButton.textContent = cellContent;
       cell.replaceWith(viewResidentsButton);
    }
}


function getResidentsColumnIndex(){
     let residentsColumnIndex = 0;
    const table = document.getElementById("table");
    const thead = table.children[0];
    
    for (const tr of thead.children){
        let columnIndex = 0;
        for (const th of tr.children){
            if (th.innerHTML === 'Residents'){
                residentsColumnIndex = columnIndex;
                return residentsColumnIndex;
            }
            columnIndex ++;
        }
    }
}


function onClickResponse(){
    createPopupModel();
    const modal = document.querySelector(".modal");
    showModal(modal);
    const closeButton = document.querySelector(".close-button");
    closeButton.addEventListener("click", hideModal);
}


function createPopupModel(){
    let divModel = document.createElement('div');
    divModel.classList.add('modal');
    let divContent = document.createElement('div');
    divContent.classList.add('modal-content');
    let closeButton = document.createElement('span');
    closeButton.classList.add('close-button');
    closeButton.textContent = "X";
    let text = document.createElement('h1');
    text.textContent = "Hello, I am a modal!";
    divContent.appendChild(closeButton);
    divContent.appendChild(text);
    divModel.appendChild(divContent);
    document.body.appendChild(divModel);
}


function showModal(modal) {
    modal.classList.toggle("show-modal");
}


function hideModal() {
    const modal = document.querySelector(".modal");
    modal.classList.remove("show-modal");
}
