import os
from linkedin_scraper import scrape_linkedin_job

# Ask user to paste job URL
url = input("🔗 Paste the LinkedIn job URL: ")

# Scrape the job description
description = scrape_linkedin_job(url)

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Save to file
with open("output/job_description.txt", "w", encoding="utf-8") as f:
    f.write(description)

print("✅ Job description saved to 'output/job_description.txt'")