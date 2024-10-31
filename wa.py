import sys
import subprocess
from AppOpener import open

URLS = {
    "work": ["https://chat.openai.com/", "https://www.youtube.com/", ],
    "personal": ["https://www.youtube.com/"]
}

APPS = {
    "work": ["Sublime Text"]
}

BROWSERS = {
	# the r in front of the strings are just so that the backslashes are treated literally
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "microsoft": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
}

def open_webpages(urls):
    for i, url in enumerate(urls):
        try:
            if i == 0:
                print(f"Opening {url} in Chrome...")
                #Popen is what is used to open the browser we want
                subprocess.Popen([BROWSERS["chrome"], url])
            else:
                print(f"Opening {url} in Edge...")
                subprocess.Popen([BROWSERS["microsoft"], url])
        #except exception as e is so that is saves the error to the variable e
        #we will then print this error so that our code doesn't just completely stop
        except Exception as e:
            print(f"Failed to open {url}: {e}")

def open_apps(apps):
    for app in apps:
        print(f"Opening {app}...")
        open(app)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a valid set name (e.g., 'work')")
        sys.exit(1)

    set_name = sys.argv[1]
    if set_name not in URLS or set_name not in APPS:
        print("You did not pick a correct choice")
        sys.exit(1)

    urls = URLS[set_name]
    apps = APPS[set_name]

    try:
        open_webpages(urls)
        open_apps(apps)
    except Exception as e:
        print(f"An error occurred: {e}")
