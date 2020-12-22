$(document).ready(function(){

    $("button").each(function(){

        if($(this).html() == window.location.pathname.split('/')[3])
        {
            $(this).css("background-color", "red");
        }

    });

    $(".button").click(function(){

        let page = $(this).html();
        if($(this).html() == window.location.pathname.split('/')[3])
        {
            return;
        }
        else
        {
            let hash = window.location.pathname.split('/')[2];
            window.location.replace("/feed/"+hash+'/'+page)
        }
    });
});