import os
import argparse

from hemp.blog.modules import EntryModule

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=5000)
args = parser.parse_args()
port = args.port


TORNADO = {
    'debug': False,
    'static_path': os.path.join(os.path.dirname(__file__), '..', 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), '..', 'templates'),
    'cookie_secret': '<put something random here>',
    'login_url': '/auth/login/',
    'domain_name': 'localhost',
    'port': port,


    'ui_modules': {
        "Entry": EntryModule,
    },
    'xsrf_cookies': True,
    'autoescape': None,

}


MONGO = {
    'name': 'hemp',
    'options': {}
}

