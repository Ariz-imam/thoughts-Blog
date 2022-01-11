window.addEventListener('load', function(){
    query_form = document.getElementById('query-form');
    
    query_form.addEventListener('submit', function(event){
        httpRequest = new XMLHttpRequest(); // ajax object

        form_data = new FormData(query_form);

        httpRequest.addEventListener('load', queryResult); // when request complete successfully

        httpRequest.addEventListener('error', errorResult); // when request terminates with error

        httpRequest.open('POST', '/askQuery');

        httpRequest.send(form_data);
        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });


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

let queryResult = function(event){
    document.getElementById('loading').style.display = 'none';

    let response = JSON.parse(event.target.responseText);

    if (response.success){
        alert(response.message);
        location.reload();
    }else{
        alert(response.message);
        location.reload();
    }
};

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
        window.location.href = "/dashboard";
    }else{
        alert(response.message);
    }
}

let errorResult = function(event){
    document.getElementById('loading').style.display = 'none';

    alert('SomeThing Went Wrong');
    location.reload();
}