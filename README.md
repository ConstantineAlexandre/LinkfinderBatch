# Python LinkFinder Batch Automation Script

This Python script automates the execution of **LinkFinder** for a list of URLs, allowing you to find potential endpoints in JavaScript files. It uses the **colorama** library to provide colorful output, making it easier to differentiate between process steps, results, and errors.

## Features

- **Automated URL Processing:** The script processes a list of URLs from a file and runs **LinkFinder** on each of them.
- **Colorful Output:** The script uses **colorama** to display different colors for success, error messages, and processing steps.
- **Error Handling:** Gracefully handles errors and displays relevant messages.

## Requirements

Make sure you have the following installed:

1. **Python 3.x**
2. **LinkFinder**  
   You can install **LinkFinder** by cloning the repository and installing its dependencies:

   ```bash
   git clone https://github.com/GerbenJavado/LinkFinder.git
   cd LinkFinder
   pip install -r requirements.txt
   
2. **Install the required Python packages by running:**
   ```bash
   pip install colorama

## How to Use

1. **Prepare a text file (e.g., urls.txt) with a list of URLs, each on a new line:**

   ```bash
   https://example.com/file1.js
   https://example.com/file2.js

2. **Run the script:**

   ```bash
   python3 batch_linkfinder.py

3. **The script will prompt you to enter the path to the file containing the URLs:**

   ```bash
   Enter the path to the file containing URLs: urls.txt

4. **The script will process each URL, run LinkFinder on it, and display the results in the terminal with colorful output:**

   - Cyan: Indicates the URL being processed.
   - Green: Shows the results of successful URL analysis.
   - Yellow: Displays the raw output from LinkFinder.
   - Red: Displays errors or exceptions.

## Example Output

   ```
   Enter the path to the file containing URLs: urls.txt
   Processing: https://example.com/file1.js
   Results for https://example.com/file1.js:
   [output of LinkFinder]
   ```

If there is an error processing a URL, you will see something like this:

   ```
   Error processing https://example.com/file2.js: [error details]
   ```

## Notes

   - Ensure that LinkFinder is installed and properly configured in your environment.
   - The script is designed to handle basic errors such as missing URLs or file paths, but ensure the URLs are valid and accessible.
   - This script is useful for automating the discovery of potential endpoints in JavaScript files across multiple URLs.

## Version: 1.0.0