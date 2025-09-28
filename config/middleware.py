from django.http import HttpResponse

class PrintHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the Host header so you see it in Render logs
        print(">>> Incoming Host:", request.get_host())
        return self.get_response(request)
