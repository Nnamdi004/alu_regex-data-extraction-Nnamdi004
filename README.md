# 🔍 Regex Data Extraction Project

This project uses Python and regular expressions (regex) to extract structured data from raw text. It simulates parsing API responses by identifying patterns such as emails, URLs, phone numbers, and more.

## ✅ Features

* Extracts 8 categories of data:

  * Email addresses
  * URLs
  * Phone numbers
  * Credit card numbers
  * Time (12-hour & 24-hour formats)
  * HTML tags
  * Hashtags
  * Currency amounts

## 📁 File Structure

```
├── main.py          # Main Python script with extraction logic
├── README.md        # Project overview and setup guide
```

## 🚀 Setup Instructions

1. **Ensure Python is installed** (recommended: Python 3.6+)

2. **Make script executable (Linux/macOS):**

```bash
chmod +x main.py
```

3. **Run the script:**

```bash
./main.py
```

## 🧪 Sample Output

```
=== REGEX DATA EXTRACTION RESULTS ===

Emails:
 - user@example.com
 - firstname.lastname@company.co.uk

URLs:
 - https://www.example.com
 - https://subdomain.example.org/page

Phone Numbers:
 - (123) 456-7890
 - 123-456-7890
 - 123.456.7890
...
```

## 👤 Author

Created as part of an ALU assignment by me.

