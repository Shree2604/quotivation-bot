# 🤖 Quotivation Bot

[![GitHub Actions Status](https://img.shields.io/github/workflow/status/Shree2604/quotivation-bot/Daily%20Quote%20Generation?style=flat-square)](https://github.com/Shree2604/quotivation-bot/actions)
[![Last Commit](https://img.shields.io/github/last-commit/Shree2604/quotivation-bot?style=flat-square)](https://github.com/Shree2604/quotivation-bot/commits/main)
[![License](https://img.shields.io/github/license/Shree2604/quotivation-bot?style=flat-square)](LICENSE)

> Keep your GitHub commit streak alive with AI-themed motivational quotes for developers!

## Quotivation Bot

**Keywords**: daily quotes, life quotes, tech quotes, AI quotes, GitHub Actions, automation, inspiration, motivation

Welcome to Quotivation Bot, a GitHub repository designed specifically for AI developers to maintain their GitHub commit streaks in a meaningful and creative way. Instead of making placeholder commits, this bot uses GitHub Actions to automatically generate and commit a new AI-themed motivational quote each day.

## ✨ Features

- 🤖 **Daily AI Quotes**: Automatically generates and commits a new AI-themed motivational quote every day
- 🔄 **GitHub Actions**: Pre-configured workflow that runs on a schedule (12:00 AM Indian time)
- 📊 **Commit Streak Maintenance**: Helps maintain your GitHub activity graph
- 📝 **Markdown Formatting**: Beautifully formatted quotes in a dedicated markdown file
- 💬 **500+ Quotes**: Includes a collection of 500+ quotes related to life, tech, and AI

## 🚀 Getting Started

### Prerequisites

- A GitHub account

### Setup Instructions

```
git clone https://github.com/Shree2604/quotivation-bot.git
   cd quotivation-bot
```

1. **Fork this repository** or use it as a template
2. **Enable GitHub Actions** in your repository settings
3. **Configure the workflow**:
   - For basic setup, no changes are needed

## 📋 How It Works

1. The GitHub Action runs daily at 12:00 AM Indian time
2. It generates a new AI-themed motivational quote
3. The quote is added to `daily_quotivation.md` with proper formatting and date
4. Changes are automatically committed to your repository
5. Your GitHub activity graph shows a new contribution each day

## 🔧 Customization

### Changing the Schedule

Edit the cron expression in `.github/workflows/daily-quote.yml` to change when the quote is generated:

```yaml
schedule:
  - cron: '30 18 * * *'  # Runs at 12:00 AM Indian time (IST, UTC+5:30)
```

### Modifying Quote Collection

You can customize the quote collection in the `scripts/generate_quote.py` file by editing the `QUOTES` list.

## 📚 Example Quote

```
# Quote of the Day - June 15, 2023

> "Neural networks don't actually think; they just find patterns we're too busy to notice."

*Generated with ❤️ by Quotivation Bot*
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 🙏 Acknowledgements

- Inspired by the AI development community
- Built with GitHub Actions

---

<p align="center">Made with ❤️ for developers who love AI</p>