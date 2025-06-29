# NCKU Donation Scraper & Interactive CLI Analyzer

## Project Overview

While National Cheng Kung University publishes its donation records online, the official webpage is presented in a long list, making it difficult for users to browse or analyze the data effectively.

To solve this, I built:

-  **A web scraper that extracts all donation records from the NCKU donation site**
-  **A terminal-based interactive CLI that lets users easily explore and analyze donation data**

## Features

- Fetches complete donation records and saves them as CSV files
- Supports interactive analysis in the terminal:
  - View total donations to a specific purpose 
  - Look up donation totals by a specific donor
  - Explore detailed donation records for any target unit or purpose

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mellamochiao/ncku_donate.git
cd ncku_donate
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## How to use

### 1. Run the crawler
By default, all crawled data will be saved to the data/ folder.
This project already includes donation data for 2024 and 2025.
```bash
scrapy crawl donate_spider -O data/2025donations.csv
```

### 2. Launch the CLI analyzer
```bash
python3 donation_analysis.py
```
CLI analyzer demonstration
<img width="349" alt="Image" src="https://github.com/user-attachments/assets/8f211492-c0ab-46e6-9c0e-84cb3f84696a" />


