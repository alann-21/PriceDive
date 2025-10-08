# 脚本目录 | Scripts Directory

本目录包含PriceDive的启动脚本和工具脚本。  
This directory contains launch scripts and utility scripts for PriceDive.

---

## 📝 文件说明 | Files

### `run_pricedive.bat` - Windows启动脚本
**适用系统 | For**: Windows 10/11

**使用方法 | Usage**:
```bash
# 方式一：双击运行 | Method 1: Double-click
# 直接在文件管理器中双击 run_pricedive.bat

# 方式二：命令行运行 | Method 2: Command line
scripts\run_pricedive.bat
```

**功能 | Features**:
- ✅ 自动检查Python是否安装
- ✅ 验证配置文件是否存在
- ✅ 运行主程序
- ✅ 显示生成的文件
- ✅ 等待用户按键（便于查看输出）

---

### `run_pricedive.sh` - Linux/Mac启动脚本
**适用系统 | For**: Linux, macOS, Unix-like systems

**使用方法 | Usage**:
```bash
# 首次使用需要添加执行权限 | First time: add execute permission
chmod +x scripts/run_pricedive.sh

# 然后运行 | Then run
./scripts/run_pricedive.sh
```

**功能 | Features**:
- ✅ 自动检查Python 3是否安装
- ✅ 验证配置文件是否存在
- ✅ 支持虚拟环境自动激活
- ✅ 运行主程序
- ✅ 显示生成的文件

---

## 🚀 快速开始 | Quick Start

### Windows用户 | Windows Users
1. 确保已安装Python 3.8+
2. 双击 `run_pricedive.bat`
3. 查看运行结果

### Linux/Mac用户 | Linux/Mac Users
1. 打开终端
2. 运行以下命令:
```bash
cd /path/to/pricedive
chmod +x scripts/run_pricedive.sh
./scripts/run_pricedive.sh
```

---

## 🔧 脚本功能详解 | Script Features Explained

### 1. 环境检查 | Environment Check
脚本会自动检查：
- Python是否已安装
- 配置文件是否存在
- 依赖包是否安装

### 2. 自动运行 | Auto Execution
脚本会：
- 切换到正确的目录
- 执行主程序
- 捕获输出信息

### 3. 结果展示 | Result Display
运行完成后显示：
- 数据库文件位置
- 生成的图表位置
- 执行状态

---

## 🎯 高级用法 | Advanced Usage

### 添加日志记录 | Add Logging
编辑脚本，添加日志输出：

**Windows (run_pricedive.bat)**:
```batch
python src\pricedive.py >> logs\pricedive_%date:~0,4%%date:~5,2%%date:~8,2%.log 2>&1
```

**Linux/Mac (run_pricedive.sh)**:
```bash
python3 src/pricedive.py >> logs/pricedive_$(date +%Y%m%d).log 2>&1
```

### 静默运行 | Silent Mode
不显示输出，仅记录日志：

**Windows**:
```batch
python src\pricedive.py > nul 2>&1
```

**Linux/Mac**:
```bash
python3 src/pricedive.py > /dev/null 2>&1
```

### 添加错误通知 | Add Error Notification
```bash
#!/bin/bash
if ! python3 src/pricedive.py; then
    echo "PriceDive运行失败！" | mail -s "PriceDive Error" your@email.com
fi
```

---

## ⏰ 自动化运行 | Automated Execution

### Windows任务计划程序 | Windows Task Scheduler

1. 打开"任务计划程序" | Open "Task Scheduler"
2. 创建基本任务 | Create Basic Task
3. 设置触发器 | Set Trigger:
   - 每天 | Daily
   - 上午10:00 | 10:00 AM
4. 设置操作 | Set Action:
   - 程序：`C:\Windows\System32\cmd.exe`
   - 参数：`/c "cd /d C:\path\to\pricedive && scripts\run_pricedive.bat"`
5. 完成 | Finish

**或使用脚本路径 | Or use script path**:
- 程序：`C:\path\to\pricedive\scripts\run_pricedive.bat`
- 起始于：`C:\path\to\pricedive`

---

### Linux/Mac Cron任务 | Linux/Mac Cron Job

