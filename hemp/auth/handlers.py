import tornado.auth, tornado.web

import hemp.handler
from hemp.auth.models import User


class LoginHandler(hemp.handler.Handler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user_data):
        print user_data
        if not user_data:
            raise tornado.web.HTTPError(500, "Google auth failed")
        try:
            user = User.objects.get(email=user_data['email'])
        except:
            user = None
        if not user:
            # Auto-create first author
            any_author = User.objects.all().count()
            if not any_author:
                user = User(name=user_data['name'], email=user_data['email'])
                user.save()
            else:
                self.redirect("/")
                return
        self.set_secure_cookie("user", str(user.id))
        self.redirect(self.get_argument("next", "/"))


class LogoutHandler(hemp.handler.Handler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))
