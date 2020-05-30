from uuid import uuid4
from django.db import models
from tinymce.models import HTMLField
from bs4 import BeautifulSoup


class Bio(models.Model):
    id = models.UUIDField(default=uuid4, editable=False,
                          primary_key=True, unique=True)
    content = HTMLField()

    def __str__(self):
        return self.content[0:15]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.content = "".join(self.content.splitlines())

        soup = BeautifulSoup(self.content)
        links = soup.find_all('a')
        for link in links:
            link['class'] = ['external-link']
            link['rel'] = ['noopener', 'noreferrer']

        self.content = str(soup)

        super().save(force_insert=force_insert, force_update=force_update,
                     using=using, update_fields=update_fields)
