#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PriceDive - E-commerce Price Tracker
Monitors product prices across multiple platforms and posts updates to Twitter
"""

import sqlite3
import json
import random
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Set matplotlib backend before importing pyplot
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Import httpx for async-friendly HTTP requests
try:
    import httpx
except ImportError:
    print("Warning: httpx not installed. Install with: pip install httpx")
    httpx = None

# Import tweepy for Twitter API
try:
    import tweepy
except ImportError:
    print("Warning: tweepy not installed. Install with: pip install tweepy")
    tweepy = None


# ============================================================================
# DATABASE FUNCTIONS
# ============================================================================

def setup_database(db_path: str = "data/prices.db") -> None:
    """
    Initialize the SQLite database and create the prices table if it doesn't exist.
    
    Args:
        db_path: Path to the SQLite database file
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table with proper schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            product_name TEXT NOT NULL,
            platform TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print(f"✓ Database initialized: {db_path}")


def save_price_to_db(product_name: str, platform: str, price: float, 
                     db_path: str = "data/prices.db") -> None:
    """
    Save a new price entry to the database.
    
    Args:
        product_name: Name of the product
        platform: E-commerce platform name
        price: Current price of the product
        db_path: Path to the SQLite database file
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    timestamp = datetime.now().isoformat()
    
    cursor.execute("""
        INSERT INTO prices (timestamp, product_name, platform, price)
        VALUES (?, ?, ?, ?)
    """, (timestamp, product_name, platform, price))
    
    conn.commit()
    conn.close()
    print(f"✓ Saved: {platform} - ¥{price:.2f}")


def get_price_history(product_name: str, db_path: str = "data/prices.db") -> List[Dict]:
    """
    Retrieve all historical price data for a product.
    
    Args:
        product_name: Name of the product to query
        db_path: Path to the SQLite database file
        
    Returns:
        List of dictionaries containing price history
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT timestamp, platform, price
        FROM prices
        WHERE product_name = ?
        ORDER BY timestamp ASC
    """, (product_name,))
    
    rows = cursor.fetchall()
    conn.close()
    
    history = []
    for row in rows:
        history.append({
            'timestamp': row[0],
            'platform': row[1],
            'price': row[2]
        })
    
    return history


# ============================================================================
# CONFIGURATION
# ============================================================================

def load_config(config_path: str = "config/config.json") -> Dict:
    """
    Load configuration from JSON file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Dictionary containing configuration settings
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print(f"✓ Configuration loaded from {config_path}")
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_path}' not found!")
        print("Please create config.json with your settings.")
        raise
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in configuration file: {e}")
        raise


# ============================================================================
# WEB SCRAPING (PLACEHOLDER)
# ============================================================================

