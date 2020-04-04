# Scraper

It Searches for Apps on Google Play Store and Apple App Store, also It Searches for
Keywords in given URL and also Suggests some Recommended Keywords


## Usage


Run this Command on your Command-Line to create a Virtual Env & Activating it.

```bash
virtualenv PROJECT_NAME
source PROJECT_NAME/bin/activate
```


### Installing Dependencies

To Install Required Dependencies, Run this Command

```bash
pip install -r requirements.txt
```

It'll Install all required Libraries for our App.

### Running App

To Run it, Run this Command

```bash
python manage.py runserver
```

<div style="page-break-after: always;"></div>

## Features

It Searches for Apps on Google Play Store and Apple App Store, also It Searches for
Keywords in given URL and also Suggests some Recommended Keywords

This app uses SQlite3 Database.
I have included a ```scrape.py``` which includes all the code used to scrape data
from different sites seperated using Classes.

Folder App Contains all the code required for our app to run.

Frontend is built using Tailwind CSS - Which a Utility Based CSS Framework which
focuses on flexibility of Using.

JQuery and AJAX are used to send POST Request to Server and Fetch Back Data.
JQuery is used in .html files, so that I can use
```python
{% url 'app:url' %}
```
Format.

In Keywords Page,
The Recommend Keyword Section was hard to implement as we have to do multiple
data-type conversions on Model Class to use it (I Don't Know Any other Option).
So,
I Implemented using simple method - Generate Random Integers between 0 to End of Array
and pick that element as a Recommend Keyword.

```Sorry for this Implementation but I did not wanted to leave it blank```

I have added a Simple User Authentication System and have Personalized
User Experience

I was Initially using Class Based Views but Switched to Function based view later.


## Note

If the database is not working properly, you can do data migrations using this command

```bash
python manage.py makemigrations
python manage.py migrate
```
