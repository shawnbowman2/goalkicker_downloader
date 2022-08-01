# goalkicker_downloader
## Purpose
Identify and download all PDFs on GoalKicker
## Method
1. Provide single user entry point via run.sh which:
  * Creates python virtualenv.
  * Installs requirements into isolated environment intstead of system python.
  * Launches python script within virtual environment to handle main tasks. 
2. Use Python3, requests, and BeautifulSoup / bf4 to find all relevant links in the main goalkicker site.
3. Use the same tools to identify the PDF file links and download the manuals provided by Goalkicker.