def fetch_price(url: str, platform: str) -> float:
    """
    Fetch the current price from a product URL.
    
    ⚠️ IMPORTANT: This is a SIMULATION function that returns random prices.
    
    In a real implementation, you would:
    1. Use httpx to make HTTP requests:
       async with httpx.AsyncClient() as client:
           response = await client.get(url, headers=headers, timeout=30)
    
    2. Parse the HTML with BeautifulSoup or parsel:
       from bs4 import BeautifulSoup
       soup = BeautifulSoup(response.text, 'html.parser')
       price_element = soup.select_one('.price-class')  # Use actual CSS selector
       price = float(price_element.text.strip().replace('¥', '').replace(',', ''))
    
    3. Handle anti-scraping measures:
       - Add realistic User-Agent headers
       - Implement delays between requests
       - Use proxies if necessary
       - Handle CAPTCHAs or login requirements
    
    4. Handle errors gracefully:
       - Network timeouts
       - Changed page structure
       - Product not available
    
    Args:
        url: The product page URL
        platform: Name of the platform (for logging)
        
    Returns:
        The scraped price as a float
    """
    # SIMULATION: Generate random but realistic price variations
    # Base price around 500-1500, with small daily fluctuations
    base_price = 899.00
    variation = random.uniform(-50, 50)
    simulated_price = round(base_price + variation, 2)
    
    print(f"⚠️  Simulated scraping from {platform}: {url}")
    print(f"   (Replace this with actual scraping logic)")
    
    # Example of what real scraping might look like (commented out):
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        if httpx:
            with httpx.Client(timeout=30) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                # Parse HTML and extract price
                # This depends on the specific website structure
                # Example: price = parse_price_from_html(response.text, platform)
                pass
    except Exception as e:
        print(f"Error scraping {platform}: {e}")
        return None
    """
    
    return simulated_price


# ============================================================================
# DATA ANALYSIS
# ============================================================================

def calculate_price_change(platform: str, current_price: float, 
                          price_history: List[Dict]) -> Optional[float]:
    """
    Calculate the percentage change in price from the previous day.
    
    Args:
        platform: Name of the platform
        current_price: Current price
        price_history: List of historical price data
        
    Returns:
        Percentage change as a float, or None if no previous data
    """
    # Filter history for this platform
    platform_history = [h for h in price_history if h['platform'] == platform]
    
    if len(platform_history) < 1:
        return None
    
    # Get the previous price (most recent before current)
    previous_price = platform_history[-1]['price']
    
    if previous_price == 0:
        return None
    
    change = ((current_price - previous_price) / previous_price) * 100
    return round(change, 2)


# ============================================================================
# VISUALIZATION
# ============================================================================

def create_plot(price_history: List[Dict], product_name: str, 
                output_path: str = "examples/price_trend.png") -> None:
    """
    Generate a line chart showing price trends for all platforms.
    
    Args:
        price_history: List of historical price data
        product_name: Name of the product
        output_path: Path to save the generated chart
    """
    if not price_history:
        print("No price history available to plot.")
        return
    
    try:
        # Organize data by platform
        platforms = {}
        for entry in price_history:
            platform = entry['platform']
            if platform not in platforms:
                platforms[platform] = {'dates': [], 'prices': []}
            
            platforms[platform]['dates'].append(
                datetime.fromisoformat(entry['timestamp'])
            )
            platforms[platform]['prices'].append(entry['price'])
        
        # Create the plot
        plt.figure(figsize=(12, 6))
        
        # Define colors for different platforms
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
        
        # Plot each platform's price trend
        for idx, (platform, data) in enumerate(platforms.items()):
            color = colors[idx % len(colors)]
            plt.plot(data['dates'], data['prices'], 
                    marker='o', linewidth=2, markersize=6,
                    label=platform, color=color)
        
        # Formatting
        plt.title(f'Price Trend for {product_name}', 
                 fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Date', fontsize=12, fontweight='bold')
        plt.ylabel('Price (CNY)', fontsize=12, fontweight='bold')
        plt.legend(loc='best', frameon=True, shadow=True, fontsize=10)
        plt.grid(True, alpha=0.3, linestyle='--')
        
        # Format x-axis dates
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.gcf().autofmt_xdate()  # Rotate date labels
        
        # Tight layout to prevent label cutoff
        plt.tight_layout()
        
        # Save the figure
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Price trend chart saved: {output_path}")
    except Exception as e:
        print(f"Error creating plot: {e}")
        print("Continuing without chart generation...")


# ============================================================================
# TWITTER INTEGRATION
# ============================================================================

def post_to_twitter(message: str, image_path: str, config: Dict) -> bool:
    """
    Post a tweet with text and an image.
    
    Args:
        message: The tweet text
        image_path: Path to the image to attach
        config: Configuration dictionary containing Twitter API keys
        
    Returns:
        True if successful, False otherwise
    """
    if not tweepy:
        print("⚠️  Tweepy not installed. Skipping Twitter post.")
        print("   Install with: pip install tweepy")
        print(f"\nWould have posted:\n{message}")
        return False
    
    try:
        # Extract Twitter API keys from config
        twitter_keys = config.get('twitter_api_keys', {})
        consumer_key = twitter_keys.get('consumer_key')
        consumer_secret = twitter_keys.get('consumer_secret')
        access_token = twitter_keys.get('access_token')
        access_token_secret = twitter_keys.get('access_token_secret')
        
        # Check if keys are provided
        if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
            print("⚠️  Twitter API keys not configured in config.json")
            print(f"\nWould have posted:\n{message}")
            return False
        
        # Check if keys are still placeholders
        if 'YOUR_KEY' in consumer_key or 'YOUR_SECRET' in consumer_secret:
            print("⚠️  Twitter API keys are still placeholders. Please add your real keys.")
            print(f"\nWould have posted:\n{message}")
            return False
        
        # Authenticate with Twitter API v2
        client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        
        # For media upload, we also need API v1.1
        auth = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret,
            access_token, access_token_secret
        )
        api = tweepy.API(auth)
        
        # Upload media
        media = api.media_upload(image_path)
        
        # Post tweet with media
        client.create_tweet(text=message, media_ids=[media.media_id])
        
        print("✓ Successfully posted to Twitter!")
        return True
        
    except Exception as e:
        print(f"Error posting to Twitter: {e}")
        print(f"\nWould have posted:\n{message}")
        return False


# ============================================================================
# MAIN ORCHESTRATION
# ============================================================================

def main():
    """
    Main function that orchestrates the entire price tracking workflow.
    """
    print("=" * 60)
    print("PriceDive - E-commerce Price Tracker")
    print("=" * 60)
    print()
    
    # Step 1: Initialize database
    print("Step 1: Setting up database...")
    setup_database()
    print()
    
    # Step 2: Load configuration
    print("Step 2: Loading configuration...")
    config = load_config()
    product_name = config.get('product_name', 'Unknown Product')
    targets = config.get('targets', [])
    print(f"   Tracking: {product_name}")
    print(f"   Platforms: {len(targets)}")
    print()
    
    # Step 3: Scrape current prices
    print("Step 3: Fetching current prices...")
    current_prices = {}
    for target in targets:
        platform = target['platform']
        url = target['url']
        
        price = fetch_price(url, platform)
        if price is not None:
            current_prices[platform] = price
            save_price_to_db(product_name, platform, price)
    print()
    
    # Step 4: Get price history
    print("Step 4: Retrieving price history...")
    price_history = get_price_history(product_name)
    print(f"   Total records: {len(price_history)}")
    print()
    
    # Step 5: Calculate price changes
    print("Step 5: Calculating price changes...")
    price_changes = {}
    for platform, current_price in current_prices.items():
        change = calculate_price_change(platform, current_price, price_history)
        price_changes[platform] = change
        
        if change is not None:
            direction = "📈" if change > 0 else "📉" if change < 0 else "➡️"
            print(f"   {platform}: {direction} {change:+.2f}%")
        else:
            print(f"   {platform}: ➡️ First record")
    print()
    
    # Step 6: Generate visualization
    print("Step 6: Generating price trend chart...")
    create_plot(price_history, product_name)
    print()
    
    # Step 7: Compose tweet message
    print("Step 7: Composing tweet...")
    chart_path = "examples/price_trend.png"
    tweet_lines = [f"【PriceDive Daily Report】{product_name}"]
    
    for platform, price in current_prices.items():
        change = price_changes.get(platform)
        
        if change is None:
            change_text = "➡️ First record"
        elif change > 0:
            change_text = f"📈 +{change:.2f}%"
        elif change < 0:
            change_text = f"📉 {change:.2f}%"
        else:
            change_text = "➡️ No change"
        
        tweet_lines.append(f"{platform}: ¥{price:.2f} ({change_text})")
    
    tweet_lines.append("\nWhich platform is getting ready for the shopping festival?")
    tweet_lines.append("#PriceWatch #618 #Double11")
    
    tweet_message = "\n".join(tweet_lines)
    print(f"   Message preview:\n{tweet_message}")
    print()
    
    # Step 8: Post to Twitter
    print("Step 8: Posting to Twitter...")
    post_to_twitter(tweet_message, chart_path, config)
    print()
    
    print("=" * 60)
    print("PriceDive run completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

