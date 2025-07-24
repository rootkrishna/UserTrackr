# UserTrackr - Social Media Username OSINT Tool
# Developed by KRISHNA

import requests
import sys
import time
from colorama import Fore, Style

BANNER = f"""{Fore.CYAN}
 _    _                 _             _             
| |  | |               | |           (_)            
| |  | |_   _ _ __ ___ | |__   ___ ___ _ __   __ _  
| |  | | | | | '_ ` _ \| '_ \ / __/ __| '_ \ / _` | 
| |__| | |_| | | | | | | |_) | (__\__ \ | | | (_| | 
 \____/ \__,_|_| |_| |_|_.__/ \___|___/_| |_|\__,_| 
              Username Tracker by KRISHNA
{Style.RESET_ALL}"""

print(BANNER)

if len(sys.argv) != 2:
    print(f"{Fore.YELLOW}[!] Usage: python usertrackr.py <username>{Style.RESET_ALL}")
    sys.exit(1)

username = sys.argv[1]

sites = {
    "Facebook": f"https://www.facebook.com/{username}",
    "Instagram": f"https://www.instagram.com/{username}",
    "Twitter": f"https://www.twitter.com/{username}",
    "GitHub": f"https://www.github.com/{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "YouTube": f"https://www.youtube.com/@{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Pinterest": f"https://www.pinterest.com/{username}",
    "Medium": f"https://medium.com/@{username}",
    "Vimeo": f"https://vimeo.com/{username}",
    "LinkedIn": f"https://www.linkedin.com/in/{username}",
    "Steam": f"https://steamcommunity.com/id/{username}",
    "Twitch": f"https://www.twitch.tv/{username}",
    "Spotify": f"https://open.spotify.com/user/{username}",
    "AskFM": f"https://ask.fm/{username}",
    "DeviantArt": f"https://{username}.deviantart.com",
    "Flickr": f"https://www.flickr.com/people/{username}",
    "Flipboard": f"https://flipboard.com/@{username}",
    "SoundCloud": f"https://soundcloud.com/{username}",
    "VK": f"https://vk.com/{username}"
}

print(f"{Fore.YELLOW}[*] Scanning {len(sites)} platforms for username: {username}...\n{Style.RESET_ALL}")
time.sleep(1)

for site, url in sites.items():
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            print(f"{Fore.GREEN}[+] Found on {site}: {url}{Style.RESET_ALL}")
        elif res.status_code == 404:
            print(f"{Fore.RED}[-] Not found on {site}.{Style.RESET_ALL}")
        else:
            print(f"{Fore.MAGENTA}[?] Unknown response from {site} - {res.status_code}{Style.RESET_ALL}")
    except requests.exceptions.RequestException:
        print(f"{Fore.RED}[!] Error connecting to {site}{Style.RESET_ALL}")

print(f"\n{Fore.CYAN}[✔] Scan complete. Stay Anonymous. ✨{Style.RESET_ALL}")
