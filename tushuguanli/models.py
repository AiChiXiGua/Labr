from django.db import models

# Book {ISBN (PK), Title, AuthorID (FK), Publisher, PublishDate, Price}
# Author {AuthorID (PK), Name, Age, Country}


class Author(models.Model):
    AuthorID = models.IntegerField()
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Country = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Book(models.Model):
    ISBN = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(
        Author,
    )
    Publisher = models.CharField(max_length=100)
    PublishDate = models.DateTimeField()
    Price = models.IntegerField()

    def __str__(self):
        return self.Title
