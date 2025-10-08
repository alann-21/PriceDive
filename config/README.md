# 配置目录 | Configuration Directory

本目录包含PriceDive的配置文件。  
This directory contains configuration files for PriceDive.

---

## 📝 文件说明 | Files

### `config.json` - 实际配置文件
**⚠️ 重要 | Important**: 
- 包含API密钥等敏感信息
- 已在 `.gitignore` 中，不会提交到Git
- 从 `config.json.example` 复制并修改

**内容 | Contents**:
```json
{
  "product_name": "要追踪的商品名称",
  "targets": [
    {
      "platform": "平台名称",
      "url": "商品页面URL"
    }
  ],
  "twitter_api_keys": {
    "consumer_key": "你的密钥",
    "consumer_secret": "你的密钥",
    "access_token": "你的令牌",
    "access_token_secret": "你的令牌"
  }
}
```

---

### `config.json.example` - 配置模板
**用途 | Purpose**: 
- 配置文件模板
- 可以安全提交到Git
- 不包含真实的API密钥

---

## 🚀 首次设置 | First Time Setup

```bash
# 1. 复制模板文件 | Copy template file
cp config/config.json.example config/config.json

# 2. 编辑配置文件 | Edit config file
# 使用任何文本编辑器打开 config/config.json
# Open config/config.json with any text editor

# 3. 填写以下信息 | Fill in the following:
#    - product_name: 商品名称 | Product name
#    - targets[].url: 实际商品URL | Real product URLs
#    - twitter_api_keys: Twitter API密钥 | Twitter API keys
```

---

## 🔑 获取 Twitter API 密钥 | Get Twitter API Keys

1. 访问 [Twitter Developer Portal](https://developer.twitter.com/)
2. 创建开发者账号
3. 创建新应用
4. 生成API密钥
5. 将密钥复制到 `config.json`

**注意 | Note**: Twitter API 是可选的。没有API密钥程序也能正常运行，只是不会发推文。

---

## 🛡️ 安全建议 | Security Tips

- ✅ 定期更新API密钥
- ✅ 不要分享配置文件
- ✅ 不要截图包含密钥的内容
- ❌ 永远不要提交 `config.json` 到Git
- ❌ 不要在公开场合展示密钥

---

## 📋 配置示例 | Configuration Example

### 追踪单个产品 | Track Single Product
```json
{
  "product_name": "iPhone 15 Pro 256GB",
  "targets": [
    {"platform": "淘宝", "url": "https://item.taobao.com/item.htm?id=123456"},
    {"platform": "京东", "url": "https://item.jd.com/123456.html"},
    {"platform": "拼多多", "url": "https://mobile.yangkeduo.com/goods.html?goods_id=123456"}
  ]
}
```

### 添加更多平台 | Add More Platforms
只需在 `targets` 数组中添加更多项即可，无需修改代码！

---

## 🔧 高级配置 | Advanced Configuration

### 使用环境变量（可选）| Use Environment Variables (Optional)
```bash
# 设置环境变量 | Set environment variables
export TWITTER_CONSUMER_KEY="your_key"
export TWITTER_CONSUMER_SECRET="your_secret"
export TWITTER_ACCESS_TOKEN="your_token"
export TWITTER_ACCESS_TOKEN_SECRET="your_token_secret"

# 然后在代码中读取 | Then read in code
import os
api_key = os.getenv('TWITTER_CONSUMER_KEY')
```

---

## 📚 更多信息 | More Information

- Twitter API设置教程: [`docs/USAGE.md`](../docs/USAGE.md#setting-up-twitter-api)
- 完整配置指南: [`docs/START_HERE.md`](../docs/START_HERE.md)

