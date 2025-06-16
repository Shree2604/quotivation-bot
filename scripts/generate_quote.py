#!/usr/bin/env python3

import random
import datetime
from pathlib import Path
import pytz
import re

from scripts.quotes_data import QUOTES

import random
import datetime
from pathlib import Path
import pytz
import re

def generate_random_quote():
    """Generates a random quote."""
    return random.choice(QUOTES)

def update_daily_quotivation_md(quote, date):
    """Appends the new quote to daily_quotivation.md."""
    date_str = date.strftime('%B %d, %Y')
    quote_entry = f"""# Quote of the Day - {date_str}

> "{quote}"

*Generated with ❤️ by Quotivation Bot*

"""
    with open('daily_quotivation.md', 'a', encoding='utf-8') as f:
        f.write(quote_entry)

def update_readme_md(quote, date):
    """Updates the README.md with the latest quote at the top."""
    readme_path = Path('README.md')
    readme_content = readme_path.read_text(encoding='utf-8')

    # Define the new quote section to be inserted
    date_str = date.strftime('%B %d, %Y')
    new_quote_section = f"""# Shree Quotivation Bot

> "{quote}"

*— Quote of the Day - {date_str}*

"""

    # Regex to find the existing quote section (assuming it starts with # Shree Quotivation Bot and ends before the first badge or similar)
    # This regex looks for the pattern: # Shree Quotivation Bot, then any content, then a line starting with > " and ending with *— Quote of the Day*
    # It's designed to capture and replace the entire block.
    pattern = re.compile(r'(# Shree Quotivation Bot\n\n> ".*?"\n\n\*— Quote of the Day(?: - .*?)*\*\n\n)', re.DOTALL)

    if pattern.search(readme_content):
        # Replace the existing quote section
        updated_content = pattern.sub(new_quote_section, readme_content)
    else:
        # If no existing pattern found, insert after the first line (or at the very beginning if needed)
        # This part might need adjustment based on the exact README structure if the pattern doesn't match
        lines = readme_content.splitlines(True)
        if lines:
            updated_content = lines[0] + new_quote_section + "\n" + "".join(lines[1:])
        else:
            updated_content = new_quote_section

    readme_path.write_text(updated_content, encoding='utf-8')

if __name__ == "__main__":
    quote = generate_random_quote()
    today = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    update_daily_quotivation_md(quote, today)
    update_readme_md(quote, today)


def update_quote_file(quote):
    """Update the daily_quotivation.md file with the new quote using Indian time"""
    # Get current time in Indian timezone (IST)
    india_tz = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(india_tz).strftime("%B %d, %Y")
    
    content = f"""# Quote of the Day - {today}

> \"{quote}\"

*Generated with ❤️ by Quotivation Bot Done By Shree*

---

"""
    
    # Create the file if it doesn't exist
    quote_file = Path("daily_quotivation.md")
    
    if quote_file.exists():
        # Read existing content and prepend new quote
        existing_content = quote_file.read_text()
        # Keep only the last 30 quotes to avoid the file growing too large
        quotes_list = existing_content.split('---\n\n')
        if len(quotes_list) > 30:
            quotes_list = quotes_list[:30]
        updated_content = content + '\n'.join(quotes_list[:-1]) if len(quotes_list) > 1 else content
        quote_file.write_text(updated_content)
    else:
        # Create new file with just today's quote
        quote_file.write_text(content)
    
    print(f"Updated daily_quotivation.md with quote for {today}")

def update_readme(quote, today):
    """Update the README.md file with the new quote"""
    readme_file = Path("README.md")
    if not readme_file.exists():
        print("README.md not found, skipping update.")
        return

    readme_content = readme_file.read_text()

    # Define the new quote section content
    new_quote_section = f"""## 📚 Example Quote\n\n```\n# Quote of the Day - {today}\n\n> \"{quote}\"\n\n*Generated with ❤️ by Quotivation Bot*\n```"""

    # Find the start and end of the existing example quote section
    # This assumes the structure is consistent as per the generated README.md
    start_marker = "## 📚 Example Quote"
    end_marker = "## 📄 License"

    start_index = readme_content.find(start_marker)
    end_index = readme_content.find(end_marker)

    if start_index != -1 and end_index != -1 and start_index < end_index:
        # Replace the old section with the new one
        before_section = readme_content[:start_index]
        after_section = readme_content[end_index:]
        updated_readme_content = before_section + new_quote_section + "\n\n" + after_section
        readme_file.write_text(updated_readme_content)
        print("Updated README.md with the latest quote.")
    else:
        print("Could not find the example quote section in README.md, skipping update.")

def main():
    # Ensure scripts directory exists
    Path("scripts").mkdir(exist_ok=True)
    
    # Generate and update quote
    quote = generate_quote()
    update_quote_file(quote)
    
    # Get current time in Indian timezone (IST) for README update
    india_tz = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(india_tz).strftime("%B %d, %Y")
    update_readme(quote, today)

if __name__ == "__main__":
    main()