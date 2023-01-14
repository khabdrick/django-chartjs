from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=200)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'%s' % (self.name)


class Article(models.Model):
    text_title = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(max_length=200, null=True, blank=True)
    refWriter = models.ForeignKey(Writer, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'[%s] : %s' % (self.refWriter,self.text_title)