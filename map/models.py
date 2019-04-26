from django.db import models

class Room(models.Model):
	uid = models.CharField(max_length=36)
	
class Location(models.Model):
	lat = models.CharField(max_length=15)
	lng = models.CharField(max_length=15)
	user = models.CharField(max_length=36)
	room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)


#  Models: 

#  # Create a new record using the model's constructor. 
#  record = MyModelName(my_field_name="Instance #1”) 

#  # Save the object into the database. 
#  record.save() 

#  # Change record by modifying the fields, then calling save(). 
#  record.my_field_name = "New Instance Name” 
#  record.save() 

#  # Get all book instances as iterable. The values() command formats the results as dictionaries
#  all_books = Book.objects.all().values()

# # Filter
#  wild_books = Book.objects.filter(title__contains='wild’).distinct('pub_date’) # all books with ‘wild’ in the title that have different pub dates
#  number_wild_books = wild_books.count() 
# Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello’)   # all book instances where the pub_date > (2005,1,3) AND headline!=‘Hello’
#  Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3).exclude(headline='Hello’)   # all book instances where the pub_date > (2205,1,3) OR headline!=‘Hello’)
#  Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', ‘headline')   # order by pub_date descending, then by headline ascending


# class Reporter(models.Model):
#     name = models.CharField(max_length=30)
#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)
# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateField()
#     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.headline
#     class Meta:
#         ordering = ('headline’,)

# r = Reporter(name=‘John’)
# a = Article(id=None, headline=“Stock Market Crash", pub_date=date(1929, 10, 24), reporter=r)
# a2 = r.article_set.create(headline=“Less impressive follow-up story", pub_date=date(1929, 10, 25))
# x = Reporter.objects.filter(article__headline__startswith=’Stock’) # headline is a member var of article
