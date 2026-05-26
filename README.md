# ZoomDownloader
Python-based Zoom cloud recording downloader using authenticated browser session cookies. Supports protected/private recordings, streaming MP4 downloads, real-time progress display, and VS Code compatibility. Uses Zoom MP4 request URL and browser cookies to securely download recordings.

---

# Features

- Download protected Zoom cloud recordings
- Supports authenticated Zoom sessions
- Uses browser cookies to bypass temporary access restrictions
- Streams large video files efficiently
- Shows real-time download progress
- Works with VS Code and Windows PowerShell

---

# Requirements

- Python 3.10+
- requests library
- Valid Zoom recording access
- Browser session cookies from Chrome/Edge

---

# Project Structure

```text
ZoomDownloader/
│
├── zoom_download.py
├── README.md
```

---

# Installation

Install Python package:

```bash
pip install requests
```

---

# Python Script

Create a file named:

```text
zoom_download.py
```

Paste this code:

```python
import requests

url = "PASTE_MP4_URL_HERE"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://us02web.zoom.us/",
    "Cookie": "PASTE_COOKIE_HERE"
}

output_file = "zoom_recording.mp4"

with requests.get(url, headers=headers, stream=True) as r:

    print("Status Code:", r.status_code)

    if r.status_code not in [200, 206]:
        print("Access denied or invalid URL")
        exit()

    total = 0

    with open(output_file, "wb") as f:

        for chunk in r.iter_content(chunk_size=1024 * 1024):

            if chunk:
                f.write(chunk)

                total += len(chunk)

                print(
                    f"Downloaded: {total / (1024 * 1024):.2f} MB",
                    end="\r"
                )

print(f"\nDownload completed: {output_file}")
```

---

# How to Get Zoom MP4 URL

## Step 1

Open the Zoom recording page in Google Chrome.

---

## Step 2

Press:

```text
F12
```

to open Developer Tools.

---

## Step 3

Open:

```text
Network
```

tab.

---

## Step 4

Play the video.

---

## Step 5

Search for:

```text
mp4
```

inside the Network filter.

---

## Step 6

Click the `.mp4` request.

---

## Step 7

Open:

```text
Headers
```

---

## Step 8

Copy:

- Request URL
- Cookie value

---

# How to Copy Cookie

Inside the `.mp4` request headers:

Find:

```text
cookie:
```

Example:

```text
cookie: _zm_mtk_guid=xxxx; _zm_page_auth=xxxx; cred=xxxx;
```

Copy everything after:

```text
cookie:
```

---

# Update Python Script

Replace:

```python
url = "PASTE_MP4_URL_HERE"
```

with your real MP4 URL.

Replace:

```python
"Cookie": "PASTE_COOKIE_HERE"
```

with your real cookie value.

---

# VS Code Setup

## Install VS Code

Download:

https://code.visualstudio.com/

---

## Install Python Extension

1. Open VS Code
2. Open Extensions
3. Search:

```text
Python
```

4. Install Microsoft Python extension

---

# Open Project

1. Create folder:

```text
ZoomDownloader
```

2. Open folder in VS Code

3. Create file:

```text
zoom_download.py
```

4. Paste the Python code

---

# Open Terminal

In VS Code:

```text
Terminal → New Terminal
```

---

# Install requests

Run:

```bash
pip install requests
```

---

# Run Script

Run:

```bash
python zoom_download.py
```

If Python command does not work:

```bash
py zoom_download.py
```

---

# Example Output

```text
Status Code: 206
Downloaded: 25.32 MB
Downloaded: 51.88 MB
Downloaded: 105.91 MB

Download completed: zoom_recording.mp4
```

---

# Downloaded File

The downloaded video will appear as:

```text
zoom_recording.mp4
```

inside the same project folder.

---

# Common Errors

## 403 Access Denied

Reason:
- Missing cookies
- Expired Zoom URL
- Host restricted recording access

Fix:
- Copy fresh cookies
- Refresh recording page
- Copy latest MP4 request

---

## requests Module Not Found

Install:

```bash
pip install requests
```

---

## Python Not Recognized

Use:

```bash
py zoom_download.py
```

or reinstall Python with:

```text
Add Python to PATH
```

enabled.

---

# Notes

- Zoom recording URLs expire after some time
- Cookies only work while logged into Zoom
- HTTP status `206` is normal
- Large videos may take time depending on internet speed

---

# License

Educational and personal use only.

---
