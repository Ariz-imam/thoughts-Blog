
window.addEventListener('load', function(){

    resetPasswordToken_form = document.getElementById('resetPasswordToken-form');
    
    resetPasswordToken_form.addEventListener('submit', function(event){
        httpRequest = new XMLHttpRequest(); // ajax object

        form_data = new FormData(resetPasswordToken_form);

        httpRequest.addEventListener('load', resetPasswordTokenResult); // when request complete successfully

        httpRequest.addEventListener('error', resetPasswordError); // when request terminates with error

        httpRequest.open('POST', `/reset_password/${token}`);

        httpRequest.send(form_data);
        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

});

let resetPasswordTokenResult = function(event){
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

let resetPasswordError = function(event){
    document.getElementById('loading').style.display = 'none';

    alert('SomeThing Went Wrong');
    location.reload();
}