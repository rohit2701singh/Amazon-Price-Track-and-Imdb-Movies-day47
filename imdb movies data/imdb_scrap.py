import pandas
import requests
from bs4 import BeautifulSoup


name_list = []
year_list = []
genres_list = []
rating_list = []
votes_list = []
story_list = []

i = 1
while i < 50:

    # URL = f"https://www.imdb.com/search/title/?title_type=tv_series&countries=kr&start={i}&ref_=adv_nxt"
    URL = F"https://www.imdb.com/search/title/?title_type=feature&countries=in&languages=hi&start={i}&ref_=adv_nxt"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
    }

    response = requests.get(url=URL, headers=header)
    content = response.text
    # print(content)
    soup = BeautifulSoup(content, "html.parser")

    all_container = soup.find_all(name="div", class_="lister-item-content")
    # print(single_container)

    for single_container in all_container:
        try:
            name = (single_container.select_one(selector=".lister-item-header a")).getText()
            name_list.append(name)
        except:
            continue

        try:
            year = ((single_container.find(name="span", class_="lister-item-year text-muted unbold")).getText()).strip("\n)(-")
            year_list.append(year)
        except:
            year_list.append("NaN")

        try:
            genres = ((single_container.find(name="span", class_="genre")).getText()).strip()
            genres_list.append(genres)
        except:
            genres_list.append("NaN")

        try:
            rating = ((single_container.find(name="div", class_="inline-block ratings-imdb-rating")).getText()).strip()
            rating_list.append(rating)
        except:
            rating_list.append("NaN")

        try:
            votes = ((((single_container.find(name="p", class_="sort-num_votes-visible")).getText()).split(":"))[1]).strip()
            votes_list.append(votes)
        except:
            votes_list.append("NaN")

        try:
            story = (((single_container.find_all(name="p", class_="text-muted"))[1]).getText()).strip()
            story_list.append(story)
        except:
            story_list.append("NaN")

    i += 50

print(name_list)
print(year_list)
print(genres_list)
print(rating_list)
print(votes_list)
print(story_list)

dataframe = {
    "Title": name_list,
    "Release Year": year_list,
    "Genres": genres_list,
    "Rating": rating_list,
    "Votes": votes_list,
    "Story": story_list
}

data = pandas.DataFrame(dataframe)
data.to_csv("bollywood_movies.csv", encoding="utf-8")











