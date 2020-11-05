$(document).ready(function () {
    $(document).ready(function(){
        $("#hero2").hide();
        $("#errorFullName").hide();
        $("#errorEmailAddress").hide();
        $("#errorJob").hide();
        $("#errorGender").hide();
        $("#errorPassword").hide();
        $("#errorVerifyPassword").hide();

        $("#errorEmailAddressLogin").hide();

        var errorFullName = false;
        var errorEmailAddress = false;
        var errorJob = false;
        var errorGender = false;
        var errorPassword = false;
        var errorVerifyPassword = false;

        var errorEmailAddressLogin = false;


        $("#fullName").focusout(function (){
            checkFullName();
        });

        $("#emailAddress").focusout(function (){
            checkEmailAddress();
        });

        $("#job").focusout(function (){
            checkJob();
        });

        $("#password").focusout(function (){
            checkPassword();
        });

        $("#verifyPassword").focusout(function (){
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

        /*---------------------------------------------------------------------*/
        function checkJob(){
            var expRegJob = new RegExp(/([a-zA-Z]+)/i);

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
        /*---------------------------------------------------------------------*/

        function checkPassword(){
            var passwordLength = $("#password").val().length;

            if(passwordLength<8){
                $("#errorPassword").show();
                errorPassword = true;
                $("#password").addClass("is-invalid");
            }
            else{
                $("#errorPassword").hide();
                $("#password").removeClass("is-invalid");
            }
        }
        function checkVerifyPassword(){
            var passwordValue = $("#password").val();
            var verifyPasswordValue = $("#verifyPassword").val();

            if(passwordValue != verifyPasswordValue){
                $("#errorVerifyPassword").show();
                errorVerifyPassword = true;
                $("#verifyPassword").addClass("is-invalid");
            }
            else{
                $("#errorVerifyPassword").hide();
                $("#verifyPassword").removeClass("is-invalid");
            }
        }

        function checkEmailAddressLogin(){
            var expRegEmail = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);

            if(!(expRegEmail.test($("#emailAddressLogin").val()))){
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