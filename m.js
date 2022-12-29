function increment1()
{
    var value = parseInt(document.getElementById('number1').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value<10){
        value++;
            document.getElementById('number1').value = value;
    }
}
function decrement1()
{
    var value = parseInt(document.getElementById('number1').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value>1){
        value--;
            document.getElementById('number1').value = value;
    }

}
function increment2()
{
    var value = parseInt(document.getElementById('number2').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value<10){
        value++;
            document.getElementById('number2').value = value;
    }
}
function decrement2()
{
    var value = parseInt(document.getElementById('number2').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value>1){
        value--;
            document.getElementById('number2').value = value;
    }

}
function increment3()
{
    var value = parseInt(document.getElementById('number3').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value<10){
        value++;
            document.getElementById('number3').value = value;
    }
}
function decrement3()
{
    var value = parseInt(document.getElementById('number3').value, 10);
    value = isNaN(value) ? 0 : value;
    if(value>1){
        value--;
            document.getElementById('number3').value = value;
    }

}