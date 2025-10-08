# PriceDive 项目结构说明 | Project Structure

本文档说明了重新组织后的项目目录结构。  
This document explains the reorganized project directory structure.

---

## 📁 目录结构 | Directory Structure

```
pricedive/
├── 📂 src/                    # 源代码 | Source Code
│   ├── pricedive.py          # 主程序 | Main application
│   └── generate_hook_chart.py # 图表生成器 | Chart generator
│
├── 📂 config/                 # 配置文件 | Configuration Files
│   ├── config.json           # 用户配置（请勿提交到Git）| User config (DO NOT commit)
│   └── config.json.example   # 配置模板 | Config template
│
├── 📂 docs/                   # 文档 | Documentation
│   ├── START_HERE.md         # ⭐ 快速开始指南 | Quick start guide
│   ├── QUICK_REFERENCE.md    # 命令速查表 | Command cheat sheet
│   ├── USAGE.md              # 详细使用教程 | Complete usage guide
│   ├── PROJECT_SUMMARY.md    # 技术文档 | Technical documentation
│   └── DELIVERY_CHECKLIST.md # 交付清单 | Delivery checklist
│
├── 📂 scripts/                # 启动脚本 | Launch Scripts
│   ├── run_pricedive.bat     # Windows启动脚本 | Windows launcher
│   └── run_pricedive.sh      # Linux/Mac启动脚本 | Linux/Mac launcher
│
├── 📂 examples/               # 示例输出 | Example Outputs
│   ├── v_curve_example.png   # 宣传图表 | Promotional chart
│   └── price_trend.png       # 价格趋势图（自动生成）| Price trend chart (auto-generated)
│
├── 📂 data/                   # 数据库 | Database
│   └── prices.db             # SQLite数据库（自动生成）| SQLite DB (auto-generated)
│
├── 📜 README.md               # 项目主页（中英双语）| Project homepage (bilingual)
├── 📜 PROJECT_STRUCTURE.md    # 本文件 | This file
├── 📜 LICENSE                 # MIT开源协议 | MIT License
├── 📜 requirements.txt        # Python依赖 | Python dependencies
└── 📜 .gitignore              # Git忽略规则 | Git ignore rules
```

---

## 📖 各目录说明 | Directory Descriptions

### 📂 `src/` - 源代码目录
**用途**: 存放所有Python源代码文件  
**Purpose**: Contains all Python source code files

**文件列表 | Files**:
- `pricedive.py` - 主应用程序，包含所有核心功能
- `generate_hook_chart.py` - 独立的V型价格曲线生成器

**运行方式 | How to Run**:
```bash
# 从项目根目录运行 | Run from project root
python src/pricedive.py
python src/generate_hook_chart.py
```

---

### 📂 `config/` - 配置目录
**用途**: 存放所有配置文件  
**Purpose**: Contains all configuration files

**文件列表 | Files**:
- `config.json` - 实际使用的配置文件（包含API密钥，已在.gitignore中）
- `config.json.example` - 配置文件模板（可安全提交到Git）

**重要提示 | Important**:
- ⚠️ `config.json` 包含敏感信息，不要提交到版本控制
- ✅ 修改 `config.json.example` 后复制为 `config.json` 使用

**首次使用 | First Time Setup**:
```bash
# 复制配置模板 | Copy config template
cp config/config.json.example config/config.json
# 然后编辑 config/config.json | Then edit config/config.json
```

---

### 📂 `docs/` - 文档目录
**用途**: 存放所有项目文档  
**Purpose**: Contains all project documentation

**文档清单 | Document List**:

| 文件 | 说明 | 推荐阅读顺序 |
|------|------|------------|
| `START_HERE.md` ⭐ | 新手快速上手指南 | 1️⃣ 第一个读 |
| `QUICK_REFERENCE.md` | 常用命令速查表 | 2️⃣ 日常参考 |
| `USAGE.md` | 完整使用教程 | 3️⃣ 深入学习 |
| `PROJECT_SUMMARY.md` | 技术架构文档 | 4️⃣ 开发者参考 |
| `DELIVERY_CHECKLIST.md` | 项目交付清单 | 5️⃣ 验收参考 |

---

### 📂 `scripts/` - 脚本目录
**用途**: 存放启动脚本和工具脚本  
**Purpose**: Contains launch scripts and utility scripts

**脚本列表 | Scripts**:
- `run_pricedive.bat` - Windows用户双击运行
- `run_pricedive.sh` - Linux/Mac用户执行运行

**使用方法 | Usage**:
```bash
# Windows 用户
scripts\run_pricedive.bat

# Linux/Mac 用户
chmod +x scripts/run_pricedive.sh
./scripts/run_pricedive.sh
```

**功能 | Features**:
- ✅ 自动检查Python环境
- ✅ 验证配置文件存在
- ✅ 运行主程序
- ✅ 显示生成的文件

---

### 📂 `examples/` - 示例输出目录
**用途**: 存放示例图表和自动生成的输出  
**Purpose**: Contains example charts and auto-generated outputs

**文件列表 | Files**:
- `v_curve_example.png` - 宣传用的V型价格曲线（手动生成）
- `price_trend.png` - 程序运行后自动生成的价格趋势图

