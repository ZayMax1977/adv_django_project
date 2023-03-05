function two_btn(e,state){
    var el = document.getElementById('name_state');
    var w = document.getElementById(e);
    el.innerText = state;
    w.style.color = '#15FC0A';
}

function return_color(e){
    var w = document.getElementById(e);
    var el = document.getElementById('name_state');
    el.innerText = 'Россия';
    w.style.color = '';
}


function color_state(e){
    var el = document.getElementById(e);
    el.style.fill = '#15FC0A';
}
function color_back(e){
    var el = document.getElementById(e);
    el.style.fill = '';
}
 
function get_state(id){
    var form =  document.getElementsByName('formochka');
    var w = document.getElementById(id).textContent;
    
    var q = document.getElementById('hidden-input');
    q.value = w;
    console.log(w)
    

    
    form[0].submit();
    
}