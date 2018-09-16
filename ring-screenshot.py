import os
from ring_doorbell import Ring
from pprint import pprint

# Set your environment variables with export RING_USERNAME='user@host'
RING_USERNAME = os.environ.get('RING_USERNAME', None)
RING_PASSWORD = os.environ.get('RING_PASSWORD', None)

pprint(os.environ)

myring = Ring(RING_USERNAME, RING_PASSWORD)

myring.is_connected
True

pprint(myring.devices)

#Download a video

dev = myring.stickup_cams[1]

pprint(dev.history(limit=10, kind='motion')[0]['id'])

dev.recording_download(
    dev.history(limit=10, kind='motion')[0]['id'],
                     filename='./screenshots/lastding.mp4',
                     override=True)
