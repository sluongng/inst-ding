from instagram_web_api import Client
import requests

INSTAGRAM_BASE_URL = "https://www.instagram.com/p/"
DINGTALK_BASE_URL = "https://oapi.dingtalk.com/robot/send?access_token="

# REPLACE THIS WITH YOURS DINGDING CHATBOT
ACCESS_TOKEN = "123123"
INSTAGRAM_TAG = "selfie"


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
    web_api = Client(auto_patch=True, drop_incompat_keys=False)
    feed = web_api.tag_feed(INSTAGRAM_TAG)
    feed = feed["data"]["hashtag"]["edge_hashtag_to_media"]["edges"]

    for post in feed:
        post = post["node"]
        postId = post["id"]
        picUrl = post["display_url"]
        shortCode = post["shortcode"]
        if not post["is_video"]:
            send2Ding(postId, picUrl, shortCode)


if __name__ == '__main__':
    main()