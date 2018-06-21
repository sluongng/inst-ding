from instagram_web_api import Client
import requests
import time

# Constants
INSTAGRAM_BASE_URL = "https://www.instagram.com/p/"
INSTAGRAM_PATH_LATEST = "edge_hashtag_to_media"
INSTAGRAM_PATH_HOTTEST = "edge_hashtag_to_top_posts"
DINGTALK_BASE_URL = "https://oapi.dingtalk.com/robot/send?access_token="


# User Configurations
REFRESH_DURATION = 60  # Seconds
# Example:
# Given webhook https://oapi.dingtalk.com/robot/send?access_token=7c86f414bea82d41cf52f905de947663a4adfcd4854270a57eaf834ae223d552
# your access_token is 7c86f414bea82d41cf52f905de947663a4adfcd4854270a57eaf834ae223d552
ACCESS_TOKEN = "DEFAULT_ACCESS_TOKEN"
DEFAULT_ACCESS_TOKEN = "DEFAULT_ACCESS_TOKEN"
INSTAGRAM_TAG = "selfie"

# If want to use latest feed instead of hottest, change this to False
INSTAGRAM_IS_FEED_HOTTEST = True


def send2Ding(postId, instagramPic, shortCode):
    url = DINGTALK_BASE_URL + ACCESS_TOKEN
    message = "\n\nNew post in tag #{}: [{}]({})".format(
        INSTAGRAM_TAG,
        postId,
        INSTAGRAM_BASE_URL + shortCode,
    )
    body = {
        "msgtype": "markdown",
        "markdown": {
            "title": "Notification",
            "text": message
        },
        "at": {
            "atMobiles": [],
            "isAtAll": False
        }
    }
    print "Sending post with id: {}".format(postId)
    requests.post(url, json=body)


def main():
    if ACCESS_TOKEN == DEFAULT_ACCESS_TOKEN:
        print "Please update your Dingtalk webhook access token"
        return

    path = INSTAGRAM_PATH_HOTTEST if INSTAGRAM_IS_FEED_HOTTEST else INSTAGRAM_PATH_LATEST

    web_api = Client(auto_patch=True, drop_incompat_keys=False)
    while True:
        # Load up post have already been posted
        old_posts = []
        with open("old_posts.txt", "r") as posts_file:
            for line in posts_file:
                old_posts.append(line.rstrip())

        # Traverse to post list in response data
        feed = web_api.tag_feed(INSTAGRAM_TAG)["data"]["hashtag"]
        feed = feed[path]["edges"]

        for post in feed:
            post = post["node"]

            postId = post["id"]
            picUrl = post["display_url"]
            shortCode = post["shortcode"]
            isVideo = post["is_video"]

            if postId in old_posts:
                print "{} already exist".format(postId)
                continue
            else:
                with open("old_posts.txt", "a") as posts_file:
                    posts_file.write(postId+"\n")

                old_posts.append(postId)
                if not isVideo:
                    send2Ding(postId, picUrl, shortCode)

        time.sleep(REFRESH_DURATION)


if __name__ == '__main__':
    main()
