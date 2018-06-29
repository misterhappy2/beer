from bs4 import BeautifulSoup
import requests
import re
import nltk
import pandas as pd

class Beer:
    """Beer object contains word-frequency data for the BeerAdvocate reviews of given beer.
    """
    def __init__(self, beer_id):
        self.beer_id = beer_id
        self.soup = self.get_soup()
        self.name, self.brewery = self.get_name()
        if self.name is not None:
            self.rating = self.get_rating()
            self.review = self.get_words()
            self.style = self.get_style()
        else:
            self.get_rating = None
            self.words = None
            self.style = None

    def get_name(self):
        n_b = self.soup.find("h1").get_text()
        # Protecting against invalid beer_ids
        if n_b == "404 Not Found - BeerAdvocate":
            return None, None
        elif " | " not in n_b:
            return None, None
        name, brewery = tuple(n_b.split(" | "))
        return name, brewery

    def get_rating(self):
        return float(self.soup.find("span", class_="ba-ravg").get_text())

    def get_soup(self):
        url = "https://www.beeradvocate.com/beer/profile/" + self.beer_id + "?sort=topr&start=0"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html5lib")
        return soup

    def get_words(self):
        review = ''
        for s in self.soup.find_all("div", id="rating_fullview_content_2"):
            s = list(s.stripped_strings)[5:]
            review += ' '.join(s[:-4]) + ' '
        review = review.lower()  # Convert to all lowercase
        return review

    def get_style(self):
        return self.soup.find_all("a", href=re.compile("/beer/style/"))[2].get_text()

    def get_attributes(self):
        # Returns dictionary of attributes of the beer used to create dataframe
        attributes = {'name': self.name, 'brewery': self.brewery, 'style': self.style,
                      'rating': self.rating,'review': self.review}
        return attributes

    def create_df(self):
        # Create single row dataframe
        attributes = self.get_attributes()
        df = pd.DataFrame(attributes, index=[0])
        return df
