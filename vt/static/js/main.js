const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

timeout = 3000

setTimeout(function(){
    $('#message').fadeOut('slow');
}, timeout);