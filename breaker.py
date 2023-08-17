import os
import sys
import requests
import argparse
import threading
import subprocess

def should_skip_scan(url):
    skip_keywords = ["cpanel", "webmail"]
    for keyword in skip_keywords:
        if keyword in url.lower():
            return True
    return False

def get_subdomains(domain):
    try:
        result = subprocess.check_output(["subfinder", "-d", domain], universal_newlines=True)
        subdomains = result.strip().split('\n')
        return subdomains
    except subprocess.CalledProcessError:
        print("[!] Error menjalankan Subfinder. Pastikan sudah terinstal dan ada di PATH.")
        return []

def scan_subdomains(subdomains, endpoints, max_threads=10):
    thread_pool = []
    found_urls = []

    def scan_url(url):
        try:
            response = requests.head(url)
            content_length = int(response.headers.get('content-length', 0))
            if (
                response.status_code == 200
                and "The requested URL was rejected" not in response.text
                and "Request Rejected" not in response.text
                and content_length > 300
            ):
                found_urls.append(url)
        except:
            pass

    for subdomain in subdomains:
        for endpoint in endpoints:
            test_url = "https://" + subdomain + "/" + endpoint
            t = threading.Thread(target=scan_url, args=(test_url,))
            thread_pool.append(t)
            t.start()

            # Gabungkan thread jika mencapai jumlah maksimum
            if len(thread_pool) == max_threads:
                for t in thread_pool:
                    t.join()
                thread_pool = []

    # Gabungkan sisa thread
    for t in thread_pool:
        t.join()

    return found_urls

def update_script():
    print("[*] Mengambil pembaruan skrip dari repositori GitHub...")
    try:
        os.system("git pull origin main")
        print("[+] Skrip berhasil diperbarui.")
    except:
        print("[!] Gagal memperbarui skrip.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pemindai Berkas')
    parser.add_argument('-d', '--domain', help='Nama domain', required=True)
    parser.add_argument('--update', action='store_true', help='Mengambil pembaruan skrip dari repositori GitHub')
    parser.add_argument('-t', '--threads', type=int, default=5000, help='Jumlah maksimum thread')
    args = parser.parse_args()

    if args.update:
        update_script()
        sys.exit(0)

    subdomains = get_subdomains(args.domain)
    if not subdomains:
        print("[!] Tidak ditemukan subdomain. Keluar.")
    else:
        print(f"[*] Ditemukan {len(subdomains)} subdomain untuk {args.domain}")
        endpoints = [
            ".env"
        ]
        print("[*] Memulai pemindaian berkas...")
        found_urls = scan_subdomains(subdomains, endpoints, max_threads=args.threads)
        print("[*] Pemindaian berkas selesai.")
        
        if found_urls:
            print("[+] Endpoint yang ditemukan:")
            for url in found_urls:
                print(url)
