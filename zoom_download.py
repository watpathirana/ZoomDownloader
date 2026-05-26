import requests

url = "video URL"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://us02web.zoom.us/",
    "Cookie": "ADD YOUR COOKIE"
}
output_file = "zoom_recording.mp4"

with requests.get(url, headers=headers, stream=True) as r:
    print("Status Code:", r.status_code)

    if r.status_code != 200 and r.status_code != 206:
        print("Access denied or invalid URL")
        exit()

    total = 0

    with open(output_file, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
                total += len(chunk)
                print(f"Downloaded: {total / (1024 * 1024):.2f} MB", end="\r")

print(f"\nDownload completed: {output_file}")
