const puppeteer = require('puppeteer');

// Create screenshot folder if it doesn't exist
var fs = require('fs');
var dir = './screenshots';

if (!fs.existsSync(dir)){
    fs.mkdirSync(dir);
}

// Take screenshot

async function run() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1366, height: 768});

  // Login
  await page.goto('https://ring.com/users/sign_in');
  await page.type('#user_email', process.env.RING_USERNAME);
  await page.type('#user_password', process.env.RING_PASSWORD);
  await page.screenshot({ path: 'screenshots/ring-login.png' });
  await page.click('#new_user > button');
  await page.waitForNavigation();

  // Navigate to the Account Activity page
  await page.goto('https://ring.com/account/activity');
  await page.waitFor(10000);
  await page.screenshot({ path: 'screenshots/ring-activity.png' });

  const videoUrl = await page.$eval('#ding-video', el => el.src);
  // console.debug(videoUrl);


  // Download the video at the top of the page
  var https = require('https');
  var file = fs.createWriteStream('screenshots/video.mp4');
  var request = https.get(videoUrl, function(response) {
    response.pipe(file);
  });

  // #ding-video - video at top of page
  // #data-table-0 > div.scrollable > table > tbody > tr:nth-child(11) > td.table-cell.description
  ////*[@id="data-table-0"]/div[2]/table/tbody/tr[11]/td[4]/text()[2]

  browser.close();
}

run();
