function formal(){
    var formal_button = document.getElementById('fb');
    var form = document.getElementById('form');
    var dd = document.getElementById('b_class');
    formal_button.parentNode.removeChild(formal_button);
    var loding_gif = document.createElement('img');
    loding_gif.src = "/static/loading.gif";
    loding_gif.style = 'width: 65px;height:70px;';
    dd.appendChild(loding_gif);
    form.submit();
}
