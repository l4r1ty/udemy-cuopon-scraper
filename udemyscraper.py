import praw
import smtplib
import secret
import time

#reads the key words for the search
keywordFile = open('keywords.txt', 'r')
keywords = keywordFile.read().split(',')
keywordFile.close()
#reddit api conn
reddit = praw.Reddit(
    client_id=secret.client_id,
    client_secret=secret.client_token,
    username=secret.username,
    password=secret.password,
    user_agent=secret.user_agent
)


def search_reddit():
    subreddit = reddit.subreddit('udemyfreebies')
    new_posts = subreddit.new()  # requests the last 100 post in subreddit
    findings = {}
    #if keywords found in the posts, adds the posts title and url to a dict
    for posts in new_posts:
        for keyword in keywords:
            if keyword in posts.title.lower():
                findings[posts.title] = posts.url
    findings.encode('ascii', 'ignore')
    if findings:
        send_mail(findings)


def send_mail(findings):
    #reads in titles that were sent previously
    sentFile = open('sent.txt', 'r')
    sent = sentFile.read().splitlines()
    sentFile.close()
    #if item sent previously, deletes it from the found item dictionary
    for title in sent:
        try:
            if findings[title]:
                del findings[title]
        except KeyError:
            pass
    #sending email
    if findings:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(secret.src_mail, secret.mail_pw)

        subject = 'Found free courses that may be interesting'
        body = ''
        try:
            for item in findings:
                body += str(item) + '\n'
                body += str(findings[item] + '\n')
        except UnicodeEncodeError:
            pass

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            secret.src_mail,
            secret.dst_mail,
            msg
        )
        server.quit()

    #Saving the sent course's titles
    sentFile = open('sent.txt', 'a')
    for item in findings:
        new_item = item
        sentFile.write('{}\n'.format(new_item))
    sentFile.close()


while True:
    search_reddit()
    time.sleep(600)