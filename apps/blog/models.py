from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.PROTECT, default=1)
    title = models.CharField(_("title"), max_length=250)
    excerpt = models.TextField(_("excerpt"), null=True)
    content = models.TextField(_("content"))
    slug = models.SlugField(_("slug"), max_length=250, unique_for_date="published")
    published = models.DateTimeField(_("published"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(_("status"), max_length=9, choices=options, default="published")

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ("-published",)

    def __str__(self) -> str:
        return self.title

    objects = models.Manager()
    postobjects = PostObjects()
