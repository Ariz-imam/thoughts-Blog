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

    resetRequest_form = document.getElementById('resetRequest-form');
    
    resetRequest_form.addEventListener('submit', function(event){
        httpRequest = new XMLHttpRequest(); // ajax object

        form_data = new FormData(resetRequest_form);

        httpRequest.addEventListener('load', resetRequestResult); // when request complete successfully

        httpRequest.addEventListener('error', errorResult); // when request terminates with error

        httpRequest.open('POST', '/reset_request');

        httpRequest.send(form_data);
        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

    resetPassword_form = document.getElementById('resetPassword-form');
    
    resetPassword_form.addEventListener('submit', function(event){
        httpRequest = new XMLHttpRequest(); // ajax object

        form_data = new FormData(resetPassword_form);

        httpRequest.addEventListener('load', resetPasswordResult); // when request complete successfully

        httpRequest.addEventListener('error', errorResult); // when request terminates with error

        httpRequest.open('POST', '/reset_password');

        httpRequest.send(form_data);
        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

    delete_account = document.getElementById('delete-account-button')

    delete_account.addEventListener('click', function(event){
        httpRequest = new XMLHttpRequest(); // ajax object

        httpRequest.addEventListener('load', deleteResult); // on load

        httpRequest.addEventListener('error', errorResult); // on error

        httpRequest.open('GET', `/delete_account/${user_id}`);

        httpRequest.send();

        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    })

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
        location.reload();
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
        location.reload();
    }
}

let resetRequestResult = function(event){
    document.getElementById('loading').style.display = 'none';

    let response = JSON.parse(event.target.responseText);

    if (response.success){
        alert(response.message);
        window.location.href = "/";
    }else{
        alert(response.message);
        location.reload();
    }
};

let resetPasswordResult = function(event){
    document.getElementById('loading').style.display = 'none';

    let response = JSON.parse(event.target.responseText);

    if (response.success){
        alert(response.message);
        window.location.href = "/dashboard/";
    }else{
        alert(response.message);
        window.location.href = "#resetPassword-form";
    }
};

let deleteResult = function(event){
    document.getElementById('loading').style.display = 'none';

    let response = JSON.parse(event.target.responseText);

    if(response.success){
        alert(response.message);
        window.location.href = '/';
    }else{
        alert(response.message);
        location.reload();
    }
}

let errorResult = function(event){
    document.getElementById('loading').style.display = 'none';

    alert('SomeThing Went Wrong');
    location.reload();
}