$(document).ready(function () {
    console.log($('#tel-res'))
    $('#tel-res').mask('(00) 0000-0000');
    $('#tel-cel').mask('(00) 00000-0000');
    $('.cpf').mask('000.000.000-00');
    $('.formulario').submit(function () {
        $('#tel-res').unmask();
        $('#tel-cel').unmask();
        $('.cpf').unmask();
    });
});