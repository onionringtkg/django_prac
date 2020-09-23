from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    #この関数で、文字を返せるようになる
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

#新たにmodelsファイルを作成して、設定を追加した際には、
#py manage.py makemigrations コマンドでマイグレーションファイルを作成し直す。
#その後、py manage.py migrate コマンドの実行 
#これを行うことで、DBにカラムを新規作成できる