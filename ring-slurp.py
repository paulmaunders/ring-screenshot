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
pprint(myring.devices)

#Download the most recent motion video from the 2nd stickup cam
dev = myring.stickup_cams[1]
#old_event=6605114755809561293
pprint(dev.id)
exit()

#TODO!!!
#Loop through all devices
#Use dev.id in the filename, store them in sub-folders (1 per device)
# for dev in list(myring.stickup_cams + myring.chimes + myring.doorbells):

#Loop through all events in the event history
keep_looking=True
old_event=None

while keep_looking==True:
  history = dev.history(limit=100, kind='motion', older_than=old_event)

  # If there are no more events, stop looking!
  if len(history) == 0:
    keep_looking=False;

  # If there are events, loop through them and save each one.
  for recording in history:

    # pprint(recording)

    # Keep track of the event id so we can look for older events in the next iteration
    old_event=recording['id']   
    timestr = recording['created_at'].strftime("%Y%m%d-%H%M%S")
    output_file = SCREENSHOT_DIRECTORY + '/motion-stickup1-' + timestr + '.mp4'

    # Skip downloading if we have already downloaded them.
    if os.path.isfile(output_file):
      print output_file + ' exists, skipping...'
    else:
      print 'Downloading ' + output_file 
      dev.recording_download(
        recording['id'],
        filename= output_file,
        override=True)


