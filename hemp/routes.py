from tornado.web import URLSpec as r
from hemp.auth.handlers import LoginHandler, LogoutHandler
from hemp.blog.handlers import HomeHandler #TODO: move
from hemp.blog.handlers import ArchiveHandler, FeedHandler, EntryHandler, \
        ComposeHandler

urls = (
    # hemp.auth
    r(r'/auth/login/', LoginHandler, name='login'),
    r(r'/auth/logout/', LogoutHandler, name='logout'),

    # hemp.blog
    r(r"/", HomeHandler, name='index'), #TODO: move
    r(r"/archives/", ArchiveHandler, name='archives'),
    r(r"/feed.xml", FeedHandler, name='feed'),
    r(r"/p/([^/]+).html", EntryHandler, name='post'),
    r(r"/compose/", ComposeHandler, name='compose'),
)
