const showPassword = document.querySelector('.show-password');
const messageToast = new bootstrap.Toast('.toast');
const btnCopy = document.querySelector('.btn-copy');

btnCopy.addEventListener('click', () =>{
    let password = showPassword.innerText;
    navigator.clipboard.writeText(password)
    messageToast.show()
})