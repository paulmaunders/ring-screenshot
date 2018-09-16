# ring-screenshot
A couple of scripts to help save screenshots from Ring doorbells and security cameras. One is written in node, the other in python. 

## Installation
```bash
git clone git@github.com:paulmaunders/ring-screenshot.git
cd ring-screenshot
yarn install
pip install ring_doorbell
```

## Configuration
Set your environment variables
```export RING_USERNAME=myuser 
export RING_PASSWORD=mypassword 
```
If you want to set them persistently, edit /etc/environment or the equivalent file.
## Usage
To run the Javascript version of the screenshot script
```node ring-screenshot.js```
To run the Python version of the screenshot script
```python ring-screenshot.py```
