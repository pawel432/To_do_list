from django.contrib.auth.middleware import get_user
from django.utils.deprecation import MiddlewareMixin


class CustomUserMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response

    def __call__(self, request):
        request.CustomUser = get_user(request)
        return self.get_response(request)

    def process_response(self, request, response):
        if request.path == 'signout/':
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            return response
