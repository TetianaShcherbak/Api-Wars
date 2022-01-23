const previousPageButton = document.getElementById('prev_page_btn');
const nextPageButton = document.getElementById('next_page_btn');


export function addResponseOnClick(){
    previousPageButton.addEventListener('click',goToPreviousPage);
    previousPageButton.addEventListener('dblclick',goToPreviousPage);
    nextPageButton.addEventListener('click',goToNextPage);
    nextPageButton.addEventListener('dblclick',goToNextPage);
}



function goToPreviousPage(){
    const url = window.location.href;
    const currentPage = getCurrentPage();
    const previousPage = (currentPage > 1) ? (currentPage - 1) : 1;

    window.location.href = url.slice(0,-1) + previousPage;
}


function goToNextPage(){
    const url = window.location.href;
    const currentPage = getCurrentPage();
    const nextPage = (currentPage > 7) ? 7 : (currentPage + 1);

    try{
        window.location.href = url.slice(0,-1) + nextPage;
    }
    catch(err){
        window.location.href = url.slice(0,-1) + "/page/"+ nextPage;
    }
}


function getCurrentPage(){
    const url = window.location.href;
    const lastUrlChar = String(url).slice(-1);
    const currentPage = lastUrlChar === '/' ? 1 : lastUrlChar;

    return parseInt(currentPage);
}
