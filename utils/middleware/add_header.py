from config.settings import settings


class AddCorsHeader(object):
    """
    The Django Debug Toolbar usually only works for views that return HTML.
    This middleware wraps any non-HTML response in HTML if the request
    has a 'debug' query parameter (e.g. http://localhost/foo?debug)
    Special handling for json (pretty printing) and
    binary data (only show data length)
    """

    @staticmethod
    def process_response(request, response):
        try:
            if request.META['HTTP_ORIGIN'] in settings.IGNORE_CSRF_URLS:
                response['Access-Control-Allow-Credentials'] = "true"
                response['Access-Control-Allow-Methods'] = "GET,PUT,POST"
                response[
                    "Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
                response['Access-Control-Allow-Origin'] = request.META['HTTP_ORIGIN']
        except:
            pass
        return response
