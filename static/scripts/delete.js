$(document).ready(function(){

    $(".delete").click(function(){

        let inputHash = $(this).parent().attr('id');

        if(!confirm("Are you sure you want to delete?"))
        {
            return;
        }

        $.post("/delete/"+inputHash,
        {

        },
        function(data){

            console.log(data);
            location.reload();
            console.log($(".card").length);
            if($(".card").length == 1 && window.location.pathname.split('/')[3] != '0')
            {
                let location = window.location.pathname.split('/');
                location[3] = (parseInt(location[3]) - 1).toString(10);
                window.location.replace(location.join("/"));
            }

        });

    });

});