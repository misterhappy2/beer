# BeerScraper
## Python code to scrape BeerAdvocate reviews
## forked from  jtrawinski/BeerScraper on github.

<div class="span5 alert alert-info">
jtrawinski's notes:
This currently fully working, however it is still a work in progress. Eventually this will be used to construct a huge dataset of beer word-frequency data, which will then be used to build a beer recommendation system. 
To-Do:
 - Consider removing words with very few mentions (likely to be typos or made-up words) [easy]
 - Add functionality to manually add new beers to dataset [easy]
 </div>

## My project:
Change forked scraper to collect data from BeerAdvocate:
beer name, brewery, style, rating, and words (from first review on file for that beer)
vectorize the words data.
analyze the words to predict style and rating.  
Possible project: collect data for users, create a recommender based on their reviews.

## Why I search for beer:
My second project at Springboard to apply supervised learning techniques. As a lover of craft beer, I often check BeerAdvocate reviews to make sure the beer I buy is a good choice. I set out to create two things: a predictor that uses text from beer reviews to guess the rating and style, and a recommender system that would produce a list of beers to try based on similarity to a favorite beer and priority for recommendations (i.e. recommendations sorted by: overall rating, smell, taste, look, feel or alcohol content).