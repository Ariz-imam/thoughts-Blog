window.addEventListener('load', function(){
    query_form = document.getElementById('query-form');

    query_form.addEventListener('submit', function(event){
        httpRequest = new XMLHttpRequest(); // ajax object

        form_data = new FormData(query_form);

        httpRequest.addEventListener('load', queryResult); // when request complete successfully

        httpRequest.addEventListener('error', queryError); // when request terminates with error

        httpRequest.open('POST', '/askQuery');

        httpRequest.send(form_data);
        document.getElementById('loading').style.display = 'block';
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
}

let queryError = function(){
    alert('Ooops! SomeThing went wrong');
    location.reload();
}