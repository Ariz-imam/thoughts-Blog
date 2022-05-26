window.addEventListener('load', function(){

    let update_form = document.getElementById("update-form");

    update_form.addEventListener('submit', function(event){
        let httpRequest = new XMLHttpRequest();

        let form_data = new FormData(update_form);

        httpRequest.addEventListener('load', editResult);

        httpRequest.addEventListener('error', on_error);

        httpRequest.open('POST', '/editProfile');

        httpRequest.send(form_data);

        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });
});

let editResult = event =>{
    document.getElementById('loading').style.display = 'none';

    let response = JSON.parse(event.target.responseText);

    if (response.success){
        alert(response.message);
        window.location.href = "/dashboard/";
    }else{
        alert(response.message);
        location.reload();
    }
};

let on_error = function(){
    alert('Ooops! SomeThing went wrong');
    location.reload();
};