**说明 | Notes**:
- `v_curve_example.png` 是项目宣传图，已提交到Git
- `price_trend.png` 每次运行都会重新生成，不提交到Git

---

### 📂 `data/` - 数据目录
**用途**: 存放数据库文件  
**Purpose**: Contains database files

**文件 | Files**:
- `prices.db` - SQLite数据库（首次运行时自动创建）

**说明 | Notes**:
- 数据库文件不提交到Git（已在.gitignore中）
- 首次运行程序时会自动创建
- 包含所有历史价格数据

**数据库管理 | Database Management**:
```bash
# 查看数据库 | View database
sqlite3 data/prices.db
> SELECT * FROM prices;
> .quit

# 备份数据库 | Backup database
cp data/prices.db data/prices_backup_$(date +%Y%m%d).db

# 清空数据库 | Clear database
rm data/prices.db
# 下次运行时会自动重新创建 | Will be recreated on next run
```

---

## 🚀 快速开始 | Quick Start

### 1️⃣ 安装依赖 | Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ 配置设置 | Configure Settings
```bash
# 复制配置模板 | Copy config template
cp config/config.json.example config/config.json

# 编辑配置文件 | Edit config file
# 修改产品URL和Twitter API密钥 | Modify product URLs and Twitter API keys
```

### 3️⃣ 运行程序 | Run the App
```bash
# 方式一：直接运行 | Method 1: Direct run
python src/pricedive.py

# 方式二：使用脚本 | Method 2: Use scripts
./scripts/run_pricedive.sh    # Linux/Mac
scripts\run_pricedive.bat      # Windows
```

### 4️⃣ 查看结果 | View Results
- 📊 图表: `examples/price_trend.png`
- 🗄️ 数据库: `data/prices.db`

---

## 📝 文件路径变更说明 | File Path Changes

重组后，以下路径已更改：

### 旧路径 → 新路径 | Old Path → New Path

**Python 源文件 | Python Source**:
```
pricedive.py → src/pricedive.py
generate_hook_chart.py → src/generate_hook_chart.py
```

**配置文件 | Config Files**:
```
config.json → config/config.json
config.json.example → config/config.json.example
```

**文档文件 | Documentation**:
```
START_HERE.md → docs/START_HERE.md
QUICK_REFERENCE.md → docs/QUICK_REFERENCE.md
USAGE.md → docs/USAGE.md
PROJECT_SUMMARY.md → docs/PROJECT_SUMMARY.md
DELIVERY_CHECKLIST.md → docs/DELIVERY_CHECKLIST.md
```

**脚本文件 | Scripts**:
```
run_pricedive.bat → scripts/run_pricedive.bat
run_pricedive.sh → scripts/run_pricedive.sh
```

**输出文件 | Output Files**:
```
price_trend.png → examples/price_trend.png
v_curve_example.png → examples/v_curve_example.png
prices.db → data/prices.db
```

---

## 🔧 开发者注意事项 | Developer Notes

### 导入路径 | Import Paths
重组后，所有默认路径已在代码中更新：

```python
# 配置文件 | Config
load_config("config/config.json")

# 数据库 | Database
setup_database("data/prices.db")

# 输出图表 | Output Chart
create_plot(..., output_path="examples/price_trend.png")
```

### Git 提交 | Git Commits
以下文件不会被提交到Git：
- `config/config.json` - 包含API密钥
- `data/*.db` - 数据库文件
- `examples/price_trend.png` - 自动生成的图表
- `__pycache__/` - Python缓存

---

## 🎯 项目结构优势 | Structure Benefits

### ✅ 清晰分类 | Clear Organization
- 源代码、配置、文档、数据分离
- 一目了然的文件用途

### ✅ 易于维护 | Easy Maintenance
- 修改代码只需关注 `src/` 目录
- 配置管理集中在 `config/` 目录

### ✅ 开发友好 | Developer Friendly
- 标准的Python项目结构
- 便于扩展和添加新功能

### ✅ 部署方便 | Easy Deployment
- 可以只部署需要的目录
- 数据和配置分离便于备份

### ✅ 文档齐全 | Complete Documentation
- 所有文档集中在 `docs/` 目录
- 主README保留在根目录便于GitHub展示

---

## 📚 更多信息 | More Information

- 📖 **快速开始**: 阅读 [`docs/START_HERE.md`](docs/START_HERE.md)
- 🔍 **命令速查**: 查看 [`docs/QUICK_REFERENCE.md`](docs/QUICK_REFERENCE.md)
- 📘 **完整教程**: 参考 [`docs/USAGE.md`](docs/USAGE.md)
- 🏗️ **技术架构**: 了解 [`docs/PROJECT_SUMMARY.md`](docs/PROJECT_SUMMARY.md)

---

## 🎉 总结 | Summary

新的项目结构使PriceDive更加专业和易于维护。所有文件都已按功能分类，路径也已在代码中更新。你可以像以前一样使用项目，只需注意文件路径的变化。

The new project structure makes PriceDive more professional and maintainable. All files are now organized by function, and paths have been updated in the code. You can use the project as before, just note the file path changes.

**祝你使用愉快！| Happy coding! 🎯**

