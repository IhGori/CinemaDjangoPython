var btn = document.querySelector('#type');
var option_type = document.querySelector('.option_type');
var option_payment = document.querySelector('.option_payment');




btn.addEventListener('click', function(){

    if(option_type.style.display === 'none'){
        option_type.style.display = 'inline-block'
        option_payment.style.display = 'none'
        
       

    }else {
        option_type.style.display = 'inline-block'
        option_payment.style.display = 'none'
        
        
    }

});
