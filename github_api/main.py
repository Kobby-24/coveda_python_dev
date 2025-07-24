import urllib.request as requests
import urllib.error
import json

def main():
    print("Welcome to Github User Activity Tracker")
    username = input("Enter your username: ")

    try:
        response = requests.urlopen(url=f"https://api.github.com/users/{username}/events")
        data = json.load(response)
        
        print(f"\nRecent activity for {username}:")
        print("-" * 40)
        
        activity_count = 0
        for event in data:
            if activity_count >= 5:  # Show up to 5 activities
                break
                
            event_type = event.get('type', 'Unknown')
            repo_name = event.get('repo', {}).get('name', 'Unknown')
            
            if event_type == 'PushEvent' and 'payload' in event and 'commits' in event['payload']:
                commits = event['payload']['commits']
                if commits:
                    commit_message = commits[0].get('message', 'No message')
                    print(f"📤 Pushed to {repo_name}: {commit_message}")
                    activity_count += 1
            elif event_type == 'CreateEvent':
                ref_type = event.get('payload', {}).get('ref_type', 'repository')
                print(f"🆕 Created {ref_type} in {repo_name}")
                activity_count += 1
            elif event_type == 'WatchEvent':
                print(f"⭐ Starred {repo_name}")
                activity_count += 1
            elif event_type == 'ForkEvent':
                print(f"🍴 Forked {repo_name}")
                activity_count += 1
            elif event_type == 'IssuesEvent':
                action = event.get('payload', {}).get('action', 'unknown')
                print(f"🐛 {action.capitalize()} issue in {repo_name}")
                activity_count += 1
        
        if activity_count == 0:
            print("No recent public activity found.")
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"User '{username}' not found.")
        else:
            print(f"HTTP Error: {e.code}")
    except urllib.error.URLError:
        print("Network error. Please check your internet connection.")
    except json.JSONDecodeError:
        print("Error parsing response data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()