#!/bin/bash
# PriceDive - Run Script for Linux/Mac
# This script runs the PriceDive price tracker

echo "============================================================"
echo "PriceDive - E-commerce Price Tracker"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check if config.json exists
if [ ! -f config/config.json ]; then
    echo "Error: config/config.json not found!"
    echo "Please copy config/config.json.example to config/config.json and configure it."
    exit 1
fi

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Run the script
echo "Running PriceDive..."
echo ""
python3 src/pricedive.py

echo ""
echo "============================================================"
echo "PriceDive execution completed!"
echo "============================================================"
echo ""
echo "Generated files:"
[ -f data/prices.db ] && echo "  - data/prices.db (database)"
[ -f examples/price_trend.png ] && echo "  - examples/price_trend.png (chart)"
echo ""

