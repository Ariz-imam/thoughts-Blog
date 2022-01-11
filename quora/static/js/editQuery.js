
window.onload = () => {

    editQquery_form = document.getElementById('editQquery-form');
    editQquery_form.addEventListener('submit', function(event){
        httpRequest = new XMLHttpRequest(); // ajax object
        console.log(id);
        form_data = new FormData(editQquery_form);
        
        httpRequest.addEventListener('load', editResult); // when request complete successfully
        
        httpRequest.addEventListener('error', on_error); // when request terminates with error
        
        httpRequest.open('POST', `/edit/ques/${id}`);
        
        httpRequest.send(form_data);
        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

}

    

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

