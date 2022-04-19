#return a 401 unauthorized in django


def unauthorized(request):
    return HttpResponse(status=401)