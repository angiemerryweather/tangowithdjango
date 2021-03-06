from django.contrib import admin
from polls.models import Poll, Choice

'''
Add a bunch of Choices directly when creating a Poll object.
This tells Django: "Choice objects are edited on the Poll admin page.
By default, provide enough fields for 3 choices."
'''
class ChoiceInline(admin.TabularInline): # choice fields are displayed in table format
	model = Choice
	extra = 3

# Re-ordering fields on the edit form.
class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				 {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	# Adds ability to create Choices associated with Polls inline
	inlines = [ChoiceInline]
	# Controls which attributes of Polls are displayed on the poll list.
	list_display = ('question', 'pub_date', 'was_published_recently')
	# Adds a filter to the display by when the Poll was published
	list_filter = ['pub_date']
	# Adds search box to search by question
	search_fields = ['question']
	# Adds the ability to drill down by publishing date
	date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
