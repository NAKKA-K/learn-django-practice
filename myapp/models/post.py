from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.conf import settings


# 投稿を保存するテーブル
class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL) # Userテーブルを外部参照
  title = models.CharField(max_length = 32)
  text = models.TextField()
  created_date = models.DateTimeField(default = timezone.now)
  published_date = models.DateTimeField(blank = True, null =True)

  def publish(self): # 投稿更新
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

  def get_absolute_url(self): # 詳細のurlを返す
    return reverse('post:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
  post = models.ForeignKey(Post, related_name = 'comments')
  author = models.CharField(max_length = 200)
  text = models.TextField()
  created_date = models.DateTimeField(default = timezone.now)
  approved_comment = models.BooleanField(default = False)

  def approve(self):
    self.approved_comment = True
    self.save()

  def approved(self):
    return self.comments.filter(approved_comment = True)

  def __str__(self):
    return self.text


