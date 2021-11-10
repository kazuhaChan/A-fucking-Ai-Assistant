# importing the library
from Noi import talk
import requests
from bs4 import BeautifulSoup as bs
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"
def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    result = {}
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
 # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # extract the name of the day
        day_name = day.findAll("div")[0].attrs['aria-label']
        # get weather status for that day
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result
if __name__ == "__main__":
        URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
        import argparse
        parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
        parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.
                                            Default is your current location determined by your IP Address""", default="")
        # parse arguments
        args = parser.parse_args()
        region = args.region
        URL += region
        # get data
        data = get_weather_data(URL)
        talk(f"Temperature now: {data['temp_now']} Celsius")
