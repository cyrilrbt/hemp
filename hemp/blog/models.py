import datetime
import mongoengine as db

from hemp.auth.models import User


class Post(db.Document):
    author = db.ReferenceField(User, required=True)
    slug = db.StringField(max_length=100, unique=True, required=True)
    title = db.StringField(max_length=512, required=True)
    markdown = db.StringField(required=True)
    html = db.StringField(required=True)
    published = db.DateTimeField()
    updated = db.DateTimeField()

    meta = {
        'ordering': ['-published', ]
    }

    def save(self, *args, **kwargs):
        # Handle publication/update time
        if not self.published:
            self.published = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        return super(Post, self).save(*args, **kwargs)