```bash
# 编辑crontab | Edit crontab
crontab -e

# 添加以下行（每天10:00运行）| Add following line (run daily at 10:00)
0 10 * * * cd /path/to/pricedive && ./scripts/run_pricedive.sh

# 或指定完整路径 | Or specify full path
0 10 * * * /path/to/pricedive/scripts/run_pricedive.sh

# 带日志记录 | With logging
0 10 * * * cd /path/to/pricedive && ./scripts/run_pricedive.sh >> logs/cron.log 2>&1
```

**Cron时间格式说明 | Cron Time Format**:
```
分 时 日 月 周 命令
* * * * * command

例子 | Examples:
0 10 * * * - 每天10:00 | Daily at 10:00
0 */6 * * * - 每6小时 | Every 6 hours
0 10 * * 1-5 - 工作日10:00 | Weekdays at 10:00
```

---

## 🐛 故障排除 | Troubleshooting

### 问题1: "Python未找到" | "Python not found"
**解决方案 | Solution**:
```bash
# Windows: 安装Python并添加到PATH | Install Python and add to PATH
# 下载: https://www.python.org/downloads/

# Linux: 安装Python3 | Install Python3
sudo apt-get install python3  # Ubuntu/Debian
sudo yum install python3       # CentOS/RHEL

# Mac: 使用Homebrew | Use Homebrew
brew install python3
```

---

### 问题2: "权限被拒绝" | "Permission denied"
**Linux/Mac解决方案 | Linux/Mac Solution**:
```bash
chmod +x scripts/run_pricedive.sh
```

---

### 问题3: "配置文件未找到" | "Config file not found"
**解决方案 | Solution**:
```bash
# 复制配置模板 | Copy config template
cp config/config.json.example config/config.json

# 然后编辑配置文件 | Then edit the config file
```

---

### 问题4: 脚本运行但程序报错 | Script runs but program errors
**检查步骤 | Check**:
1. 依赖是否安装：`pip install -r requirements.txt`
2. 配置文件是否正确
3. 查看详细错误信息

---

## 🔐 安全建议 | Security Tips

### 1. 脚本权限 | Script Permissions
```bash
# Linux/Mac: 限制执行权限 | Limit execute permissions
chmod 700 scripts/run_pricedive.sh  # 只有所有者可执行 | Owner only
```

### 2. 日志安全 | Log Security
```bash
# 创建日志目录并限制权限 | Create log directory with restricted permissions
mkdir -p logs
chmod 700 logs
```

### 3. 环境隔离 | Environment Isolation
```bash
# 使用虚拟环境 | Use virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

## 📊 脚本输出示例 | Script Output Example

### 成功运行 | Successful Run
```
============================================================
PriceDive - E-commerce Price Tracker
============================================================

Step 1: Setting up database...
✓ Database initialized: data/prices.db

Step 2: Loading configuration...
✓ Configuration loaded from config/config.json
   Tracking: iPhone 15 Pro 256GB
   Platforms: 3

Step 3: Fetching current prices...
⚠️  Simulated scraping from Taobao: https://...
✓ Saved: Taobao - ¥899.00
...

============================================================
PriceDive run completed successfully!
============================================================

Generated files:
  - data/prices.db (database)
  - examples/price_trend.png (chart)
```

---

## 🛠️ 自定义脚本 | Customize Scripts

### 添加预检查 | Add Pre-checks
```bash
# 检查磁盘空间 | Check disk space
if [ $(df -k . | tail -1 | awk '{print $4}') -lt 10000 ]; then
    echo "警告：磁盘空间不足！| Warning: Low disk space!"
fi
```

### 添加通知 | Add Notifications
```bash
# Linux: 使用notify-send | Use notify-send
notify-send "PriceDive" "价格追踪完成！| Price tracking completed!"

# Mac: 使用osascript | Use osascript
osascript -e 'display notification "价格追踪完成！" with title "PriceDive"'
```

---

## 📚 更多信息 | More Information

- 完整使用教程: [`docs/USAGE.md`](../docs/USAGE.md)
- 快速开始: [`docs/START_HERE.md`](../docs/START_HERE.md)
- 项目结构: [`PROJECT_STRUCTURE.md`](../PROJECT_STRUCTURE.md)

