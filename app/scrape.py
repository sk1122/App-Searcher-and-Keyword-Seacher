# Importing Required Libraries
import requests
from bs4 import BeautifulSoup


class GooglePlay:

    """
    It'll Scrape Data from Google Play Store
    @param: app_id - string
    """

    def __init__(self, app_id):
        self.id = app_id
        self.url = f"https://play.google.com/store/apps/details?id={self.id}"

        self.r = requests.get(self.url)
        self.pageContent = self.r.content

        self.soup = BeautifulSoup(self.r.content, 'html.parser')

    def details(self):
        self.appName = self.soup.findAll('h1')[0].text
        self.imageUrl = self.soup.findAll('img', {'class': 'T75of'})[0]['src']
        self.developer = self.soup.find('a', {'class': 'hrTbp'}).text
        self.description = f"{self.soup.find('div', {'jsname': 'sngebd'}).get_text(strip=True)[:200]}..."
        self.downloads = self.soup.findAll('span', {'class': 'htlgb'})[5].text
        self.reviews = self.soup.find('span', {'class': 'EymY4b'}).text[:-5]
        self.ratings = self.soup.find('div', {'class': 'BHMmbe'}).text

        data = (self.appName, self.imageUrl, self.developer,
                self.description, self.downloads, self.reviews, self.ratings)

        return data


class AppleApp:

    """
    It'll Scrape Data from Apple App Store
    @param: app_name - string
    @param: app_id - string
    """

    def __init__(self, app_name, app_id):
        self.app_name = app_name
        self.app_name = self.app_name.lower().split(" ")
        self.app_name = "-".join(self.app_name)
        self.app_id = app_id
        self.url = f"https://apps.apple.com/in/app/{self.app_name}/id{self.app_id}"

        self.r = requests.get(self.url)
        self.pageContent = self.r.content

        self.soup = BeautifulSoup(self.r.content, 'html.parser')

    def details(self):
        self.appname = self.soup.find(
            "h1", {'class': 'app-header__title'}).text[:-5]
        self.image = self.soup.findAll(
            'source', {'class': 'we-artwork__source'})[0]['srcset'].split(" ")[0]
        self.developer = self.soup.find('a', {'class': 'link'}).text
        self.description = f"{self.soup.findAll('p')[1].text[:200]}..."
        self.ratings = self.soup.find(
            'figcaption', {'class': 'we-rating-count'}).text.split(", ")[0]
        self.reviews = self.soup.find(
            'figcaption', {'class': 'we-rating-count'}).text.split(", ")[1]

        data = (self.appname, self.image, self.developer,
                self.description, self.reviews, self.ratings)

        return data


class KeywordFinder:

    """
    It'll Scrape Data from Given Website
    @param: url - string
    """

    def __init__(self, url):

        self.url = url

        self.headers = {'User-Agent': 'FooBar-Spider 1.0'}

        self.page = requests.get(
            self.url, headers=self.headers)
        self.pageContent = self.page.content

        self.soup = BeautifulSoup(self.pageContent, "html.parser")

    def keywords(self):

        """ Method for Returning Keywords """

        try:
            self.keyword = self.soup.findAll("meta", {"name": "keywords"})[
                0]["content"]
        except IndexError:
            try:
                self.keyword = self.soup.findAll("meta", {"name": "Keywords"})[
                    0]["content"]
            except IndexError:
                try:
                    self.keyword = self.soup.findAll(
                        "meta", {"name": "description"})[0]["content"]
                except IndexError:
                    return False
        return self.keyword
