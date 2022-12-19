function total(){
    let valorInt = document.querySelector('#qt_inteira').value;
    let valorMeia = document.querySelector('#qt_meia').value;

    let valorTotal = (parseInt(valorInt)*15.0)+(parseInt(valorMeia)*7.50);
    console.log(valorTotal);
    document.querySelector('.valor-total').innerHTML = `R$ ${valorTotal.toFixed(2)}`;
}