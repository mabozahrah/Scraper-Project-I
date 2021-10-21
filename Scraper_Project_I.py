#imported packages- instascrape to scrape profile url and post url
#instaloader package to download all photos from profile url
#packages to install:
#pip install insta-scrape
#pip install instaloader
from instascrape import Profile
from instascrape import Post
import instaloader
import json
import datetime

#function to make JSON serializable class 
def ser(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

#input if URL is post or profile to scrape
purl = input("Post or Profile?\n")

#If post, scrape all available fields and save as .json file
#If profile, scrape all available fields and save all images
if purl == "Post" :
    url = input("Enter instagram post URL: ")
    insta_post = Post(url)
    insta_post.scrape()
    insta_post.to_dict()
    with open('data.json', 'w') as fp:
        json.dump(insta_post.to_dict(), fp, default = ser)
elif purl == "Profile":
    url = input("Enter Instagram Profile URL: ")
    username = url[26:-1]
    prof = Profile(username)
    prof.scrape()
    prof.to_dict()
    with open('data1.json', 'w') as fp:
        json.dump(prof.to_dict(), fp, default = ser)
    L = instaloader.Instaloader()
    L.download_profile(profile_name=username)

