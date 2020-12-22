$(document).ready(function(){

    $("#submit").click(function(){

        let today = new Date();
        let dd = String(today.getDate()).padStart(2, '0');
        let mm = String(today.getMonth() + 1).padStart(2, '0');
        let yyyy = today.getFullYear();
        let time = today.getTime();

        today = mm + '/' + dd + '/' + yyyy;

//        console.log(today);

//        console.log($("#memo").val());


        $.post("/input",
        {
            memo: $("#memo").val(),
            amount: $("#amount").val(),
            date: today,
            userHash: window.location.pathname.split('/')[2],
            view: window.location.pathname.split('/')[3],
            time: time
        },
        function(data){
            data = data[0].data;
//            window.location.replace("/input/"+data[0]+'/'+data[1]);
            console.log(data);
            window.location.replace(data);
        });

    });

});