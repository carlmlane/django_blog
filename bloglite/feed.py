from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPosts(Feed):
    title = "CmL Blog"
    link = "/feed/"
    description = "Carl Lane's Recent Posts"

    def items(self):
        return Entry.objects.published()[:5]