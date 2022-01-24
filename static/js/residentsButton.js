import {onClickResponse} from "./popupResponseOnResidentsButton.js";


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


function getResidentsColumnIndex(columnName='Residents'){
     let residentsColumnIndex = 0;
    const table = document.getElementById("table");
    const thead = table.children[0];
    
    for (const tr of thead.children){
        let columnIndex = 0;
        for (const th of tr.children){
            if (th.innerHTML === columnName){
                residentsColumnIndex = columnIndex;
                return residentsColumnIndex;
            }
            columnIndex ++;
        }
    }
}


