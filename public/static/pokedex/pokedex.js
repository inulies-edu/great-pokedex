var info = document.getElementById('info')
var type = document.getElementById('type')
var abilities = document.getElementById('abilities')
var moves = document.getElementById('moves')

function infoShow() {
    info.classList.remove('hide')
    type.classList.add('hide')
    abilities.classList.add('hide')
    moves.classList.add('hide')
}

function typeShow() {
    info.classList.add('hide')
    type.classList.remove('hide')
    abilities.classList.add('hide')
    moves.classList.add('hide')
}

function abilitiesShow() {
    info.classList.add('hide')
    type.classList.add('hide')
    abilities.classList.remove('hide')
    moves.classList.add('hide')
}

function movesShow() {
    info.classList.add('hide')
    type.classList.add('hide')
    abilities.classList.add('hide')
    moves.classList.remove('hide')
}