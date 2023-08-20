#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup #1
import requests
import pandas as pd


# In[2]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


table = soup.find("table", {"class": "wikitable sortable"})


rank_list = []
name_list = []
artist_list = []
upload_date_list = []
views_list = []


for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")

    rank = columns[0].get_text().strip()
    name = columns[1].get_text().strip()
    artist = columns[2].get_text().strip()
    upload_date = columns[3].get_text().strip()
    views = columns[4].get_text().strip()

    rank_list.append(rank)
    name_list.append(name)
    artist_list.append(artist)
    upload_date_list.append(upload_date)
    views_list.append(views)

for i in range(len(rank_list)):
    print(f"Rank: {rank_list[i]}")
    print(f"Name: {name_list[i]}")
    print(f"Artist: {artist_list[i]}")
    print(f"Upload Date: {upload_date_list[i]}")
    print(f"Views: {views_list[i]}\n")


# In[3]:


import requests #2
from bs4 import BeautifulSoup

url = "https://www.bcci.tv/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


fixtures_section = soup.find("div", {"class": "js-list"})


match_titles = []
series_names = []
places = []
dates = []
times = []


for fixture in fixtures_section.find_all("li", {"class": "fixture-list__item"}):
    match_title = fixture.find("p", {"class": "fixture__additional-info"}).get_text().strip()
    series_name = fixture.find("h3", {"class": "fixture__tournament__name"}).get_text().strip()
    place = fixture.find("p", {"class": "fixture__info"}).span.get_text().strip()
    date = fixture.find("span", {"class": "fixture__datetime"}).get("data-date")
    time = fixture.find("span", {"class": "fixture__time"}).get_text().strip()

    match_titles.append(match_title)
    series_names.append(series_name)
    places.append(place)
    dates.append(date)
    times.append(time)


for i in range(len(match_titles)):
    print(f"Match Title: {match_titles[i]}")
    print(f"Series: {series_names[i]}")
    print(f"Place: {places[i]}")
    print(f"Date: {dates[i]}")
    print(f"Time: {times[i]}\n")


# In[4]:


import requests #3
from bs4 import BeautifulSoup

url = "http://statisticstimes.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


indian_states_link = soup.find("a", text="Indian States")

if indian_states_link:
    indian_states_url = indian_states_link.get("href")
    indian_states_url = url + indian_states_url

 
    response = requests.get(indian_states_url)
    soup = BeautifulSoup(response.content, "html.parser")

 
    gdp_table = soup.find("table", {"id": "table_id"})

   
    ranks = []
    states = []
    gdp_18_19 = []
    gdp_19_20 = []
    shares = []
    gdp_billion = []


    for row in gdp_table.find_all("tr")[1:]:
        columns = row.find_all("td")

        rank = columns[0].get_text()
        state = columns[1].get_text()
        gdp1819 = columns[2].get_text()
        gdp1920 = columns[3].get_text()
        share = columns[4].get_text()
        gdp_b = columns[5].get_text()

        ranks.append(rank)
        states.append(state)
        gdp_18_19.append(gdp1819)
        gdp_19_20.append(gdp1920)
        shares.append(share)
        gdp_billion.append(gdp_b)

    for i in range(len(ranks)):
        print(f"Rank: {ranks[i]}")
        print(f"State: {states[i]}")
        print(f"GSDP(18-19): {gdp_18_19[i]}")
        print(f"GSDP(19-20): {gdp_19_20[i]}")
        print(f"Share(18-19): {shares[i]}")
        print(f"GDP($ billion): {gdp_billion[i]}\n")
else:
    print("Indian States link not found.")


# In[5]:


from selenium import webdriver #4
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome(executable_path='path_to_driver/chromedriver')

url = "https://github.com/"
driver.get(url)


time.sleep(5)


page_source = driver.page_source


soup = BeautifulSoup(page_source, "html.parser")


trending_repositories = soup.find("ol", class_="repo-list")


for repo in trending_repositories.find_all("li"):
    repository_title = repo.find("h3").text.strip()
    repository_description = repo.find("p", class_="mb-1").text.strip()
    contributors_count = repo.find("a", href=lambda href: href and "/contributors" in href).text.strip()
    language_used = repo.find("span", itemprop="programmingLanguage").text.strip()

    print(f"Repository Title: {repository_title}")
    print(f"Repository Description: {repository_description}")
    print(f"Contributors Count: {contributors_count}")
    print(f"Language Used: {language_used}")
    print()


driver.quit()


# In[8]:


import requests #6
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

novels_table = soup.find("table", {"class": "in-article sortable"})

# Initialize lists to store the extracted details
book_names = []
author_names = []
volumes_sold = []
publishers = []
genres = []

# Iterate through rows in the table
for row in novels_table.find_all("tr")[1:]:
    columns = row.find_all("td")

    book_name = columns[1].get_text().strip()
    author_name = columns[2].get_text().strip()
    volumes = columns[3].get_text().strip()
    publisher = columns[4].get_text().strip()
    genre = columns[5].get_text().strip()

    book_names.append(book_name)
    author_names.append(author_name)
    volumes_sold.append(volumes)
    publishers.append(publisher)
    genres.append(genre)

