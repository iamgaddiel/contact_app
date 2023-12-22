
const bgColors = [
    'green',
    'orange',
    'lightseagreen',
    'lightcoral',
    'lightslategrey',
    'aqua',
    'chocolate',
    'teal',
    'tomato',
    'darkviolet',
]

let counter = 0;

document.querySelectorAll('.contact_avatar').forEach(avatar => {
    if (counter === bgColors.length) counter = 0;
    avatar.style.backgroundColor = bgColors[counter]
    ++counter
})


