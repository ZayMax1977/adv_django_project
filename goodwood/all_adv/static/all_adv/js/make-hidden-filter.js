//function show_filter(e){
//    document.getElementById(e).hidden = false;
//    document.getElementById('curve-up').hidden = false;
//    document.getElementById('curve-down').hidden = true;
//
//}

//function hidden_filter(e):{
//    document.getElementById(e).hidden = true;
//    document.getElementById('curve-up').hidden = true;
//    document.getElementById('curve-down').hidden = false;
//}

function show_filter(e, down, up){
    let el_1 = document.getElementById(e);
    if (el_1.hidden == true){
        el_1.hidden = false;
        document.getElementById(up).hidden = false;
        document.getElementById(down).hidden = true;
    }else{
         el_1.hidden = true;
        document.getElementById(up).hidden = true;
        document.getElementById(down).hidden = false;
    }
    }

