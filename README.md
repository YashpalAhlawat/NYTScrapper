# NYTScrapper
Develop a scraper project to automate data extraction using Selenium Python and BeautifulSoup to perform the following list of actions and events :
1.Open the NY Times website (https://www.nytimes.com/) and click on the Login button
2.On the Login page, programmatically provide your credentials and login
3.Now click on the “Tech” header item from the list of category Items
4.Scroll down to the “Latest” tab section, you will see a list of news articles. Scrape the list of all articles from this section using Selenium & BeautifulSoup. Scrape data, such as Article Title, Article Summary, Author name, Published Date, and save then into a list of dictionaries in Python. Also, return the result as a JSON file.
5.Next, click on the “Account” drop-down on the top right and click on the “Account” hyperlink, On the account page, scrape all available user information present on that page, save it as a dictionary in Python, and return the result as a JSON file.
6.[optional, but a plus] Using Flask or Django REST Framework, develop two REST API endpoints:


/news/tech-latest : this endpoint will initiate the scraper and provide the scraped “Tech - Latest list of news” data
/profile : this endpoint will initiate the scraper and provide the scraped “Account info details” data



###Pre requisite
1. you have python installed on system
2. Get the webdriver for the same version as the chrome from https://chromedriver.chromium.org/downloads
3. place chromedriver in Resource folder
4. create venv with latest python (3.10)
5. install requirement using `pip install -r requirements.txt`
6. run main.py file
7. go to the endpoint http://localhost:2051/news/tech-latest


#TODO 
Avoid Captcha ang get details for accont and NYT is blockin login using script.
All steps has been completed except for Account details as nyt is captcha is blocking login.

For , Fetching NYT latest tech post, script open and login to the website, if captcha come. It will go back to default view (guest)
and fetch posts from there.


