import json
from django.conf import settings
from django.db import models
from django.core import serializers

# Create your models here.

class UpdateQuerySet(models.QuerySet):
	def serialize(self):
		list_values = list(self.values("firstname","lastname","address","city","state","zip_code", "country"))
		return json.dumps(list_values)

class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self._db)

class Lead(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	firstname = models.TextField(null=False)
	lastname = models.TextField(null=False)
	address = models.TextField(null=False)
	city = models.TextField(null=False)
	state = models.TextField(null=False)
	zip_code = models.TextField(null=False)
	country = models.TextField(null=False)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = UpdateManager()

	def __str__(self):
		return '%s %s %s %s %s %s' % (self.firstname,self.lastname, self.address, self.city, self.zip_code, self.country)

	def serialize(self):
		data = {
			"firstname": self.firstname,
			"lastname": self.lastname,
			"address": self.address,
			"city": self.city,
			"state": self.state,
			"zip_code": self.zip_code,
			"country": self.country,
		}
		data = json.dumps(data)
		return data