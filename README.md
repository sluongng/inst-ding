# inst-ding
a quick script to send notification from instagram to dingtalk

credit to https://github.com/ping/instagram_private_api for the hardworks

## Requirements

- Python 2.7
- `instagram_private_api` from https://github.com/ping/instagram_private_api
- Requests from `pip install requests`

## How to use

1. Modify main.py with your own configurations. The **Dingtalk Webhook** must be replaced by your own.

```python
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
```

2. On commandline, run `python main.py`

3. To run this in the background, run `python main.py &`

   For more info on this: https://askubuntu.com/questions/396654/how-to-run-the-python-program-in-the-background-in-ubuntu-machine
