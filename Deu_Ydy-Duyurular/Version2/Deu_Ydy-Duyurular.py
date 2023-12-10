#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/mr-Ucar

# On purpose, I did not use the 'requests' and 'bs4' libraries. I used the 'feedparser' library instead for simplicity.
# I also used the 'pandas' library to save the announcements in .csv and Excel formats.
# I used the 'os' library to check if the announcements have already been downloaded.
### On purpose, this script will only download the latest announcements. It will not download all the announcements.
### If you want to download all the announcements, then you can use the 'requests' and 'bs4' libraries.And use a Loop and a Counter. 
### But I guess no students will need to download all the announcements which are old and not valid. They will only need to download the latest announcements.

### I used some color output for fun. You can remove them if you want.So you can use this script even in a mobile device.
### If you wonder how these colorful output works, you can google it as "ANSI escape code"
import os
import feedparser
import pandas as pd
from time import sleep

print("")
# If you do not mimic the Browser, then you will get a 403 error. So I mimicked the browser by adding the 'headers'.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
}

base_url = "https://ydy.deu.edu.tr/duyurular/feed/" # RSS feed URL

# Fetch the RSS feed
feed = feedparser.parse(base_url)

# Check if the feed was fetched successfully
# I wrote some 'elif' conditions to see the status code. You can remove them if you want. 
if feed.status == 200:
    print("\033[94mDeu_Ydy-Duyurular.py\033[0m")
    print(f"\033[95mStatus code: {feed.status}\033[0m")
    sleep(0.1)
    #print("\033[94mThe website is up and running.\033[0m\n")
    print(f"\033[94mThe website {base_url} is up and running.\033[0m\n")
    sleep(0.1)
    print(f"Fetching the latest announcements from {base_url}...\n")
    sleep(0.2)
elif feed.status == 404:
    print("Page not found.")
elif feed.status == 500:
    print("Server error.")
elif feed.status == 403:
    print("Access denied.")
elif feed.status == 301:
    print("Page moved permanently.")
elif feed.status == 302:
    print("Page moved temporarily.")
elif feed.status == 503:
    print("Service unavailable.")
elif feed.status == 504:
    print("Gateway timeout.")
elif feed.status == 505:
    print("HTTP version not supported.")
elif feed.status == 401:
    print("Unauthorized.")
elif feed.status == 400:
    print("Bad request.")
elif feed.status == 408:
    print("Request timeout.")
else:
    print("Failed to fetch RSS feed.")

def check_downloaded_feeds():
    """Check if the RSS feeds have already been downloaded."""
    output_file_txt = "YDY-duyurular.txt"
    output_file_csv = "YDY-duyurular.csv"
    output_file_excel = "YDY-duyurular.xlsx"

    if os.path.exists(output_file_txt) and os.path.exists(output_file_csv) and os.path.exists(output_file_excel):
        print(f"New Announcements from {base_url } have already been downloaded.\n")
        print("\033[91mNo need to download them again.\033[0m\n")  
        print("\nIf you want to download them again, then delete the following files: \n")
        print(f"{output_file_txt}\n{output_file_csv}\n{output_file_excel}\n")
        print(f"\n\tOutput files are located at:\n{os.getcwd()}")
        return True
    else:
        return False

def download_announcements():
    """Download the latest announcements from the RSS feed."""
    print("Downloading announcements...\n") 
    sleep(0.5)
    print("Saving announcements in .txt, .csv and Excel formats...\n")
    sleep(0.5)
    base_url = "https://ydy.deu.edu.tr/duyurular/"
    output_file_txt = "YDY-duyurular.txt"
    output_file_csv = "YDY-duyurular.csv"
    output_file_excel = "YDY-duyurular.xlsx"

    # Extract the announcements from the feed
    items = feed.entries
    if len(items) > 0:
        # Save announcements in .txt format
        with open(output_file_txt, "a") as file:
            for item in items:
                title = item.title
                link = item.link
                file.write(f"Title: {title}\nLink: {link}\n\n")
        print("Announcements downloaded and saved in .txt format.") 

        # Save announcements in .csv format with Turkish encoding
        df = pd.DataFrame({'Title': [item.title for item in items],
                           'Link': [item.link for item in items]})
        df.to_csv(output_file_csv, index=False, encoding='utf-8-sig') 
        print("Announcements downloaded and saved in .csv format.") 

        # Save announcements in Excel format
        df.to_excel(output_file_excel, index=False)
        print("Announcements downloaded and saved in Excel format.\n")
    else:
        print("No announcements found.")

if not check_downloaded_feeds():
    download_announcements()


print("\033[92m\t★彡 https://ydy.deu.edu.tr/en/announcementz/ 彡★\033[0m") # Spot the spelling mistake! Not mine,but this is the original website's mistake. 
print("\n\t\033[95m◦•●◉✿ For Turkish, follow >> https://ydy.deu.edu.tr/tr/duyurular/ ✿◉●•◦\033[0m\n")  #https://ydy.deu.edu.tr/tr/duyuru-arsivi-arama-sayfasi/ 

