# 数据目录 | Data Directory

本目录存放PriceDive的SQLite数据库文件。  
This directory contains PriceDive's SQLite database files.

---

## 📝 文件说明 | Files

### `prices.db` - 价格数据库
**自动生成 | Auto-generated**: 首次运行 `pricedive.py` 时自动创建

**表结构 | Table Structure**:
```sql
CREATE TABLE prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    product_name TEXT NOT NULL,
    platform TEXT NOT NULL,
    price REAL NOT NULL
);
```

**字段说明 | Column Description**:
- `id`: 自增主键
- `timestamp`: 记录时间（ISO格式）
- `product_name`: 商品名称
- `platform`: 平台名称
- `price`: 价格（人民币）

---

## 🗄️ 数据库操作 | Database Operations

### 查看数据 | View Data
```bash
# 打开数据库 | Open database
sqlite3 data/prices.db

# 查看所有数据 | View all data
SELECT * FROM prices ORDER BY timestamp DESC;

# 查看特定商品 | View specific product
SELECT * FROM prices WHERE product_name = 'iPhone 15 Pro 256GB';

# 查看价格趋势 | View price trends
SELECT platform, AVG(price) as avg_price 
FROM prices 
GROUP BY platform;

# 退出 | Exit
.quit
```

### 备份数据库 | Backup Database
```bash
# 创建备份 | Create backup
cp data/prices.db data/prices_backup_$(date +%Y%m%d).db

# 或使用SQLite命令 | Or use SQLite command
sqlite3 data/prices.db ".backup data/prices_backup.db"
```

### 清空数据 | Clear Data
```bash
# 删除所有记录（保留表结构）| Delete all records (keep table structure)
sqlite3 data/prices.db "DELETE FROM prices;"

# 或删除整个数据库（下次运行时重新创建）| Or delete entire database (recreate on next run)
rm data/prices.db
```

---

## 📊 常用查询 | Common Queries

### 1. 查看最新价格 | View Latest Prices
```sql
SELECT platform, price, timestamp
FROM prices
WHERE product_name = '你的商品名'
ORDER BY timestamp DESC
LIMIT 10;
```

### 2. 查找最低价 | Find Lowest Price
```sql
SELECT platform, MIN(price) as lowest_price, timestamp
FROM prices
WHERE product_name = '你的商品名'
GROUP BY platform;
```

### 3. 计算平均价格 | Calculate Average Price
```sql
SELECT platform, 
       AVG(price) as avg_price,
       MIN(price) as min_price,
       MAX(price) as max_price,
       COUNT(*) as record_count
FROM prices
WHERE product_name = '你的商品名'
GROUP BY platform;
```

### 4. 查看价格变化 | View Price Changes
```sql
SELECT 
    timestamp,
    platform,
    price,
    LAG(price) OVER (PARTITION BY platform ORDER BY timestamp) as previous_price,
    price - LAG(price) OVER (PARTITION BY platform ORDER BY timestamp) as change
FROM prices
WHERE product_name = '你的商品名'
ORDER BY timestamp DESC;
```

---

## 📈 数据分析 | Data Analysis

### 导出到CSV | Export to CSV
```bash
sqlite3 -header -csv data/prices.db "SELECT * FROM prices;" > prices.csv
```

### 使用Python分析 | Analyze with Python
```python
import sqlite3
import pandas as pd

# 连接数据库 | Connect to database
conn = sqlite3.connect('data/prices.db')

# 读取数据 | Read data
df = pd.read_sql_query("SELECT * FROM prices", conn)

# 分析 | Analyze
print(df.describe())
print(df.groupby('platform')['price'].mean())

conn.close()
```

---

## 🔧 维护建议 | Maintenance Tips

### 定期备份 | Regular Backups
```bash
# 添加到cron任务 | Add to cron job
0 2 * * * cp /path/to/data/prices.db /path/to/backups/prices_$(date +\%Y\%m\%d).db
```

### 数据库优化 | Database Optimization
```bash
# 清理碎片，优化性能 | Vacuum database to optimize performance
sqlite3 data/prices.db "VACUUM;"
```

### 检查数据库完整性 | Check Database Integrity
```bash
sqlite3 data/prices.db "PRAGMA integrity_check;"
```

---

## ⚠️ 注意事项 | Important Notes

- 📦 **不提交到Git**: 数据库文件已在 `.gitignore` 中
- 💾 **定期备份**: 建议每周备份一次数据库
- 🔒 **权限设置**: 确保数据库文件只有你能访问
- 📊 **数据增长**: 每天3个平台约产生3条记录，一年约1000条

---

## 📏 数据库大小估算 | Database Size Estimation

| 天数 | 平台数 | 记录数 | 估计大小 |
|------|--------|--------|----------|
| 30天 | 3 | 90 | ~10 KB |
| 90天 | 3 | 270 | ~30 KB |
| 365天 | 3 | 1095 | ~100 KB |
| 3年 | 3 | 3285 | ~300 KB |

SQLite非常高效，即使存储多年数据也不会占用太多空间。

---

## 🛠️ 故障排除 | Troubleshooting

### 数据库锁定 | Database Locked
如果出现"database is locked"错误：
```bash
# 确保没有其他进程在使用数据库 | Ensure no other process is using the database
lsof data/prices.db  # Linux/Mac
```

### 数据库损坏 | Database Corrupted
如果数据库损坏：
```bash
# 尝试恢复 | Try to recover
sqlite3 data/prices.db ".dump" | sqlite3 data/prices_recovered.db
```

---

## 📚 更多信息 | More Information

- SQLite教程: https://www.sqlitetutorial.net/
- 完整使用指南: [`docs/USAGE.md`](../docs/USAGE.md)
- 项目结构说明: [`PROJECT_STRUCTURE.md`](../PROJECT_STRUCTURE.md)

