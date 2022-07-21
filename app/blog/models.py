from django.db import models
import uuid
# import CustomUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.utils.html import mark_safe
from django.urls import reverse
from sorl.thumbnail import ImageField

User = get_user_model()


# Create blog post model


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    authorId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(_('Title'), max_length=150)
    content = models.TextField(_('Content'), )
    summary = models.TextField(_('Summary'), max_length=250, blank=True)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    createdAt = models.DateTimeField(_('Created at'), auto_now_add=True)
    updatedAt = models.DateTimeField(_('Updated at'), auto_now=True)
    thumbnail = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Thumbnail')
    TYPES = (
        ('S', 'Standard Post'),
        ('A', 'Audio Post'),
        ('V', 'Video Post'),
    )
    type = models.CharField(max_length=20, choices=TYPES, default='S')
    category = models.ManyToManyField('Category', blank=True, verbose_name='Categories')

    def __str__(self):
        return self.title

    @property
    def content_summary(self):
        return truncatechars(self.content, 100)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blog_post_detail', kwargs={"slug": self.slug})


class PostMeta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    postId = models.ForeignKey('Post', on_delete=models.CASCADE, )
    metaKey = models.CharField(_('Meta Key'), max_length=100)
    metaValue = models.TextField(_('Meta Value'), max_length=250, blank=True)

    def __str__(self):
        return self.metaKey

    class Meta:
        verbose_name_plural = _('Metas')


class PostComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    postId = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Post')
    authorId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    title = models.TextField(_('Title'), max_length=100)
    content = models.TextField(_('Content'), max_length=500)
    createdAt = models.DateTimeField(_('Created At'), auto_now_add=True)
    updatedAt = models.DateTimeField(_('Updated At'), auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = _('Comments')


class Category(models.Model):
    # Auto increment id
    title = models.CharField(_('Category'), max_length=100)
    # The meta title is to be used for browser title and SEO.
    metaTitle = models.CharField(_('Meta Title'), max_length=100, blank=True)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    createdAt = models.DateTimeField(_('Created at'), auto_now_add=True)
    updatedAt = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Categories')


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('Image Name'), max_length=100)
    image = ImageField(_('Image'), upload_to='images/')
    createdAt = models.DateTimeField(_('Created at'), auto_now_add=True)
    updatedAt = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return self.name

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""
