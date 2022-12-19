var btn = document.querySelector('#QUA');
var info_filme = document.querySelector('.info_filme');
var info_filme2 = document.querySelector('.info_filme2');
var info_filme3 = document.querySelector('.info_filme3');

btn.addEventListener('click', function(){

    if(info_filme.style.display === 'none'){
        info_filme.style.display = 'none'
        info_filme2.style.display = 'none'
        info_filme3.style.display = 'inline-block'
    }else {
        info_filme3.style.display = 'inline-block'
        info_filme.style.display = 'none'
        info_filme2.style.display = 'none'
    }

});
