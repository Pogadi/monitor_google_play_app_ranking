## What you need to run Script?
I used 2 available libraries for Python, you have to install them through pip. 

- BeautifulSoup
- Selenium + Chrome WebDriver

To install them use pip install, commands below: 

`pip install beautifulsoup4`

`pip install selenium` 

Or you can use file `requirements.txt` in repo to install them:

`pip install requirements.txt` 

To get scroll down function you need to download WebDriver, available at link below for your current browser version. 
https://sites.google.com/a/chromium.org/chromedriver/downloads

To be sure that you installed it right, more information here:
https://sites.google.com/a/chromium.org/chromedriver/getting-started


### How does it work?
 1. To the `keywords.txt` file insert list of your keywords which you want to test for rank. It's necessary to put each of them at a new line
 2. In file ranking.py find function `def is_ranking(class_post):`
    and change variable `app_id = "com.taransit.transport"` to package_name of your app. 
 3. Change path to your downloaded WebDriver, in main function `def main():` and variable `driver = webdriver.Chrome("YOUR/PATH/OF/WEBDRIVER")`
 4. Run a script to start crawling Google Play. `python3 ranking.py`
 5. As a result you will get output in a console / terminal for each keyword. But you can find also a export of .csv file with an exact date and time of monitoring.
 6. Enjoy ! :) 
 
  ![Keywords rank output](https://github.com/Pogadi/monitor_google_play_app_ranking/blob/master/src/example%20of%20output.png)
