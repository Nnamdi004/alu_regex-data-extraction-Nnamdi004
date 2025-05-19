#!/usr/bin/python3

import re

# Sample simulated API response string
data = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
Visit our site: https://www.example.com or https://subdomain.example.org/page.
Call us at (123) 456-7890, 123-456-7890 or 123.456.7890.
Pay with card: 1234 5678 9012 3456 or 1234-5678-9012-3456.
Event starts at 14:30 or 2:30 PM.
HTML sample: <p>Welcome</p> <div class="example">Text</div> <img src="image.jpg" alt="description">
Use #ThisIsAHashtag or #example in your posts.
Total cost: $19.99 and $1,234.56
"""

# Regular Expressions for each category
regex_patterns = {
    "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "URLs": r"https?://[\w.-]+(?:/[^\s]*)?",
    "Phone Numbers": r"(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}",
    "Credit Cards": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    "Time (12/24-hour)": r"\b((1[0-2]|0?[1-9]):[0-5][0-9]\s?[APap][Mm]|([01]?\d|2[0-3]):[0-5][0-9])\b",
    "HTML Tags": r"<[^>]+>",
    "Hashtags": r"#[A-Za-z0-9_]+",
    "Currency Amounts": r"\$\d{1,3}(,\d{3})*(\.\d{2})?"
}

# Extraction function
def extract(pattern, text):
    return re.findall(pattern, text)

# Displaying results
def main():
    print("=== REGEX DATA EXTRACTION RESULTS ===\n")
    for label, pattern in regex_patterns.items():
        results = extract(pattern, data)
        print(f"{label}:")
        for match in results:
            if isinstance(match, tuple):
                print(" -", next(filter(None, match)))  # pick the actual match
            else:
                print(" -", match)
        print()

if __name__ == "__main__":
    main()

