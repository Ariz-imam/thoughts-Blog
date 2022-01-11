window.addEventListener('load', function(){
    let yourQueries = document.getElementById('yourQueries');
    yourQueries.addEventListener('click', function(event){

        httpRequest = new XMLHttpRequest();

        httpRequest.addEventListener('load', getQueries);

        httpRequest.addEventListener('error', on_error);

        httpRequest.open('GET', '/yourQueries', true);

        httpRequest.send();

        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

    let yourAnswers = document.getElementById('yourAnswers');
    yourAnswers.addEventListener('click', function(event){

        httpRequest = new XMLHttpRequest();

        httpRequest.addEventListener('load', getAnswers);

        httpRequest.addEventListener('error', on_error);

        httpRequest.open('GET', '/yourAnswers', true);

        httpRequest.send();

        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

});


let getQueries = function(event){
    document.getElementById('loading').style.display = 'none';

    let list = document.getElementById('list');

    resArr = JSON.parse(event.target.responseText);
    console.log(resArr);
    let str = "";
    for (let response of resArr){
            str += `<li class="list-group-item">
                        <h3>${response.description}</h3>
                        <h5 class="text-muted">${response.title}</h5>  
                        <em class="">${response.posted_on.slice(0, 16)}</em>
                        <div class="float-right">
                        <a href="/edit/ques/${response.sno}" class="btn rounded-circle"><i class="far fa-edit"></i></a>
                        <a href="/delete/ques/${response.sno}"  class="btn  rounded-circle"><i class="fas fa-trash-alt"></i></a>
                        </div>
                    </li>`;
            list.innerHTML = str;
    }

}

let getAnswers = function(event){
    document.getElementById('loading').style.display = 'none';

    let list = document.getElementById('list');

    resArr = JSON.parse(event.target.responseText);

    let str = "";
    for (let response of resArr){
        
        str += `<li class="list-group-item">
                    <h3>${response.description}</h3>
                    <h5 class="text-muted">${response.title}</h5>  
                    <em class="">${response.posted_on.slice(0, 16)}</em>
                    <hr/>
                    ${response.answer}
                    <div class="float-right">
                    <a href="/edit/ans/${response.sno}" class="btn  rounded-circle"><i class="far fa-edit"></i></a>
                    <a href="/delete/ans/${response.sno}" class="btn  rounded-circle"><i class="fas fa-trash-alt"></i></a>
                    </div>
                </li>`;
        list.innerHTML = str;
    }

}

let on_error = function(event){
    alert('Something Went wrong');
    location.reload();
}