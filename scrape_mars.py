# Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time


# Initialize mars_data dictionary
mars_data = {}

def init_browser():
    # Initialize Browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def nasa_mars_news():
    browser = init_browser()
    # Assign NASA Mars News Site to url variable to scrape and open site in browser
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    # Start time to allow loading
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html,"html.parser")
    # Collect the latest News Title and Paragraph Text
    first_article = soup.find('li', class_='slide')
    # Get the latest article's title
    first_title = first_article.find('div',class_='content_title').text
    # Get the latest article's paragraph text
    first_para = first_article.find('div',class_='article_teaser_body').text
    # Close the browser after scraping
    browser.quit()
    # Store data in mars dictionary
    mars_data['article_title'] = first_title
    mars_data['article_txt'] = first_para

def mars_img():
    browser = init_browser()
    # Assign NASA Mars News Site to url variable to scrape and open site in browser
    news_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(news_url)
    # Start time to allow loading
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html,"html.parser")
    # Get the featured image url
    featured_image = soup.find('img',class_='headerimage')['src']
    # Add featured image url to site url to get complete url string
    full_featured_image = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/' + featured_image
    # Close the browser after scraping
    browser.quit()
    # Store data in mars dictionary
    mars_data['featured_img_url'] = full_featured_image

def mars_tbl():
    browser = init_browser()
    # Assign NASA Mars News Site to url variable to scrape and open site in browser
    news_url = 'https://space-facts.com/mars/'
    browser.visit(news_url)
    # Start time to allow loading
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html,"html.parser")
    # Get html code for facts table
    facts_tbl = soup.find('table',id='tablepress-p-mars')
    facts_tbl_str=(f"{facts_tbl}")

    # Close the browser after scraping
    browser.quit()
    # Store data in mars dictionary
    mars_data['facts_tbl_html'] = facts_tbl_str

def mars_hemisphere():
    # Create the hemisphere dictionaries
    hemisphere_image_urls=[]

    # Initialize browser
    browser = init_browser()
    # Assign NASA Mars News Site to url variable to scrape and open site in browser
    valles_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(valles_url)
    # Start time to allow loading
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html,"html.parser")
    # Get the Valles Marineris image url
    vm_image = soup.find('div',class_='downloads')
    vm_img_url = vm_image.find('a',target='_blank')['href']
    # Get the Valles Marineris title
    vm_title = soup.find('h2', class_='title').text
    # Append to dictionary
    hemisphere_image_urls.append({"title":vm_title,"img_url":vm_img_url})
    # Close the browser after scraping
    browser.quit()

    # Initialize browser
    browser = init_browser()
    # Assign the USGS Astrogeology Cerebus Hemisphere site to url variable to scrape and open site in browser
    c_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(c_url)
    # Start time to allow loading
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html,"html.parser")
    # Get the Cerberus image url
    c_image = soup.find('div',class_='downloads')
    c_img_url = vm_image.find('a',target='_blank')['href']
    # Get the Cerberus title
    c_title = soup.find('h2', class_='title').text
    # Append to dictionary
    hemisphere_image_urls.append({"title":c_title,"img_url":c_img_url})
    # Close the browser after scraping
    browser.quit()

    # Initialize browser
    browser = init_browser()
    # Assign the USGS Astrogeology Schiaparelli Hemisphere site to url variable to scrape and open site in browser
    s_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(s_url)
    # Start time to allow loading
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html,"html.parser")
    # Get the Schiaparelli image url
    s_image = soup.find('div',class_='downloads')
    s_img_url = vm_image.find('a',target='_blank')['href']
    # Get the Schiaparelli title
    s_title = soup.find('h2', class_='title').text
    # Append to dictionary
    hemisphere_image_urls.append({"title":s_title,"img_url":s_img_url})
    # Close the browser after scraping
    browser.quit()

    # Initialize browser
    browser = init_browser()
    # Assign the USGS Astrogeology Syrtis Hemisphere site to url variable to scrape and open site in browser
    sy_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(sy_url)
    # Start time to allow loading
    time.sleep(1)
    # Scrape page into Soup
    html = browser.html
    soup = bs(html,"html.parser")
    # Get the Schiaparelli image url
    sy_image = soup.find('div',class_='downloads')
    sy_img_url = vm_image.find('a',target='_blank')['href']
    # Get the Valles Marineris title
    sy_title = soup.find('h2', class_='title').text
    # Append to dictionary
    hemisphere_image_urls.append({"title":sy_title,"img_url":sy_img_url})
    # Close the browser after scraping
    browser.quit()

    # Store data in mars dictionary
    mars_data['hemisphere_img_dict'] = hemisphere_image_urls

def scrape():
    nasa_mars_news()
    mars_img()
    mars_tbl()
    mars_hemisphere()
    mars_hemisphere()

    return mars_data

if __name__ == "__main__":
    print(scrape())