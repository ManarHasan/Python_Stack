function validateForm() {
    var fname = document.forms["register"]["fname"].value, lname = document.forms["register"]["lname"].value, email = document.forms["register"]["email"].value, birthday = document.forms["register"]["date"].value, password = document.forms["register"]["date"].value, confirm = document.forms["register"]["date"].value;
    var pattern = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    var errors = [];
    // var today = new Date()
    // if (fname.length < 2) {
    // alert("First Name is too short go to court and change it");
    // return false;
    // }
    // if(lname.length < 2){
    //     alert("Last Name is too short go to court and change it")
    //     return false;
    // }
    // if(email.match(pattern)[0] != email){
    //     alert("Incorrect email format")
    //     return false;
    // }
    // if(today.getFullYear() - parseInt(birthday.substr(0, 4) < 13)){
    //     alert("You are too young!")
    //     return false;
    // }
    if (fname.length == 0) {
        errors.push("First Name is required");
    }
    if(lname.length == 0){
        errors.push("Last Name is required");
    }
    if(email.length == 0){
        errors.push("Email is required");
    }
    if(birthday.length == 0){
        errors.push("Birthday is required");
    }
    if(password.length == 0){
        errors.push("Password is required");
    }
    if(confirm.length == 0){
        errors.push("Confirm your password");
    }
    console.log(errors)
    for(var i=0; i<errors.length;i++){
        var para = document.createElement("p");
        var node = document.createTextNode(errors[i]);
        para.appendChild(node);
        var element = document.getElementById("errors");
        element.appendChild(para);
    // document.getElementById('errors').innerHTML += "<p>" ++ errors[i] ++ "</p>";
    }
    if (errors.length > 0){
        return false;
    }
}