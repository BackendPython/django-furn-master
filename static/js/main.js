let logout_button = document.querySelector('.logout-navbar')
let block_content = document.querySelector('.block-content')
let logout_coniform = document.querySelector('.logout-coniform')
console.log(logout_coniform);

logout_button.addEventListener('click', function(){
    logout_coniform.ariaPressed = true
    logout_coniform.ariaSelected = true
    logout_coniform.style.display = 'block'
    block_content.style.opacity = '0.3'
})
setInterval(() => {
    console.log(logout_coniform);
}, 2000);