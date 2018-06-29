# BEER!
### Python code to scrape and analyze reviews from BeerAdvocate.com  
forked from  **jtrawinski/BeerScraper** on github.  
Used for a project to complete my **Springboard** curriculum.  

### jtrawinski's notes:  
"This currently fully working, however it is still a work in progress. Eventually this will be used to construct a huge dataset of beer word-frequency data, which will then be used to build a beer recommendation system."  
*jtrawinski's original code has features that I removed or altered.*  

### My project:
Change scraper to collect data from BeerAdvocate:  
Call up a random beer and collect: beer **name, brewery, style, rating,** and **review** (first review on file for that beer)  
Vectorize the words data.  
Analyze the words to predict style and rating.   
Possible project: collect data for users, create a recommender based on their reviews.  

**Beer.py** and **Scraper.py** contain code to scrape random beer reviews from BeerAdvocate.com  
**Scrape and store new data** I used to collect over 80,000 reviews.  
**EDA** a quick look at the distributions, and a search for anomolies.  
**Analyze** convert review text to word count vectors. Convert word frequency vectors.  Apply machine learning to make inferences about the beer.

### Why I search for beer:  
This is my second project at Springboard, meant to apply supervised learning techniques. 
As a lover of craft beer, I often check BeerAdvocate reviews to make sure the beer I buy is a good choice. So I set out to create two things: a predictor that uses text from beer reviews to guess the rating and style, and a recommender system that would produce a list of beers to try based on similarity to a favorite beer and priority for recommendations (i.e. recommendations sorted by: overall rating, smell, taste, look, feel or alcohol content).