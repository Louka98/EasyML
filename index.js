$(document).ready(function () {
    $(document).ready(function(){
        $("#hero2").hide();
        $("#errorFullName").hide();
        $("#errorUserName").hide();
        $("#errorEmailAddress").hide();
        $("#errorGender").hide();
        $("#errorPassword").hide();
        $("#errorVerifyPassword").hide();
        $("#errorEmailAddressLogin").hide();

        var errorFullName = false;
        var errorUserName = false;
        var errorEmailAddress = false;
        var errorGender = false;
        var errorPassword = false;
        var errorVerifyPassword = false;

        var errorEmailAddressLogin = false;


        $("#fullName").focusout(function (){
            checkFullName();
        });

        $("#usernameRegister").focusout(function (){
            checkUserName();
        });

        $("#emailAddress").focusout(function (){
            checkEmailAddress();
        });

        $("#job").focusout(function (){
            checkJob();
        });

        $("#passwordRegister").focusout(function (){
            checkPassword();
        });

        $("#verifyPasswordRegister").focusout(function (){
            checkVerifyPassword();
        });

        $("#emailAddressLogin").focusout(function (){
            checkEmailAddressLogin();
        });

        $("#buttonSignUp").click(function (){
            var selectGender = $("input[name='gender']:checked").val();
            if(selectGender){
                $("#errorGender").hide();
            }
            else{
                $("#errorGender").show();
                errorGender = true;
            }
        });

        function checkFullName(){
            var fullNameLength = $("#fullName").val().length;

            if(fullNameLength<5 || fullNameLength>31){
                $("#errorFullName").show();
                errorFullName = true;
                $("#fullName").addClass("is-invalid");
            }
            else{
                $("#errorFullName").hide();
                $("#fullName").removeClass("is-invalid");
            }
        }

        function checkUserName(){
            var fullNameLength = $("#usernameRegister").val().length;

            var expRegUserName = new RegExp(/^[a-zA-Z0-9]{4,15}$/i);

            if(!(expRegUserName.test($("#usernameRegister").val()))){
                $("#errorUserName").show();
                errorUserName = true;
                $("#usernameRegister").addClass("is-invalid");
            }
            else{
                $("#errorUserName").hide();
                $("#usernameRegister").removeClass("is-invalid");
            }
        }

        function checkEmailAddress(){
            var expRegEmail = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);

            if(!(expRegEmail.test($("#emailAddress").val()))){
                $("#errorEmailAddress").show();
                errorEmailAddress = true;
                $("#emailAddress").addClass("is-invalid");
            }
            else{
                $("#errorEmailAddress").hide();
                $("#emailAddress").removeClass("is-invalid");
            }
        }


        function checkJob(){
            var expRegJob = new RegExp(/^[a-zA-Z0-9]{4,20}$/i);

            if(!(expRegJob.test($("#job").val()))){
                $("#errorJob").show();
                errorJob = true;
                $("#job").addClass("is-invalid");
            }
            else{
                $("#errorJob").hide();
                $("#job").removeClass("is-invalid");
            }
        }


        function checkPassword(){
            var passwordLength = $("#passwordRegister").val().length;

            if(passwordLength<8){
                $("#errorPassword").show();
                errorPassword = true;
                $("#passwordRegister").addClass("is-invalid");
            }
            else{
                $("#errorPassword").hide();
                $("#passwordRegister").removeClass("is-invalid");
            }
        }
        function checkVerifyPassword(){
            var passwordValue = $("#passwordRegister").val();
            var verifyPasswordValue = $("#verifyPasswordRegister").val();

            if(passwordValue != verifyPasswordValue){
                $("#errorVerifyPassword").show();
                errorVerifyPassword = true;
                $("#verifyPasswordRegister").addClass("is-invalid");
            }
            else{
                $("#errorVerifyPassword").hide();
                $("#verifyPasswordRegister").removeClass("is-invalid");
            }
        }

        function checkEmailAddresUserNamesLogin(){
            var expRegEmailUserName = new RegExp(/^[a-zA-Z0-9]{4,15}$/i);

            if(!(expRegEmailUserName.test($("#emailAddressLogin").val()))){
                $("#errorEmailAddressLogin").show();
                errorEmailAddressLogin = true;
                $("#emailAddressLogin").addClass("is-invalid");
            }
            else{
                $("#errorEmailAddressLogin").hide();
                $("#emailAddressLogin").removeClass("is-invalid");
            }
        }
    });

    function checkEmailAddressLogin(){
        var expRegEmail = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);

        if(!(expRegEmail.test($("#emailAddressLogin").val()))){
            $("#errorEmailAddressLogin").show();
            errorEmailAddress = true;
            $("#emailAddressLogin").addClass("is-invalid");
        }
        else{
            $("#errorEmailAddressLogin").hide();
            $("#emailAddressLogin").removeClass("is-invalid");
        }
    }

    //nav function -----------------------------------------------------------------------------------------------------

    //scrolling for links
    $(".menuLink").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 2500, function () {
                window.location.hash = hash;
            });
        }
    });

    //scrolling for button
    $("#signUpButton").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 2000, function () {
                window.location.hash = hash;
            });
        }
    });


    //login function ---------------------------------------------------------------------------------------------------
    //display to login function
    $("#login1").on('click', function () {
        $("#hero1").hide(1500);
        $("#hero2").show(1500);
        $("#hero2").removeAttr("data-aos");
    });

    //check login input function
    //   $("p").hide();
    /*
    * $("button").click(function(){
    $("p").hide(1000);
  });*/
    //check signup function --------------------------------------------------------------------------------------------
    //check send function ----------------------------------------------------------------------------------------------

    $("#loginForm").validate();
    $("#SignUpForm").validate();


});


//animation
AOS.init({
    duration: 2500,
})

$(function(){
    $('#loginForm').submit(function() {
        var settings = {
            "url": "http://127.0.0.1:5000/login",
            "method": "GET",
            "timeout": 0,
            "headers": {
                "Authorization": "Basic " + btoa(document.getElementById("usernameLogin").value+":"+document.getElementById("passwordLogin").value)
            },
        };

        $.ajax(settings).done(function (response) {
            localStorage.setItem("token",response.token)
            window.location.href = "algorithms.html"
        });

        event.preventDefault();
    });

    $('#signUpForm').submit(function() {

        if($("#verifyPasswordRegister")[0].classList[2]=="is-invalid" || $("#passwordRegister")[0].classList[2]=="is-invalid" || $("#usernameRegister")[0].classList[2]=="is-invalid") {
            event.preventDefault();
            return
        }

        var settings = {
            "url": "http://127.0.0.1:5000/register",
            "method": "GET",
            "timeout": 0,
            "headers": {
                "Authorization": "Basic " + btoa(document.getElementById("usernameRegister").value+":"+document.getElementById("passwordRegister").value)
            },
        };

        $.ajax(settings).done(function (response) {
            localStorage.setItem("token",response.token)
            window.location.href = "algorithms.html"
        });

        event.preventDefault();
    });
});