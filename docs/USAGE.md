# PriceDive - Detailed Usage Guide

## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Running the Tracker](#running-the-tracker)
4. [Implementing Real Scraping](#implementing-real-scraping)
5. [Setting Up Twitter API](#setting-up-twitter-api)
6. [Scheduling Automated Runs](#scheduling-automated-runs)
7. [Database Structure](#database-structure)
8. [Troubleshooting](#troubleshooting)

---

## Installation

### 1. Install Python
Make sure you have Python 3.8+ installed:
```bash
python --version
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

The main dependencies are:
- **httpx** - Modern HTTP client for web requests
- **matplotlib** - Data visualization for charts
- **tweepy** - Twitter API integration
- **beautifulsoup4** - HTML parsing (optional, for scraping)

---

## Configuration

### Edit `config.json`

The configuration file contains three main sections:

#### 1. Product Information
```json
"product_name": "iPhone 15 Pro 256GB"
```
This is the name that will appear in charts and tweets.

#### 2. Target Platforms
```json
"targets": [
  {
    "platform": "Taobao",
    "url": "https://item.taobao.com/item.htm?id=YOUR_PRODUCT_ID"
  }
]
```
Add one entry for each platform you want to track. You can add as many platforms as you want.

#### 3. Twitter API Keys
```json
"twitter_api_keys": {
  "consumer_key": "YOUR_CONSUMER_KEY",
  "consumer_secret": "YOUR_CONSUMER_SECRET",
  "access_token": "YOUR_ACCESS_TOKEN",
  "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET"
}
```
See [Setting Up Twitter API](#setting-up-twitter-api) for details.

---

## Running the Tracker

### Manual Run
```bash
python pricedive.py
```

This will:
1. Create/open the SQLite database
2. Load configuration from `config.json`
3. Scrape prices from all configured platforms
4. Save data to the database
5. Generate a price trend chart (`price_trend.png`)
6. Calculate price changes
7. Post to Twitter (if configured)

### First Run
On the first run, you'll only have initial data points. Run it daily to build up a price history and see trends over time.

### Generate Hook Chart
```bash
python generate_hook_chart.py
```
This creates `v_curve_example.png` with a demonstrative V-shaped price curve for your README or promotional materials.

---

## Implementing Real Scraping

⚠️ **Important:** The default `fetch_price()` function uses **simulated prices**. To track real prices, you need to implement actual web scraping.

### Step-by-Step Guide

#### 1. Inspect the Target Website

Open the product page in your browser and:
1. Right-click on the price → "Inspect Element"
2. Note the HTML structure and CSS selectors
3. Check for dynamic content (JavaScript rendering)

Example HTML:
```html
<span class="price">¥899.00</span>
```

#### 2. Update the `fetch_price()` Function

Replace the simulation code in `pricedive.py`:

```python
def fetch_price(url: str, platform: str) -> float:
    """Fetch real price from product page"""
    
    # Set realistic headers to avoid blocking
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Referer': 'https://www.google.com/'
    }
    
    try:
        # Make HTTP request
        with httpx.Client(timeout=30, follow_redirects=True) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
        
        # Parse HTML
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract price based on platform
        if platform == "Taobao":
            price_element = soup.select_one('.tb-price')  # Adjust selector
        elif platform == "JD.com":
            price_element = soup.select_one('.p-price .price')  # Adjust selector
        elif platform == "Pinduoduo":
            price_element = soup.select_one('.goods-price')  # Adjust selector
        else:
            # Generic fallback
            price_element = soup.select_one('[class*="price"]')
        
        if not price_element:
            print(f"Warning: Could not find price element for {platform}")
            return None
        
        # Clean and convert price text
        price_text = price_element.text.strip()
        price_text = price_text.replace('¥', '').replace(',', '').replace(' ', '')
        
        # Handle price ranges (e.g., "899-999")
        if '-' in price_text:
            price_text = price_text.split('-')[0]  # Take lower price
        
        return float(price_text)
        
    except httpx.HTTPStatusError as e:
        print(f"HTTP error {e.response.status_code} for {platform}: {url}")
        return None
    except Exception as e:
        print(f"Error scraping {platform}: {e}")
        return None
```

#### 3. Handle Anti-Scraping Measures

Many e-commerce sites use anti-scraping techniques:

**a) User-Agent Rotation**
```python
import random

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36...',
    # Add more user agents
]

headers = {
    'User-Agent': random.choice(USER_AGENTS)
}
```

**b) Add Delays**
```python
import time

def fetch_price(url, platform):
    # ... scraping code ...
    time.sleep(random.uniform(2, 5))  # Random delay between requests
    return price
```

**c) Use Proxies (if needed)**
```python
proxies = {
    "http://": "http://proxy.example.com:8080",
    "https://": "http://proxy.example.com:8080"
}

response = client.get(url, headers=headers, proxies=proxies)
```

#### 4. Handle JavaScript-Rendered Content

Some sites load prices dynamically with JavaScript. In this case, you may need:

**Option A: Find the API endpoint**
Use browser DevTools (Network tab) to find the actual API that returns price data, then call that directly.

**Option B: Use Selenium or Playwright**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

def fetch_price_dynamic(url, platform):
    driver = webdriver.Chrome()  # Requires chromedriver
    try:
        driver.get(url)
        time.sleep(3)  # Wait for page to load
        
        price_element = driver.find_element(By.CSS_SELECTOR, '.price')
        price_text = price_element.text
        
        return float(price_text.replace('¥', '').replace(',', ''))
    finally:
        driver.quit()
```

---

## Setting Up Twitter API

### 1. Create a Twitter Developer Account

1. Go to [Twitter Developer Portal](https://developer.twitter.com/)
2. Sign in with your Twitter account
3. Apply for a developer account (may take 1-2 days for approval)

### 2. Create a New App

1. In the Developer Portal, click "Create Project"
2. Name your project (e.g., "PriceDive")
3. Select "Hobbyist" or "Making a bot"
4. Create an app within the project

### 3. Generate API Keys

1. Go to your app's "Keys and tokens" tab
2. Generate:
   - **API Key** (Consumer Key)
   - **API Secret Key** (Consumer Secret)
   - **Access Token**
   - **Access Token Secret**

### 4. Set Permissions

1. Go to "User authentication settings"
2. Set **App permissions** to "Read and Write"
3. Save changes

### 5. Update `config.json`

Copy your keys into the configuration file:
```json
"twitter_api_keys": {
  "consumer_key": "abc123xyz...",
  "consumer_secret": "def456uvw...",
  "access_token": "123-abc...",
  "access_token_secret": "ghi789rst..."
}
```

⚠️ **Security Warning**: Never commit `config.json` with real API keys to public repositories! Add it to `.gitignore`.

---

## Scheduling Automated Runs

### Windows Task Scheduler

1. Open **Task Scheduler** (search in Start menu)
2. Click "Create Basic Task"
3. Name: "PriceDive Daily Tracker"
4. Trigger: Daily at 10:00 AM (or your preferred time)
5. Action: Start a program
   - Program: `C:\Path\To\Python\python.exe`
   - Arguments: `C:\Path\To\pricedive.py`
   - Start in: `C:\Path\To\Project\Folder`
6. Finish

### Linux/Mac (cron)

Edit crontab:
```bash
crontab -e
```

Add this line to run daily at 10:00 AM:
```bash
0 10 * * * cd /path/to/pricedive && /usr/bin/python3 pricedive.py >> /path/to/pricedive.log 2>&1
```

### Check Logs

Monitor execution:
```bash
# Linux/Mac
tail -f /path/to/pricedive.log

# Windows
# Check Task Scheduler history
```

---

## Database Structure

### Table: `prices`

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| timestamp | TEXT | ISO format datetime of record |
| product_name | TEXT | Name of the product |
| platform | TEXT | Platform name (Taobao, JD, etc.) |
| price | REAL | Price in CNY |

### Query Examples

**View all prices for a product:**
```sql
SELECT * FROM prices 
WHERE product_name = 'iPhone 15 Pro 256GB' 
ORDER BY timestamp DESC;
```

**Calculate average price per platform:**
```sql
SELECT platform, AVG(price) as avg_price 
FROM prices 
WHERE product_name = 'iPhone 15 Pro 256GB' 
GROUP BY platform;
```

**Find lowest price:**
```sql
SELECT platform, MIN(price) as lowest_price, timestamp
FROM prices
WHERE product_name = 'iPhone 15 Pro 256GB'
GROUP BY platform;
```

### Access Database

```bash
# Open database
sqlite3 prices.db

# View tables
.tables

# View schema
.schema prices

# Query data
SELECT * FROM prices LIMIT 10;

# Exit
.exit
```

---

## Troubleshooting

### Issue: "No module named 'httpx'"

**Solution:**
```bash
pip install httpx
```

### Issue: "Twitter authentication failed"

**Causes:**
1. Invalid API keys
2. App permissions not set to "Read and Write"
3. Keys expired or revoked

**Solution:**
1. Regenerate keys in Twitter Developer Portal
2. Update `config.json` with new keys
3. Verify app permissions

### Issue: "Price not found on page"

**Causes:**
1. Website structure changed
2. Page requires login
3. Anti-scraping measures blocking access
4. JavaScript-rendered content

**Solution:**
1. Inspect page again and update CSS selectors
2. Add cookies/authentication if needed
3. Improve headers and add delays
4. Use Selenium for dynamic content

### Issue: "Database locked"

**Cause:** Multiple processes accessing database simultaneously

**Solution:**
```python
# In pricedive.py, add timeout
conn = sqlite3.connect(db_path, timeout=30)
```

### Issue: Chart not displaying Chinese characters

**Solution:**
```python
# Add at top of script
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
```

### Issue: "HTTP 403 Forbidden"

**Cause:** Website blocking the scraper

**Solution:**
1. Add better User-Agent headers
2. Add Referer header
3. Use delays between requests
4. Consider using proxies
5. Check website's robots.txt

---

## Best Practices

### 1. Respect Websites
- Check `robots.txt` before scraping
- Add delays between requests (2-5 seconds)
- Don't overload servers
- Use official APIs when available

### 2. Data Backup
```bash
# Backup database regularly
cp prices.db prices_backup_$(date +%Y%m%d).db
```

### 3. Error Logging
Redirect output to log file:
```bash
python pricedive.py >> pricedive.log 2>&1
```

### 4. Monitor Performance
- Check database size periodically
- Archive old data if needed
- Monitor Twitter API rate limits (300 tweets per 3 hours)

### 5. Security
- Never commit API keys to version control
- Use environment variables for sensitive data
- Restrict database file permissions

---

## Advanced Customizations

### Add Email Notifications

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email_notification(message, image_path):
    msg = MIMEMultipart()
    msg['Subject'] = 'PriceDive Daily Report'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'recipient@example.com'
    
    msg.attach(MIMEText(message, 'plain'))
    
    with open(image_path, 'rb') as f:
        img = MIMEImage(f.read())
        msg.attach(img)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@gmail.com', 'your_app_password')
        smtp.send_message(msg)
```

### Track Multiple Products

Modify `config.json`:
```json
{
  "products": [
    {
      "name": "iPhone 15 Pro",
      "targets": [...]
    },
    {
      "name": "iPad Air",
      "targets": [...]
    }
  ]
}
```

Update `main()` to loop through products.

### Add Price Alerts

```python
def check_price_alert(platform, current_price, threshold):
    if current_price < threshold:
        send_alert(f"Price drop on {platform}! Now ¥{current_price}")
```

---

## Legal Disclaimer

This tool is for **educational and personal use only**. 

- Web scraping may violate websites' Terms of Service
- Some jurisdictions restrict automated data collection
- Always respect robots.txt and rate limits
- Consider using official APIs when available
- The authors are not responsible for misuse

---

## Support

For issues or questions:
1. Check this guide
2. Review the code comments in `pricedive.py`
3. Check the GitHub Issues page
4. Search for similar problems online

---

**Happy price tracking! 🎉**

