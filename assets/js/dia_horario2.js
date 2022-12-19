var btn = document.querySelector('#TER');
var info_filme = document.querySelector('.info_filme');
var info_filme2 = document.querySelector('.info_filme2');
var info_filme3 = document.querySelector('.info_filme3');

btn.addEventListener('click', function(){

    if(info_filme.style.display === 'inline-block'){
        info_filme.style.display = 'none'
        info_filme2.style.display = 'inline-block'
        info_filme3.style.display = 'none'

    }else {
        info_filme2.style.display = 'inline-block'
        info_filme.style.display = 'none'
        info_filme3.style.display = 'none'
        
    }

});
