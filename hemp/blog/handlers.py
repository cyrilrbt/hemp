import re
import markdown
import unicodedata

import tornado.web

import hemp.handler
from hemp.blog.models import Post


class HomeHandler(hemp.handler.Handler):
    def get(self):
        entries = Post.objects.all()[:5]
#        if not entries:
#            self.redirect("/compose/")
#            return
        self.render("home.html", entries=entries)


class EntryHandler(hemp.handler.Handler):
    def get(self, slug):
        try:
            entry = Post.objects.get(slug=slug)
        except:
            raise tornado.web.HTTPError(404)
        self.render("entry.html", entry=entry)


class ArchiveHandler(hemp.handler.Handler):
    def get(self):
        entries = Post.objects.all()
        self.render("archive.html", entries=entries)


class FeedHandler(hemp.handler.Handler):
    def get(self):
        entries = Post.objects.all()[:10]
        self.set_header("Content-Type", "application/atom+xml")
        self.render("feed.xml", entries=entries)


class ComposeHandler(hemp.handler.Handler):
    @tornado.web.authenticated
    def get(self):
        id = self.get_argument("id", None)
        entry = None
        if id:
            try:
                entry = Post.objects.get(id=id)
            except:
                pass
        self.render("compose.html", entry=entry)

    @tornado.web.authenticated
    def post(self):
        id = self.get_argument("id", None)
        title = self.get_argument("title")
        text = self.get_argument("markdown")
        html = markdown.markdown(text)
        if id:
            try:
                entry = Post.objects.get(id=id)
            except:
                raise tornado.web.HTTPError(404)
            slug = entry.slug
            entry.title = title
            entry.markdown = text
            entry.html = html
            entry.save()
        else:
            slug = unicodedata.normalize("NFKD", title).encode("ascii", "ignore")
            slug = re.sub(r"[^\w]+", " ", slug)
            slug = "-".join(slug.lower().strip().split())

            if not slug:
                slug = "post"

            while True:
                try:
                    e = Post.objects.get(slug=slug)
                    slug += "-2"
                except:
                    break

            p = Post(
                author=self.get_current_user(),
                title=title,
                slug=slug,
                markdown=text,
                html=html
            )
            p.save()
        self.redirect(self.reverse_url('post', slug))
