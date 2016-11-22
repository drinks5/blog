from django.utils.deprecation import MiddlewareMixin


class AspectMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass
