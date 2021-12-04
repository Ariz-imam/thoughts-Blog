window.addEventListener('load', function(){
    let signup_form = document.getElementById("signup-form");
    signup_form.addEventListener('submit', function(event){
        
        // declaring ajax object
        let httpRequest = new XMLHttpRequest();

        // fetching form data
        let form_data = new FormData(signup_form);

        httpRequest.addEventListener('load', signupResult);

        httpRequest.addEventListener('error', errorResult);

        httpRequest.open('POST', "/signup");

        httpRequest.send(form_data);

        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

    let login_form = document.getElementById('login-form');
    login_form.addEventListener('submit', function(event){
        let httpRequest = new XMLHttpRequest();

        let form_data = new FormData(login_form);

        httpRequest.addEventListener('load', loginResult);

        httpRequest.addEventListener('error', errorResult);

        httpRequest.open('POST', '/login');

        httpRequest.send(form_data);

        document.getElementById("loading").style.display = 'block';
        event.preventDefault();
    });

});

let signupResult = function(event){
    document.getElementById('loading').style.display = 'none';

    let response = JSON.parse(event.target.responseText);

    if(response.success){
        alert(response.message);
        location.reload();
    }else{
        alert(response.message);
    }
}

let loginResult = function(event){
    document.getElementById('loading').style.display = 'none';

    let response = JSON.parse(event.target.responseText);

    if(response.success){
        alert(response.message);
        location.reload();
    }else{
        alert(response.message);
    }
}

let errorResult = function(event){
    document.getElementById('loading').style.display = 'none';

    alert('SomeThing Went Wrong');
    location.reload();
}