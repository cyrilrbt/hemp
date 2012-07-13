# hemp

hemp is a fast a minimalistic blog engine. It's written in [Python](http://www.python.org/), using [Tornado](http://tornadoweb.org/), [MongoEngine](http://mongoengine.org/), [Buildout](http://buildout.org/), and [Supervisor](http://supervisord.org/).

The starting point for hemp was Tornado's demo [blog engine](https://github.com/facebook/tornado/tree/master/demos/blog). A few methods are still present, and a lot has been added and/or compartmentalized for ease of deployment and extensibility.


## Give it a try

It's pretty easy to try hemp, it's all ready to run. Just execute those commands:

	$ python bootstrap.py
	$ bin/buildout
	$ bin/development
	
All you have to do next is open up your browser to [http://localhost:5000/](http://localhost:5000/). If your mongo server is not localhost, you'll have to change it in `hemp/settings/development.py`.

The default behavior is that the first person that opens the `compose` page will be required to sign in (via google auth), a user account will be created for him, and he can post. Subsequent attempts will not create an account.

### Understanding those commands

* `python bootstrap` is going to download and install anything that buildout will need to run. Don't worry, you don't need to be root: everything stays in the project directory.
* `bin/buildout` is going to read `buildout.cfg` to install dependencies and create binaries in `bin/`
* `bin/development` is going to load the development settings (from `hemp/settings/development.py`) and run tornado.


## Building your own blog

I recommend either forking or creating a new repository that contains everything from this one. After that, do whatever the hell you want!

If you rename the main `hemp` directory, make sure you update `buildout.cfg`, `production.cfg`, and `setup.py`.

## Production deployment

### Commands

	$ python bootstrap.py
	$ bin/buildout -c production.cfg
	$ bin/supervisord
	$ bin/supervisorctl status
	
### Understanding those commands

The recommended deployment method for Tornado is to run it directly, and use nginx or apache as a proxy and static file server. Running a python process on its own is kind of scary, so the buildout configuration in `production.cfg` will download and configure supervisor, so that it will make sure tornado is restarted if it ever crashes.

Once it's installed, you can run `bin/supervisord` to start its daemon, and then `bin/supervisorctl` to control the processes. For example `bin/supervisorctl restart all` will restart all tornado instances. Pretty useful when you've just updated your code.

By default, hemp will start 2 tornado processes, running on ports 2000 and 2001. All of that is configurable in `production.cfg`.

## Comments

I didn't think it was relevant or even worth it to build a comments engine, [Disqus](http://disqus.com/) can provide that, and it's really easy to integrate.