let logout_button = document.querySelector('.logout-navbar')
let block_content = document.querySelector('.block-content')
let logout_coniform = document.querySelector('.logout-coniform')

logout_button.addEventListener('click', function(){
    logout_coniform.style.display = 'block'
    block_content.style.mixBlendMode = 'darken'
})