from django.views.generic import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
class Login(View):

    def get(self,request):
        contexto ={'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("/veiculo")
        else:
            return render(request, 'sistema/autenticacao.html', contexto)
        
    def post(self,request):
        usuario = request.POST.get('usuario',None)
        senha = request.POST.get('senha',None)

        #verificaçao
        user = authenticate(request,username=usuario,password=senha)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("/veiculo")
            return render(request,'sistema/autenticacao.html',{'mensagem': 'usuario ou senha incorretos'})
        return render(request,'sistema/autenticacao.html', {'mensagem':'usuario incorreto'})
class Logout(View):
    def get(self,request):
        contexto = {'mensagem':''}
        logout(request)
        return redirect(settings.LOGIN_URL)
