import csv                                                                                               
from datetime import date                                                                                
import snscrape.modules.twitter as sntwitter                                                             
import time                                                                                              
import pyautogui
import pyperclip

x_box_pos = -555
y_box_pos = 1033
interval_s = 1

def prompt():
    pyautogui.click(x_box_pos,y_box_pos)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

# Creating list to append tweet data to                                                                  
tweets_list1 = []
tweet_date_list = []                                                                                        
                                                                                                         
# Using TwitterSearchScraper to scrape data and append tweets to list                                    
while(True):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:ChipotleTweets').get_items()):             
        if i>2:                                                                                           
            break                                                                                            
        print(tweet.rawContent)
        if '888222' in tweet.rawContent:
            print("FOUND")
            parse_msg = tweet.rawContent
            begin_index = parse_msg.index("Text ") 
            end_index = parse_msg.index(" to 888222") 

            text_code = parse_msg[begin_index + 5: end_index]
            print(text_code)
            print(tweet.date)
            if tweet.date in tweet_date_list:
                print("this tweet already used") 
                break
            tweet_date_list.append(tweet.date)
            print(tweet_date_list)
            pyperclip.copy(text_code)
            prompt()
            #prompt2()
            break 
        
        tweets_list1.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username])
    
    time.sleep(interal_s)
    print("Running...")

# -555 1033
