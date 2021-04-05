# Udemy Coupon Scraper

The script scrapes the /r/udemyfreebies subreddit, and searches for specific keywords in the post titles.
If a specified pattern is found in a post, it saves the posts' title and the url, and sends it to a given email address.

# Setup

For setting up the script:
    1, Create a reddit profile
    2, Go to https://www.reddit.com/prefs/apps and create an app
        - The client id is rigth under the new app's name
        - The secret is the client token
    3, Select a gmail email andress, which you will send to mails from (src_mail)
    4, Go to https://myaccount.google.com/lesssecureapps and enable the less secure applications access' for this account
    
