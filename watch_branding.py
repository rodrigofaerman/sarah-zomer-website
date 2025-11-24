import time
import os
import subprocess
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BRANDING_FILE = os.path.join(BASE_DIR, 'DNA', 'branding.json')
UPDATE_SCRIPT = os.path.join(BASE_DIR, 'update_website.py')

def get_file_mtime(filepath):
    try:
        return os.path.getmtime(filepath)
    except OSError:
        return 0

def main():
    print(f"Watching for changes in: {BRANDING_FILE}")
    print("Press Ctrl+C to stop.")

    last_mtime = get_file_mtime(BRANDING_FILE)

    try:
        while True:
            time.sleep(1)  # Check every second
            current_mtime = get_file_mtime(BRANDING_FILE)

            if current_mtime != last_mtime:
                print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Change detected!")
                
                # Wait a brief moment to ensure write is complete
                time.sleep(0.1)
                
                # Run the update script
                try:
                    result = subprocess.run(['python3', UPDATE_SCRIPT], capture_output=True, text=True)
                    print(result.stdout)
                    if result.stderr:
                        print(f"Errors:\n{result.stderr}")
                except Exception as e:
                    print(f"Failed to run update script: {e}")

                last_mtime = current_mtime

    except KeyboardInterrupt:
        print("\nStopping watcher...")

if __name__ == "__main__":
    main()
