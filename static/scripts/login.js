$(document).ready(function(){

    $("#submit").click(function(){

        let user = $("#user").val();
        let pass = $("#pass").val();

        $.post("/login",
            {
                user: user,
                pass: pass
            },
            function(data){

                user = data[0].data;
                if(user.length == 0)
                {
                    $(".login").css("background-color","rgb(255, 225, 225)");
                    $("#error").html("Wrong username or password").fadeOut(2000,function(){
                        $(this).html("");
                        $(this).show();
                        $(".login").css("background-color", "white");
                    });
                }
                else
                {
                    window.location.replace("/feed/"+data[0].hash+"/0");
                }
            }
        );

    });
});