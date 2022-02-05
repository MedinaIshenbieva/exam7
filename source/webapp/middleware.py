from django.http import HttpResponse


class ExampleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("before_view")

        request_path_data = request.path.split("/")
        for path in request_path_data:
            try:
                id = int(path)
                if id < 100:
                    return HttpResponse("id от 1 до 100 зарезервированы")
            except ValueError:
                pass

        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(view_func, view_args, view_kwargs)

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response


class Example2Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("before_view2")
        response = self.get_response(request)

        print("after_view2")
        return response
#
