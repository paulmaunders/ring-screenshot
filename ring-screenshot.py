import os
import time
from ring_doorbell import Ring
from pprint import pprint

# Set your environment variables with export RING_USERNAME='user@host'
RING_USERNAME = os.environ.get('RING_USERNAME', None)
RING_PASSWORD = os.environ.get('RING_PASSWORD', None)
SCREENSHOT_DIRECTORY = './screenshots'

# Create the screenshot folder
if not os.path.exists(SCREENSHOT_DIRECTORY):
    os.makedirs(SCREENSHOT_DIRECTORY)

# Connect to RING's API

myring = Ring(RING_USERNAME, RING_PASSWORD)
myring.is_connected
True

# List devices
# pprint(myring.devices)

#Download the most recent motion video from the 2nd stickup cam
dev = myring.stickup_cams[1]
# pprint(dev.history(limit=10, kind='motion')[0]['id'])

timestr = dev.history(limit=10, kind='motion')[0]['created_at'].strftime("%Y%m%d-%H%M%S")

dev.recording_download(
    dev.history(limit=10, kind='motion')[0]['id'],
                     filename='./' + SCREENSHOT_DIRECTORY + '/motion-stickup1-' + timestr + '.mp4',
                     override=True)
