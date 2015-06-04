from django.db import models

class Picture(models.Model):
    slug = models.SlugField(primary_key=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    url = models.URLField(blank=True)
    owner = models.ManyToManyField('auth.User', blank=True)
    def __unicode__(self):
        return self.slug
    def get_absolute_url(self):
        if self.image: return self.image.url
        else: return self.url

class Tag(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    def __unicode__(self):
        return self.name

class Idea(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=512, blank=True)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)
    def __unicode__(self):
        if self.title: return self.title
        else: 
            if len(description <= 32):
                return description[:32]
            else:
                return description[:32] + '...'

class Collaborator(models.Model):
    account = models.OneToOneField('auth.User', blank=True, null=True)
    name = models.CharField(max_length=64)
    url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    def __unicode__(self):
        return self.name

class App(models.Model):
    creator = models.ForeignKey('auth.User', related_name='my_apps')
    name = models.CharField(max_length=64)
    version = models.CharField(max_length=32)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    screenshots = models.ManyToManyField('Picture', related_name='logo_of', blank=True)
    ideabase = models.ManyToManyField('Idea', blank=True)
    appcredits = models.TextField(blank=True)
    collaborators = models.ManyToManyField('Collaborator', blank=True)
    apkfile = models.FileField(blank=True)
    def __unicode__(self):
        return '%(name)s [%(version)s]' % {
            'name': self.name,
            'version': self.version,
            }