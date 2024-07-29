import os
import time
import requests

print("Starting script...")

# Path to WoW SavedVariables file
saved_variables_file = r'D:\World Of Warcraft Retail\World of Warcraft\_retail_\WTF\Account\431287727#1\SavedVariables\MyArenaNotifier.lua'

# Discord webhook URL
webhook_url = 'https://discord.com/api/webhooks/1266892466443911219/G4L_WwIBQsxgNhk6cwLPan490GQ3rVLPmSpbiHMuJZsWIYqIKD5JKbTZ58VagkSfA2zh'

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
                        if '["queued"] = true' in content:
                            print("Player login or arena queue pop detected. Sending notification.")
                            send_discord_notification("Player has logged in or arena queue popped!")
                            with open(saved_variables_file, 'w') as file:
                                file.write(content.replace('["queued"] = true', '["queued"] = false'))
                            print("Queued flag reset.")
                        else:
                            print("Queued flag not set in file content.")
                except Exception as e:
                    print(f"Error reading file: {e}")
        except Exception as e:
            print(f"Error in monitoring loop: {e}")


if __name__ == '__main__':
    print("Running the monitor_file function")
    monitor_file()
