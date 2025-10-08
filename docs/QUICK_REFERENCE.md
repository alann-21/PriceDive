# PriceDive - Quick Reference Card

## 🚀 Quick Commands

### First Time Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure
cp config.json.example config.json
# Edit config.json with your settings

# 3. Test run
python pricedive.py
```

### Daily Operations
```bash
# Run tracker
python pricedive.py

# Generate hook chart
python generate_hook_chart.py

# Check database
sqlite3 prices.db "SELECT * FROM prices ORDER BY timestamp DESC LIMIT 10;"
```

### Windows Users
```batch
run_pricedive.bat
```

### Linux/Mac Users
```bash
chmod +x run_pricedive.sh
./run_pricedive.sh
```

---

## 📁 File Quick Reference

| File | Purpose |
|------|---------|
| `pricedive.py` | Main application |
| `generate_hook_chart.py` | Create V-curve chart |
| `config.json` | Your settings (edit this) |
| `README.md` | Start here |
| `USAGE.md` | Detailed guide |
| `prices.db` | Data storage |
| `price_trend.png` | Generated chart |

---

## ⚙️ Configuration Essentials

### config.json Structure
```json
{
  "product_name": "Your Product",
  "targets": [
    {"platform": "Platform Name", "url": "Product URL"}
  ],
  "twitter_api_keys": {
    "consumer_key": "...",
    "consumer_secret": "...",
    "access_token": "...",
    "access_token_secret": "..."
  }
}
```

---

## 🔧 Common Tasks

### Add a Platform
Edit `config.json`:
```json
"targets": [
  {"platform": "New Platform", "url": "https://..."}
]
```

### View Data
```bash
sqlite3 prices.db
> SELECT * FROM prices;
> .quit
```

### Clear Data
```bash
rm prices.db
python pricedive.py  # Recreates database
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not found | `pip install <module>` |
| Config not found | Create `config.json` |
| Twitter fails | Check API keys |
| Price not scraped | Update CSS selectors |

---

## 📊 Key Functions

| Function | Purpose |
|----------|---------|
| `setup_database()` | Initialize DB |
| `load_config()` | Load settings |
| `fetch_price()` | Scrape price |
| `save_price_to_db()` | Store data |
| `create_plot()` | Generate chart |
| `post_to_twitter()` | Tweet update |

---

## 🔗 Important Links

- **Twitter Dev Portal**: https://developer.twitter.com/
- **Python Docs**: https://docs.python.org/3/
- **matplotlib**: https://matplotlib.org/
- **SQLite**: https://www.sqlite.org/

---

## 📅 Automation

### Windows (Task Scheduler)
Program: `python.exe`
Arguments: `C:\path\to\pricedive.py`
Schedule: Daily 10:00 AM

### Linux/Mac (cron)
```bash
crontab -e
# Add: 0 10 * * * cd /path/to/project && python3 pricedive.py
```

---

## 🎯 Project Files at a Glance

```
✅ pricedive.py           → Main application
✅ generate_hook_chart.py → Hook chart generator
✅ config.json            → Your configuration
✅ requirements.txt       → Dependencies
✅ README.md              → Quick start guide
✅ USAGE.md               → Detailed manual
✅ PROJECT_SUMMARY.md     → Architecture docs
✅ DELIVERY_CHECKLIST.md  → Delivery verification
✅ QUICK_REFERENCE.md     → This file
✅ run_pricedive.bat      → Windows launcher
✅ run_pricedive.sh       → Linux/Mac launcher
✅ .gitignore             → Git security
```

---

## 💡 Pro Tips

1. **Test First**: Run in simulation mode before implementing real scraping
2. **Backup Data**: Copy `prices.db` regularly
3. **Monitor Logs**: Redirect output to log files
4. **Rate Limit**: Add delays between requests (2-5 seconds)
5. **Respect Sites**: Check robots.txt before scraping

---

## 🔐 Security Reminders

- ❌ Never commit `config.json` with real API keys
- ✅ Use `config.json.example` for version control
- ✅ Add `config.json` to `.gitignore`
- ✅ Regenerate API keys if exposed

---

## 📝 Need Help?

1. Check **USAGE.md** for detailed guides
2. Review **PROJECT_SUMMARY.md** for architecture
3. Search the code comments in `pricedive.py`
4. Test with simulation mode first

---

**Quick Start in 3 Steps:**
1. `pip install -r requirements.txt`
2. Edit `config.json`
3. `python pricedive.py`

**That's it! 🎉**

