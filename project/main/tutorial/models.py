from django.db import models


class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=255)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=70)
    comment_text = models.CharField('текст комментария', max_length=255)

    def __str__(self):
        return self.comment_text
