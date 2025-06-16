#!/usr/bin/env python3

import random
import datetime
from pathlib import Path
import pytz
import re

from scripts.quotes_data import QUOTES

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