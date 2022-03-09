
window.addEventListener('load', function(){
    let yourQueries = document.getElementById('yourQueries');
    yourQueries.addEventListener('click', function(event){

        httpRequest = new XMLHttpRequest();

        httpRequest.addEventListener('load', getQueries);

        httpRequest.addEventListener('error', on_error);

        httpRequest.open('GET', `/viewProfileGetQueries/${id}`, true);

        httpRequest.send();

        document.getElementById('loading').style.display = 'block';
        event.preventDefault();
    });

    let yourAnswers = document.getElementById('yourAnswers');
    yourAnswers.addEventListener('click', function(event){

        httpRequest = new XMLHttpRequest();

        httpRequest.addEventListener('load', getAnswers);

        httpRequest.addEventListener('error', on_error);

        httpRequest.open('GET', `/viewProfileGetAnswers/${id}`, true);

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
                        <a href="/answer/ques=${response.id}">
                            <h3 class="post-title">${response.description}</h3>
                        </a>
                        <h5 class="text-muted">${response.title}</h5>  
                        <em class="">${response.posted_on.slice(0, 16)}</em>
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
                    <a href="/answer/ques=${response.id}">
                        <h3 class="post-title">${response.description}</h3>
                    </a>
                    <h5 class="text-muted">${response.title}</h5>  
                    <em class="">${response.posted_on.slice(0, 16)}</em>
                    <hr/>
                    ${response.answer}
                </li>`;
        list.innerHTML = str;
    }

}

let on_error = function(event){
    alert('Something Went wrong');
    location.reload();
}