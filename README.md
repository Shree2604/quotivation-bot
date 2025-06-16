# 🤖 Quotivation Bot

> "Neural networks don't actually think; they just find patterns we're too busy to notice."
> 
> *— Quote of the Day*

[![GitHub Actions Status](https://img.shields.io/github/actions/workflow/status/Shree2604/quotivation-bot/daily-quote.yml?style=flat-square&logo=github&label=Daily%20Quote%20Generation)](https://github.com/Shree2604/quotivation-bot/actions)
[![Last Commit](https://img.shields.io/github/last-commit/Shree2604/quotivation-bot?style=flat-square&logo=git)](https://github.com/Shree2604/quotivation-bot/commits/main)
[![License](https://img.shields.io/github/license/Shree2604/quotivation-bot?style=flat-square&logo=opensource)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Shree2604/quotivation-bot?style=flat-square&logo=github)](https://github.com/Shree2604/quotivation-bot/stargazers)
[![Forks](https://img.shields.io/github/forks/Shree2604/quotivation-bot?style=flat-square&logo=github)](https://github.com/Shree2604/quotivation-bot/network/members)
[![Issues](https://img.shields.io/github/issues/Shree2604/quotivation-bot?style=flat-square&logo=github)](https://github.com/Shree2604/quotivation-bot/issues)
[![Contributors](https://img.shields.io/github/contributors/Shree2604/quotivation-bot?style=flat-square&logo=github)](https://github.com/Shree2604/quotivation-bot/graphs/contributors)

**Keep your GitHub commit streak alive with AI-themed motivational quotes for developers!**

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

```bash
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

```markdown
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
