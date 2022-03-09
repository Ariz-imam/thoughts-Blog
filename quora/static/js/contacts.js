
window.addEventListener('load', function(){
    contact_form = document.getElementById('contactForm');
    
    contact_form.addEventListener('submit', function(event){
        httpRequest = new XMLHttpRequest(); // ajax object

        form_data = new FormData(contact_form);

        httpRequest.addEventListener('load', contactResult); // when request complete successfully

        httpRequest.addEventListener('error', contactError); // when request terminates with error

        httpRequest.open('POST', '/contact');

        httpRequest.send(form_data);
        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

});

let contactResult = function(event){
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

let contactError = function(event){
    document.getElementById('loading').style.display = 'none';

    alert('SomeThing Went Wrong');
    location.reload();
}