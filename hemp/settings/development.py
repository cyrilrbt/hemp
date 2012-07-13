import os

from hemp.blog.modules import EntryModule


TORNADO = {
    'debug': True,
    'static_path': os.path.join(os.path.dirname(__file__), '..', 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), '..', 'templates'),
    'cookie_secret': '<put something random in here>',
    'login_url': '/auth/login/',
    'domain_name': 'localhost',
    'port': 5000,


    'ui_modules': {
        "Entry": EntryModule,
    },
    'xsrf_cookies': True,
    'autoescape': None,

}


MONGO = {
    'name': 'hemp-dev',
    'options': {}
}
