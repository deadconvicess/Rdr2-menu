# coded by @deadconvicess
# This script installs required programs
# Github repo - https://github.com/deadconvicess/Rdr2-menu

import os, sys, urllib.request, subprocess, tempfile, platform
os.system("title Program installer by @deadconvicess")

if platform.system() != "Windows" or int(platform.version().split(".")[0]) < 10:
    sys.exit("Windows required")

programs = {
    "Sdk.exe": "https://builds.dotnet.microsoft.com/dotnet/Sdk/10.0.100/dotnet-sdk-10.0.100-win-x64.exe",
    "Redistributable.exe": "https://aka.ms/vs/17/release/vc_redist.x64.exe"
}

temp_dir = tempfile.gettempdir()

def install(url, dest):
    def show_progress(block, block_size, total_size):
        if total_size <= 0: total_size = 1
        percent = min(100, block * block_size / total_size * 100)
        bar_len = 50
        filled = int(bar_len * percent / 100)
        bar = "█" * filled + "-" * (bar_len - filled)
        print(f"\r[{bar}] {percent:6.2f}%", end="")
    try:
        urllib.request.urlretrieve(url, dest, reporthook=show_progress)
        print("\r[" + "█"*50 + "] 100.00%")
    except Exception as e:
        sys.exit(f"Failed to download:(")

for name, url in programs.items():
    path = os.path.join(temp_dir, name)
    print(f"Ininstalling {name}")
    install(url, path)
    try:
        proc = subprocess.Popen([path, "/quiet", "/norestart"], shell=True)
        proc.wait()
    except Exception as e:
        sys.exit(f"Failed to install:(")
