from selenium import webdriver
from pytube import YouTube
from pytube.cli import on_progress


url = "" # Youtube Channel URL

browser = webdriver.Chrome() # Location to Driver (leave empty if stored in same path)
browser.get(url)

browser.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button").click() # Agree to form (needed if not signed into Youtube)

videos = browser.find_elements_by_xpath('//*[@id="video-title"]')
video_urls = []

# Build list of all video urls to be downloaded by PyTube
for video in videos:
    href = video.get_attribute('href')
    if href:
        video_urls.append(href)

browser.quit()

for url in video_urls:
    try:
        yt_obj = YouTube(url, on_progress_callback=on_progress)
        yt_obj.streams.filter(file_extension='mp4').first().download()

    except Exception as e:
        print(e)
        raise Exception('Some exception occurred.')
        print('All YouTube videos downloaded successfully.')
