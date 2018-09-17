# ring-screenshot
A couple of scripts to help save screenshots from Ring doorbells and security cameras. One is written in node, the other in python. 

## Installation
```bash
git clone git@github.com:paulmaunders/ring-screenshot.git
cd ring-screenshot
npm install yarn -g
yarn install
pip install ring_doorbell
```
On Centos you may need to install some additional dependencies
```
yum install pango.x86_64 libXcomposite.x86_64 libXcursor.x86_64 libXdamage.x86_64 libXext.x86_64 libXi.x86_64 libXtst.x86_64 cups-libs.x86_64 libXScrnSaver.x86_64 libXrandr.x86_64 GConf2.x86_64 alsa-lib.x86_64 atk.x86_64 gtk3.x86_64 ipa-gothic-fonts xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-utils xorg-x11-fonts-cyrillic xorg-x11-fonts-Type1 xorg-x11-fonts-misc -y
``` 

## Configuration
Set your configuration variables in config.ini
```
cp config.ini.example config.ini
RING_USERNAME=myuser 
RING_PASSWORD=mypassword 
SCREENSHOTS_DIRECTORY=~/ring-screenshot/screenshots
```
If you want to set them persistently, edit /etc/environment or the equivalent file.
## Usage
To run the Javascript version of the screenshot script
```
node ring-screenshot.js
```
To run the Python version of the screenshot script
```
python ring-screenshot.py
```