# Print or manipulate the extracted details as needed
for i in range(len(book_names)):
    print(f"Book Name: {book_names[i]}")
    print(f"Author Name: {author_names[i]}")
    print(f"Volumes Sold: {volumes_sold[i]}")
    print(f"Publisher: {publishers[i]}")
    print(f"Genre: {genres[i]}\n")


# In[9]:


pip install requests beautifulsoup4 selenium


# In[11]:


import time #5
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='path_to_driver/chromedriver')

url = "https://www.billboard.com/"
driver.get(url)


charts_option = driver.find_element(By.LINK_TEXT, "Charts")
charts_option.click()


hot_100_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Hot 100"))
)
hot_100_link.click()


time.sleep(5)


page_source = driver.page_source


soup = BeautifulSoup(page_source, "html.parser")


songs_table = soup.find("table", {"class": "chart-list container js-chart-list"})


song_names = []
artist_names = []
last_week_ranks = []
peak_ranks = []
weeks_on_board = []


for row in songs_table.find_all("div", {"class": "container-list__elem"}):
    song_name = row.find("span", {"class": "chart-element__information__song text--truncate color--primary"}).text.strip()
    artist_name = row.find("span", {"class": "chart-element__information__artist text--truncate color--secondary"}).text.strip()
    last_week_rank = row.find("span", {"class": "chart-element__meta text--center color--secondary text--last"}).text.strip()
    peak_rank = row.find("span", {"class": "chart-element__meta text--center color--secondary text--peak"}).text.strip()
    weeks_on_chart = row.find("span", {"class": "chart-element__meta text--center color--secondary text--week"}).text.strip()

    song_names.append(song_name)
    artist_names.append(artist_name)
    last_week_ranks.append(last_week_rank)
    peak_ranks.append(peak_rank)
    weeks_on_board.append(weeks_on_chart)


for i in range(len(song_names)):
    print(f"Song Name: {song_names[i]}")
    print(f"Artist Name: {artist_names[i]}")
    print(f"Last Week Rank: {last_week_ranks[i]}")
    print(f"Peak Rank: {peak_ranks[i]}")
    print(f"Weeks on Board: {weeks_on_board[i]}\n")

# Close the browser
driver.quit()


# In[12]:


import requests #7
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls095964455/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

tv_series_list = soup.find_all("div", {"class": "lister-item-content"})


names = []
year_spans = []
genres = []
run_times = []
ratings = []
votes = []


for tv_series in tv_series_list:
    name = tv_series.find("h3").a.text
    year_span = tv_series.find("span", {"class": "lister-item-year"}).text
    genre = tv_series.find("span", {"class": "genre"}).text.strip()
    run_time = tv_series.find("span", {"class": "runtime"}).text
    rating = tv_series.find("div", {"class": "ipl-rating-star small"}).text.strip()
    vote = tv_series.find("span", {"name": "rk"}).get("data-value")

    names.append(name)
    year_spans.append(year_span)
    genres.append(genre)
    run_times.append(run_time)
    ratings.append(rating)
    votes.append(vote)


for i in range(len(names)):
    print(f"Name: {names[i]}")
    print(f"Year Span: {year_spans[i]}")
    print(f"Genre: {genres[i]}")
    print(f"Run Time: {run_times[i]}")
    print(f"Rating: {ratings[i]}")
    print(f"Votes: {votes[i]}\n")


# In[13]:


pip install requests beautifulsoup4 selenium


# In[14]:


import time #8
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='path_to_driver/chromedriver')

url = "https://archive.ics.uci.edu/"
driver.get(url)


show_all_dataset_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Show All Dataset"))
)
show_all_dataset_link.click()


time.sleep(5)


page_source = driver.page_source


soup = BeautifulSoup(page_source, "html.parser")


dataset_table = soup.find("table", {"border": "1", "cellpadding": "5"})


dataset_names = []
data_types = []
tasks = []
attribute_types = []
no_of_instances = []
no_of_attributes = []
years = []


pattern = re.compile(r'\d{4}')


for row in dataset_table.find_all("tr")[1:]:
    columns = row.find_all("td")

    dataset_name = columns[0].a.text
    data_type = columns[1].text
    task = columns[2].text
    attribute_type = columns[3].text
    no_of_instances = columns[4].text
    no_of_attributes = columns[5].text
    year_match = pattern.search(columns[6].text)
    year = year_match.group() if year_match else "N/A"

    dataset_names.append(dataset_name)
    data_types.append(data_type)
    tasks.append(task)
    attribute_types.append(attribute_type)
    no_of_instances.append(no_of_instances)
    no_of_attributes.append(no_of_attributes)
    years.append(year)


for i in range(len(dataset_names)):
    print(f"Dataset Name: {dataset_names[i]}")
    print(f"Data Type: {data_types[i]}")
    print(f"Task: {tasks[i]}")
    print(f"Attribute Type: {attribute_types[i]}")
    print(f"No of Instances: {no_of_instances[i]}")
    print(f"No of Attributes: {no_of_attributes[i]}")
    print(f"Year: {years[i]}\n")


driver.quit()


# In[ ]:




