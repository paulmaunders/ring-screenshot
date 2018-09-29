import os
import time
from ring_doorbell import Ring
from pprint import pprint
import ConfigParser
import logging
import os.path

logging.basicConfig()

# Note that ConfigParser has been renamed to configparser in Python 3, so this will have to be renamed
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Set your environment variables with export RING_USERNAME='user@host'
RING_USERNAME = config.get('DEFAULT', 'RING_USERNAME')
RING_PASSWORD = config.get('DEFAULT','RING_PASSWORD')
SCREENSHOT_DIRECTORY = config.get('DEFAULT','SCREENSHOT_DIRECTORY')

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
#old_event=6605114755809561293
#pprint(dev.history(limit=100, kind='motion', older_than=old_event))


#Loop through all events
keep_looking=True
old_event=None
while keep_looking==True:
  history = dev.history(limit=100, kind='motion', older_than=old_event)
  if len(history) == 0:
    keep_looking=False;
  for recording in history:
    # pprint(recording)
    old_event=recording['id']   
    timestr = recording['created_at'].strftime("%Y%m%d-%H%M%S")
    output_file = SCREENSHOT_DIRECTORY + '/motion-stickup1-' + timestr + '.mp4'
    if os.path.isfile(output_file):
      print output_file + ' exists, skipping...'
    else:
      print 'Downloading ' + output_file 
      dev.recording_download(
        recording['id'],
        filename= output_file,
        override=True)

exit()



history = dev.history(limit=10, kind='motion')
for recording in history:
    timestr = recording['created_at'].strftime("%Y%m%d-%H%M%S")

    dev.recording_download(
        recording['id'],
        filename= SCREENSHOT_DIRECTORY + '/motion-stickup1-' + timestr + '.mp4',
        override=True)