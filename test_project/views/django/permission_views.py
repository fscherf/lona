from lona.errors import ForbiddenError
from lona.view import LonaView


class DjangLoginView(LonaView):
    def handle_user_enter(self, request):
        if not (request.user.is_active and request.user.is_authenticated):
            raise ForbiddenError

    def handle_request(self, request):
        return '<h1>Hello {}!</h1>'.format(request.user)
