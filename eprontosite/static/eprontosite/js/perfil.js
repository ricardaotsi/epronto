$(document).ready(function () {
    $('#first-name').mask('Z',{translation: {'Z': {pattern: /[a-zA-Z ]/, recursive: true}}});
    $('#last-name').mask('Z',{translation: {'Z': {pattern: /[a-zA-Z ]/, recursive: true}}});
    $('#tel-res').mask('(00) 0000-0000');
    $('#tel-cel').mask('(00) 00000-0000');
    $('.cpf').mask('000.000.000-00');
    $('.formulario').submit(function () {
        $('#tel-res').unmask();
        $('#tel-cel').unmask();
        $('.cpf').unmask();
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('[type="file"]').onchange = changeEventHandler;
}, false);

function changeEventHandler(event) {
    $(".custom-file-label").text($('#inputimage')[0].value.split(/(\\|\/)/g).pop());
}