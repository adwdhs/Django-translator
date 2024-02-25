const fromField=document.querySelector('#fromField');
const toField=document.querySelector('.result')
fromField.addEventListener('keyup', (e) => {


    let usernameVal=e.target.value;
    console.log('111',usernameVal);

    const qw = document.querySelector( 'small' ).textContent;
    console.log('111', qw);
    usernameVal = qw + ' ' + usernameVal;
    console.log(usernameVal);

    if (usernameVal.length > -10){
        fetch("http://127.0.0.1:8000/text",{
                body: JSON.stringify(usernameVal),
                method: 'post',

                })
                .then(response => response.json())
                .then(data => {
                console.log('data', data);
                toField.innerHTML= `<h6>${data.translation}<h6>`;
                });

        }
});


