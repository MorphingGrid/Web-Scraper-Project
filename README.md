![banner](assets/banner.png)

# Author
- [Vinh Van](https://github.com/MorphingGrid)


#  Insights at a Glance:  
Data Analysts and Data Engineering Roles stress more on data cleaning and database management skills such as Excel and SQL whereas Data Scientists require a much more Software oriented and well rounded background. Many Data Analyst Roles didn't even list a programming lanauge as required whereas Data Scientists often required knowing Python as a bare minimum.  
## Most Popular Software Overall:  
**SQL**  
## Most Popular Software by Role  
Data Analyst: **Excel**  
Data Engineers: **SQL**  
Data Scientists: **Python** 

# Tableau Dashboard 

![dashboard](assets/Dashboard.png)
### Interactive dashboard can be found [here](https://public.tableau.com/app/profile/vinh.van/viz/JobPostingWebScraper/Dashboard1)

# Table of Contents

  - [Data Problem](#data-problem)
  - [Tech Stack](#tech-stack)
  - [Methods](#methods)
  - [Recommendations and Lessons Learned](#recommendations-and-lessons-learned)

## Data Problem
This Automated Bot will scrape the top job postings of popular job sites such as Indeed, LinkedIn and Handshake to record and collect the frequency of key tech stacks such as Excel, Python and SQL etc etc. The project aims to provide valuable insights into common industry practices. The gathered data will help narrow the scope of future projects and guide the identification of essential skills necessary for success in the field. Through this analysis, the project seeks to enhance decision-making and optimize learning strategies for career advancement.

## Tech Stack  
  - Python (selenium, BeautifulSoup4, re, time)
  - [ChromeWebDriver](https://sites.google.com/chromium.org/driver/?pli=1)
  - Chrome Version 114
  - This project was done in Spyder using Anaconda which is why the requirements.txt is bloated. Can be done with a clean Python install using PIP instead of using Conda

## Methods
  - Automated Web Navigation
  - Dynamic HTML Elements Interaction
  - Web Scraping
  - Dashboard Visualization

## Recommendations and Lessons Learned

### Using Excel to create a blueprint
![table](assets/table.PNG)  

  
I highly recommend using Excel to record your data and create a simple table and pivot table to help organize your thoughts. Don't spend so much time making it look pretty or worrying about the visuals. That's what visualization software like PowerBi and Tableau are for, just use it to give you a baseline of how you want to display the information. 

### Websites that require logins and security credentials
Throughout this project, Handshake proved to be a tougher nut to crack than LinkedIn and Indeed for a multitude of reasons. The first was that Handshake requires a person have an account and login before they can look at available jobs.. I used my student account to login to Handshake and to automate this I would recommend using driver.get() to brute force and grab the webpages during the login process and minimizing how often you're searching for elemnets on the webpage to reduce loading times. You will have to input your actual username and password for Selenium to login so if you are not comfortable with putting that information publicly I would omit the Handshake code from your src file like I did or putting a placeholder text whereever a username or password is needed.

### Static vs Dynamic HTML Elements
Another problem I ran into early with Handshake is how they handle their HTML elements. I have a very basic knowledge of web development but from how I understand it, websites handle their HTML in 2 ways: statically and dynamically. Older and simpler websites such as Indeed and LinkedIn employ static HTML, where information is pre-created and stored on a web server. When the user requests a page from a static website, the user's browser retrieves the entire pre-built file with fixed content.  

Handshake uses a dynamically updated system. This is where websites dynamically update content on the fly either using some form of server-side technology like PHP, Python or React. This is so the webpage can change on-the-fly based on how the user interacts with it. Go on any webpage, right click the page and click 'Inspect Elements'. If every piece of text or element can be found in the elements tab, it is most likely a static website. If a lot of the information is omitted or you only see a skelaton with the most basic information, it is probably a dynamically updated website where a lot of the information is hidden behind an API or external source. This makes web scraping a bit more difficult since you can't just scrape the raw data on the page like you can with static pages.  

The method I employed was a brute force approach to the problem. Handshake uses 'style cards', think of them as little rectangle boxes that contain each individual job posting(shown above). Instead of containing the HTML elements of each job postng in each card, it instead encapsulates the information and uses a reference link known as an **href** parameter, storing a link to a page with the actual job posting.

  - First, I iterated through every style card and pulled the reference links and put them all in a list called job_links
  - Second, I iterated through job_links, using ChromeWebDriver to load each link, giving 5 second for the webpage to load
  - Third, I used BeautifulSoup4 to then parse and scrape the elements that were now available
  - Lastly, I made sure to account for grammatical issues such as capitalization and standalone characters

This isn't the only or best way to implement web scraping dynamically updated systems, only one possible solution.

##  What Can Be Improved  

  - **Pagination**: My project only scraped the first 20-25 jobs of each job board, the most relevant ones on the first page of each search result. Depending on the scope of a project you may want to look at the top 100 jobs for example, and that would require you to navigate to page 2,3,etc... of a job board. Implementing some form of pagination would be useful.  
  - **Reduce Load Times**: Another thing is loading efficiency. Because of my brute force approach, it increased loading time. Scraping would often take around 3-5 minutes and that was just for the first page of results. This was a result of having to set a global implicit wait of 10 seconds and occasional use of time.sleep() of 5 seconds to ensure the information was properly loaded before it could be parsed. Optimizing the code to reduce the use of these methods would improve loading times tremendously.  
