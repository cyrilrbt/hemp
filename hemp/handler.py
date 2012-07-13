import tornado.web

from hemp.auth.models import User


class Handler(tornado.web.RequestHandler):
    def get_current_user(self):
        #TODO: Load user object, once we have them
        rc = None
        if self.get_secure_cookie("user"):
            try:
                rc = User.objects.get(id=self.get_secure_cookie("user"))
            except:
                pass
        return rc

    def absolute_url(self, name, *args, **kwargs):
        rc = "http://" + self.settings['domain_name']
        if self.settings.get('debug') and self.settings.get('port') and self.settings.get('port')!=80:
            rc += ':' + str(self.settings['port'])
        try:
            rc += self.reverse_url(name, *args, **kwargs)
        except:
            rc += name
        return rc
