// validating form submission for demographic data
// TODO: debug
function validate_demographics(){
    var x = document.forms.demographics.gender.value;
    if (x == null){
        alert("Please select a gender.");
        return false;
    }
    
    var y = document.forms.demographics.age.value;
    if(y == null){
        alert("Please select an age group.");
        return false;
    }
    return true;
}


// AJAX to update side bar of demographics as user clicks through
function demographics_update(){
    var xmlhttp;
    
    if (str==""){
        document.getElementById("brochure").inner.HTML="";
        return
    }
    
    if (window.XMLHttpRequest){ // for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else{ // for IE5/6
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    
    xmlhttp.onreadystatechange=function(){
        if (xmlhttp.readyState==4 && xmlhttp.status==200){
            document.getElementById("brochure").innerHTML=xmlhttp.responseText;
        }
    }
    
    xmlhttp.open("POST","details.py",true);
    xmlhttp.send();
}