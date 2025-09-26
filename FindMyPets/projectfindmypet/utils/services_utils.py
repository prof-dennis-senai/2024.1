from django.shortcuts import redirect, render

def validacao_form(request,form,url_redirect):
    _form = form(request.POST)
    if _form.is_valid():
        _form.save()
        return redirect(url_redirect)
    return _form