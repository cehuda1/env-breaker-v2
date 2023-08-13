import requests
import argparse
import threading
from urllib.parse import urlparse

def should_skip_scan(url):
    skip_keywords = ["cpanel", "webmail"]
    for keyword in skip_keywords:
        if keyword in url.lower():
            return True
    return False

def scan_wordlist(url, wordlist):
    if should_skip_scan(url):
        print(f"[*] Skipping scan for {url}")
        return

    with open(wordlist) as f:
        for line in f:
            word = line.strip()
            test_url = url + "/" + word
            try:
                response = requests.head(test_url)
                content_length = int(response.headers.get('content-length', 0))
                if (
                    response.status_code == 200
                    and "The requested URL was rejected" not in response.text
                    and "Request Rejected" not in response.text
                    and content_length > 300
                ):
                    print("[+] Found: " + test_url + " [Content Length: " + str(content_length) + " bytes]")
            except:
                pass

def scan_urls(urls, wordlist, max_threads=10):
    thread_pool = []
    for url in urls:
        # Add https:// to URL if protocol is not provided
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = "https://" + url

        print("[*] Scanning: " + url)
        t = threading.Thread(target=scan_wordlist, args=(url, wordlist))
        thread_pool.append(t)
        t.start()

        # Join threads if max_threads is reached
        if len(thread_pool) == max_threads:
            for t in thread_pool:
                t.join()
            thread_pool = []

    # Join remaining threads
    for t in thread_pool:
        t.join()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Scanner')
    parser.add_argument('-l', '--list', help='List of target URLs', required=True)
    parser.add_argument('-w', '--wordlist', help='Wordlist file', required=True)
    parser.add_argument('-t', '--threads', type=int, default=10, help='Maximum number of threads')
    args = parser.parse_args()

    with open(args.list) as f:
        urls = [line.strip() for line in f]

    print("[*] Starting file scanning...")
    scan_urls(urls, args.wordlist, max_threads=args.threads)
    print("[*] File scanning complete.")
