import tornado.web
from mongoengine import connect
from hemp import routes
from hemp.settings import (development as dev, production as prod)


def run(settings):
    """
    Run the app using specified settings
    """
    app = tornado.web.Application(routes.urls,
                                  **settings.TORNADO)
    app.listen(settings.TORNADO['port'], '127.0.0.1')
    connect(settings.MONGO['name'],
            **settings.MONGO['options'])
    tornado.ioloop.IOLoop.instance().start()


def production():
    return run(prod)


def development():
    return run(dev)
