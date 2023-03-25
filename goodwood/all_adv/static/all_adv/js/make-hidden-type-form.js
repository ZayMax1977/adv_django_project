let list_forms = ['form_common','form_for_realty','form_for_car',
'form_for_meetting','form_for_job']



function hidden_block(e){
    for (let i of list_forms) {
        if (i == e){
            let elem = document.getElementById(e);
            elem.hidden = false;
        }else{
            let element = document.getElementById(i);
            element.hidden = true;
        }
    }
}

