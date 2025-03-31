# 🔄 Naukri Resume Auto-Updater

This script automatically updates your resumes on Naukri.com using **Python & Selenium**.

## 🚀 Features

- **Automated Login**: Logs into your Naukri account securely.
- **Resume Uploading**: Updates your resumes back-to-back with a 5-minute interval.
- **Secure Credentials**: Uses a `.env` file to store login details safely.
- **Loop Execution**: Runs continuously to keep your profile active.

## 🛠 Setup Instructions

### 1️⃣ Install Dependencies

Ensure you have **Python** installed, then run:

```sh
pip install selenium python-dotenv
```

2️⃣ Set Up Your Credentials
Create a .env file in the project folder and add:

NAUKRI_EMAIL=your-email@example.com
NAUKRI_PASSWORD=your-secure-password
⚠️ Important: Do not share this file or commit it to Git.

3️⃣ Download ChromeDriver
Find your Chrome version by going to chrome://settings/help

Download the matching ChromeDriver from here

Place the chromedriver.exe in the project folder.

4️⃣ Run the Script
python index.py

5️⃣ How It Works
Opens Naukri.com and logs in.

Goes to the resume upload section.

Uploads resume1.

Waits 5 minutes.

Uploads resume2.

Loops forever to keep your profile updated.

🤖 Technologies Used
Python 3+

Selenium

dotenv (for secure credential storage)

❓ FAQ

1. The script closes automatically after login?
   👉 Add a time.sleep(10) before the next action to debug.

2. Can I change the upload interval?
   👉 Yes! Modify time.sleep(300) in the script to adjust the delay.

3. My browser isn't opening?
   👉 Ensure ChromeDriver matches your Chrome version.

```

Made with ❤️ by Abhishek Powade
Feel free to contribute & improve this script! 🚀

```
