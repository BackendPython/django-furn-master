let logout_button = document.querySelector('.logout-navbar')
let block_content = document.querySelector('.block-content')
let logout_coniform = document.querySelector('.logout-coniform')
let openModal = false

logout_button.addEventListener('click', function(){
    setTimeout(() => {
        openModal = true
        document.body.style.overflow = 'hidden'
    }, 100);
    logout_coniform.style.display = 'block'
    block_content.style.opacity = '0.3'
    block_content.addEventListener('click', function(){
        if (openModal==true) {
            openModal = false
            logout_coniform.style.display = 'none'
            block_content.style.opacity = '1'
            document.body.style.overflow = 'scroll'
        }
        setTimeout(() => {
            block_content.removeEventListener('click')
        }, 10);
    })
})