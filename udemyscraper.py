import praw
import smtplib
import secret
import time

#these are the words, the script looks for at the subreddit
keywordFile = open('keywords.txt', 'r')
keywords = keywordFile.read().split(' ')
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
        try:
            post=posts.title
            post.encode('utf-8').decode('ascii')
        except UnicodeDecodeError:
            continue
        for keyword in keywords:
            if str(keyword) in posts.title.lower():
                findings[posts.title] = posts.url
    if findings:
        send_mail(findings)


def send_mail(findings):
    #reads in the titles, which are already sent to dst_mail
    try:
        sentFile = open('sent.txt', 'r')
        sent = sentFile.read().splitlines()
        sentFile.close()
    except FileNotFoundError:
        sentFile = open("sent.txt", "w")
        sentFile.close()

    #if item sent already, delete it from the found item dictionary
    for title in sent:
        try:
            if findings[title]:
                del findings[title]
        except KeyError:
            pass
    #sending the mail
    if findings:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(secret.src_mail, secret.mail_pw)

        subject = 'Found free courses that may be interesting...'
        body = ''
        for item in findings:
            body += str(item) + '\n'
            body += str(findings[item] + '\n')

        msg = f"Subject: {subject}\n\n{body}"
        
        server.sendmail(
            secret.src_mail,
            secret.dst_mail,
            msg
        )
        server.quit()

    #Saves the sent courses' titles
    sentFile = open('sent.txt', 'a')
    for item in findings:
        new_item = item
        sentFile.write('{}\n'.format(new_item))
    sentFile.close()


if __name__ == "__main__":
    while True:
        search_reddit()
        time.sleep(600)