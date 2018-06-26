from bs4 import BeautifulSoup
import requests
import re
import nltk
import pandas as pd


class Beer:
    """
    Beer object contains word-frequency data for the BeerAdvocate reviews of given beer.
    Uses first 25 comments from "top-raters" to get the data.
    Expandable to get more comments, but requires grabbing a new page for every 25 comments, which can be costly
    """
    def __init__(self, beer_id):
        # self.beer_string = beer_string
        self.beer_id = beer_id
        self.soup = self.get_soup()
        self.name, self.brewery = self.get_name()
        if self.name is not None:
            self.rating = self.get_rating()
            self.words = self.get_words()
            self.style = self.get_style()
            self.freq_dist = nltk.FreqDist(self.words)
        else:
            self.get_rating = None
            self.words = None
            self.style = None
            self.freq_dist = None

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
        words = ''
        for s in self.soup.find_all("div", id="rating_fullview_content_2"):
            s = list(s.stripped_strings)[5:]
            words += ' '.join(s[:-4]) + ' '
        # Convert to all lowercase
        words = words.lower()
        # Convert to list of words
        #words = words.split()
        # Remove stopwords
        #words = [word for word in words if word not in nltk.corpus.stopwords.words("english")]
        # Remove puncutation
        #words = [self.remove_punc(word) for word in words]
        # Remove some particular words that break things
        #words = [word for word in words if word not in ['name', 'style', 'brewery', 'rating', '']]
        # Remove numbers
        #words = [word for word in words if not word.isdigit()]
        return words

    def get_style(self):
        return self.soup.find_all("a", href=re.compile("/beer/style/"))[2].get_text()

    def remove_punc(self, word):
        # Removes punctuation from a word
        return re.sub(r'[^\w\s]', '', word)

    def get_attributes(self):
        # Returns dictionary of attributes of the beer
        # Used to create dataframe
        attributes = {'name': self.name, 'brewery': self.brewery, 'style': self.style,
                      'rating': self.rating,'words': self.words}
        attributes.update(self.freq_dist)
        return attributes

    def create_df(self):
        # Create single row dataframe
        attributes = self.get_attributes()
        df = pd.DataFrame(attributes, index=[0])
        return df
