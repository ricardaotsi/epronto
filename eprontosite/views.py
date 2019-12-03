from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from eprontosite.models import Profile
from . import cpfcheck as calc
from django.conf import settings
from django.template.defaultfilters import filesizeformat

def index(request):
    return render(request,"eprontosite/index.html")

@login_required
def dashboard_home(request):
    return render(request,"eprontosite/dashboard.html")

def validate(cpf_number):
    first_cpf_weighs = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    second_cpf_weighs = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    first_part = cpf_number[:9]
    first_digit = cpf_number[9]
    second_digit = cpf_number[10]
    if (first_digit == calc.first_check_digit(first_part,first_cpf_weighs) and
       second_digit == calc.second_check_digit(cpf_number[:10],second_cpf_weighs)):
        return True
    return False

@login_required
def perfil(request):
    usuario = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        Profile.objects.get_or_create(user=request.user)
        usuario.first_name = request.POST.get('first-name')
        usuario.last_name = request.POST.get('last-name')
        usuario.email = request.POST.get('email')
        usuario.profile.CPF = request.POST.get('cpf')
        usuario.profile.Telefone_Residencial = request.POST.get('tel-res')
        usuario.profile.Telefone_Celular = request.POST.get('tel-cel')
        if  request.FILES['inputimage']:
            usuario.profile.Foto = request.FILES.get['inputimage']
        try:
            if len(usuario.profile.CPF) < 11 or not validate(usuario.profile.CPF):
                messages.error(request, "CPF é inválido.")
            elif len(usuario.profile.Telefone_Celular) < 11:
                messages.error(request, "Telefone Celular é inválido.")
            elif request.FILES['inputimage'] and usuario.profile.Foto._size > settings.MAX_UPLOAD_SIZE:
                messages.error(request, ('O tamanho do arquivo de foto de ser menor que %s. O tamanho atual é %s') % 
                                            (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(usuario.profile.Foto._size))
)
            else:
                usuario.save()
                messages.success(request, 'Dados alterados com sucesso.')
        except Exception as e:
            messages.error(request, "Ocorreu um problema na alteração. Entre em contato com o Administrador")
    return render(request,"eprontosite/perfil.html", {'usuario':usuario})