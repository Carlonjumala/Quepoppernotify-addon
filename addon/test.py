import os
import time
import requests

print("Starting script...")

# Path to WoW SavedVariables file
saved_variables_file = r'D:\World Of Warcraft Retail\World of Warcraft\_retail_\WTF\Account\431287727#1\SavedVariables\MyArenaNotifier.lua'

# Discord webhook URL
webhook_url = ''

print(f"Checking file: {saved_variables_file}")

def send_discord_notification(message):
    print(f"Preparing to send notification: {message}")
    data = {
        "content": message
    }
    try:
        response = requests.post(webhook_url, json=data)
        print(f"Discord response status: {response.status_code}")
        if response.status_code == 204:
            print("Notification sent successfully.")
        else:
            print(f"Failed to send notification: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while sending notification: {e}")

def monitor_file():
    print(f"Monitoring file: {saved_variables_file}")
    if not os.path.exists(saved_variables_file):
        print(f"File not found: {saved_variables_file}")
        return
    
    last_modified = os.path.getmtime(saved_variables_file)
    print(f"Initial last modified time: {last_modified}")
    
    notified = False  # Track if we've already sent a notification

    while True:
        try:
            time.sleep(5)  # Check every 5 seconds
            
            current_modified = os.path.getmtime(saved_variables_file)
            print(f"Current modified time: {current_modified}, Last modified time: {last_modified}")
            
            if current_modified != last_modified:
                print("File modification detected.")
                last_modified = current_modified
                try:
                    with open(saved_variables_file, 'r') as file:
                        content = file.read().strip()  # Strip leading/trailing whitespace
                        print(f"File content:\n{content}")
                        
                        if 'queued = true' in content and not notified:
                            print("Arena queue pop detected. Sending notification.")
                            send_discord_notification("Arena queue has popped!")
                            notified = True  # Set notified to True to avoid re-sending
                        elif 'queued = false' in content:
                            notified = False  # Reset notified flag when queued is false
                            print("Queued flag reset detected.")
                except Exception as e:
                    print(f"Error reading file: {e}")
        except Exception as e:
            print(f"Error in monitoring loop: {e}")

if __name__ == '__main__':
    print("Running the monitor_file function")
    monitor_file()
