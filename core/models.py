from django.db import models
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()
    content = RichTextField(
        config_name="special",
        external_plugin_resources=[
            (
                "youtube",
                "/static/shareledge/ckeditor-plugins/youtube/youtube/",
                "plugin.js",
            )
        ],
    )

    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
