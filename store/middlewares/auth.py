from django.shortcuts import redirect


def auth_middleware(get_response):

    # decorator for auth_middleware
    def middleware(request):
        # for returning back  to the same orders page whenever passes middleware
        returnUrl = request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')
        response = get_response(request)
        return response

    return middleware

# middlware is a decorator of a function auth_middleware and can be called before any request in various views in your app
# whenever needed