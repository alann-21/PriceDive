#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Hook Chart for PriceDive README
Creates a compelling V-shaped price curve showing "price hike before sale" pattern
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta


def generate_v_curve_chart(output_path: str = "examples/v_curve_example.png"):
    """
    Generate a V-shaped price curve chart demonstrating the common
    e-commerce tactic of raising prices before a sale.
    
    Args:
        output_path: Path to save the generated chart
    """
    # Define the date range (2 weeks before a shopping festival)
    start_date = datetime(2024, 11, 1)
    dates = [start_date + timedelta(days=i) for i in range(15)]
    
    # Define prices showing the classic "price hike before sale" pattern
    # Pattern: stable → gradual increase → spike → dramatic drop
    prices = [
        999,   # Day 1: Normal price
        999,   # Day 2: Stable
        1019,  # Day 3: Small increase
        1049,  # Day 4: Creeping up
        1099,  # Day 5: Higher
        1149,  # Day 6: Getting expensive
        1199,  # Day 7: Peak before "sale"
        1249,  # Day 8: Maximum inflation
        1229,  # Day 9: Slight dip
        1199,  # Day 10: Preparing for "discount"
        949,   # Day 11: "BIG SALE!" (still higher than original)
        929,   # Day 12: "Extra discount"
        899,   # Day 13: Finally lower than original
        879,   # Day 14: Best deal
        899,   # Day 15: Stabilizing
    ]
    
    # Create figure with Chinese font support
    plt.figure(figsize=(14, 7))
    
    # Try to use a Chinese font if available
    try:
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
        plt.rcParams['axes.unicode_minus'] = False
    except:
        # Fallback to default if Chinese fonts not available
        pass
    
    # Plot the price curve
    plt.plot(dates, prices, linewidth=3, color='#E74C3C', 
             marker='o', markersize=8, label='商品价格 (Product Price)')
    
    # Add annotations for key points
    # Highlight the "before sale" peak
    peak_idx = prices.index(max(prices))
    plt.annotate('涨价高峰\n(Price Peak)', 
                xy=(dates[peak_idx], prices[peak_idx]),
                xytext=(dates[peak_idx] - timedelta(days=2), prices[peak_idx] + 80),
                fontsize=12, fontweight='bold', color='#C0392B',
                arrowprops=dict(arrowstyle='->', color='#C0392B', lw=2),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))
    
    # Highlight the "sale" drop
    min_idx = prices.index(min(prices))
    plt.annotate('大促销！\n(Big Sale!)', 
                xy=(dates[min_idx], prices[min_idx]),
                xytext=(dates[min_idx] + timedelta(days=1), prices[min_idx] - 100),
                fontsize=12, fontweight='bold', color='#27AE60',
                arrowprops=dict(arrowstyle='->', color='#27AE60', lw=2),
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.7))
    
    # Add horizontal reference line for original price
    original_price = prices[0]
    plt.axhline(y=original_price, color='#3498DB', linestyle='--', 
               linewidth=2, alpha=0.7, label=f'原价 (Original: ¥{original_price})')
    
    # Fill areas to show price manipulation
    # Area above original price (price hike)
    plt.fill_between(dates[:peak_idx+1], original_price, prices[:peak_idx+1], 
                     where=[p >= original_price for p in prices[:peak_idx+1]],
                     alpha=0.2, color='red', label='涨价期 (Price Hike Period)')
    
    # Area below original price (actual savings)
    plt.fill_between(dates[10:], original_price, prices[10:], 
                     where=[p < original_price for p in prices[10:]],
                     alpha=0.2, color='green', label='真正优惠 (Real Discount)')
    
    # Formatting
    plt.title('商家套路实锤：先涨后降?\nProof of Seller\'s Trick: Price Hike Before Sale?', 
             fontsize=18, fontweight='bold', pad=20, color='#2C3E50')
    plt.xlabel('日期 (Date)', fontsize=14, fontweight='bold')
    plt.ylabel('价格 (Price ¥)', fontsize=14, fontweight='bold')
    plt.legend(loc='upper left', frameon=True, shadow=True, fontsize=11)
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Format x-axis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
    plt.gcf().autofmt_xdate()
    
    # Add a text box with statistics
    price_increase = max(prices) - original_price
    final_discount = original_price - min(prices)
    stats_text = (
        f"最高涨价: ¥{price_increase} (+{price_increase/original_price*100:.1f}%)\n"
        f"最终优惠: ¥{final_discount} (-{final_discount/original_price*100:.1f}%)\n"
        f"别被套路了！"
    )
    plt.text(0.98, 0.97, stats_text, transform=plt.gca().transAxes,
            fontsize=11, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Tight layout
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(output_path, dpi=200, bbox_inches='tight')
    print(f"✓ V-curve hook chart saved: {output_path}")
    print(f"   This chart is ready to use in your README to demonstrate")
    print(f"   the common e-commerce pricing tactics during shopping festivals!")
    
    plt.close()


if __name__ == "__main__":
    print("=" * 60)
    print("PriceDive - Hook Chart Generator")
    print("=" * 60)
    print()
    print("Generating a compelling V-shaped price curve chart...")
    print("This will show the 'price hike before sale' pattern.")
    print()
    
    generate_v_curve_chart()
    
    print()
    print("=" * 60)
    print("Chart generation complete!")
    print("=" * 60)

