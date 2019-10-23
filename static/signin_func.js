$(document).ready(function() {
    var cont_btn = $("#continue_btn");
    var username_area = $("#username_area")
    var password_area = $("#password_area")
    password_area.hide()

    var signin_btn = $("#signin_btn")

    var username = $("#username_input")
    username.focus()
    var password = $("#password_input")

    var createAccountBtn = $("#createAccountBtn")



    createAccountBtn.click(function(){
        window.location = "/createAccount"
    })


    cont_btn.click(function() {
        username_area.hide()
        password_area.show()
        password.focus()
    })
    username.keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);

        if(keycode == '13'){
            username_area.hide()
            password_area.show()
            password.focus()	
        }
    })

    signin_btn.click(function() {
        // alert("Signed in. Redirecting to Home Page.")
        login()
    })
    password.keypress(function(event){
	
        var keycode = (event.keyCode ? event.keyCode : event.which);

        if(keycode == '13'){
            login()	
        }
    
    });

    function login() {
        window.location.href = "/";
    }
});