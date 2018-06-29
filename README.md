# BEER!
### Python code to scrape BeerAdvocate reviews  
forked from  **jtrawinski/BeerScraper** on github.  
Used for a project to complete my **Springboard** curriculum.  

Beer.py and Scraper.py contain code to scrape beer reviews from BeerAdvocate.com  
To invoke, call  ** df = create_data(20) **  (this would request 20 reviews.)  It scrapes the first review for a random beer.  

###jtrawinski's notes:
"This currently fully working, however it is still a work in progress. Eventually this will be used to construct a huge dataset of beer word-frequency data, which will then be used to build a beer recommendation system."  
*jtrawinski's original code has features that I removed, such as vectorizing the review words into an array.  My code simply stores the full review text.*  

## My project:
Change scraper to collect data from BeerAdvocate:  
Call up a random beer and collect: beer **name, brewery, style, rating, and review** (first review on file for that beer)  
Vectorize the words data.  
Analyze the words to predict style and rating.   
Possible project: collect data for users, create a recommender based on their reviews.  

## Why I search for beer:  
My second project at Springboard to apply supervised learning techniques. As a lover of craft beer, I often check BeerAdvocate reviews to make sure the beer I buy is a good choice. I set out to create two things: a predictor that uses text from beer reviews to guess the rating and style, and a recommender system that would produce a list of beers to try based on similarity to a favorite beer and priority for recommendations (i.e. recommendations sorted by: overall rating, smell, taste, look, feel or alcohol content).