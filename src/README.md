# 源代码目录 | Source Code Directory

本目录包含PriceDive的所有Python源代码。  
This directory contains all Python source code for PriceDive.

---

## 📝 文件说明 | Files

### `pricedive.py` - 主程序
**功能 | Features**:
- ✅ 价格抓取（当前为模拟模式）
- ✅ SQLite数据库管理
- ✅ 数据可视化（matplotlib图表）
- ✅ 价格变化计算
- ✅ Twitter集成

**运行 | Run**:
```bash
# 从项目根目录运行 | Run from project root
python src/pricedive.py
```

---

### `generate_hook_chart.py` - 图表生成器
**功能 | Features**:
- ✅ 生成V型价格曲线图
- ✅ 展示"先涨后降"套路
- ✅ 用于项目宣传

**运行 | Run**:
```bash
# 从项目根目录运行 | Run from project root
python src/generate_hook_chart.py
```

**输出 | Output**: `examples/v_curve_example.png`

---

## 🔧 开发说明 | Development Notes

### 默认路径 | Default Paths
代码中使用的默认路径：
- 配置: `config/config.json`
- 数据库: `data/prices.db`
- 输出图表: `examples/price_trend.png`

### 模块结构 | Module Structure
```python
pricedive.py:
├── Database Functions
│   ├── setup_database()
│   ├── save_price_to_db()
│   └── get_price_history()
├── Configuration
│   └── load_config()
├── Web Scraping
│   └── fetch_price()  # ⚠️ 模拟模式 | Simulation mode
├── Data Analysis
│   └── calculate_price_change()
├── Visualization
│   └── create_plot()
├── Twitter Integration
│   └── post_to_twitter()
└── Main Orchestration
    └── main()
```

---

## 📚 更多信息 | More Information

- 详细使用教程: [`docs/USAGE.md`](../docs/USAGE.md)
- 快速开始: [`docs/START_HERE.md`](../docs/START_HERE.md)

