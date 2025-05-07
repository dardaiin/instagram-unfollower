import instaloader
from typing import List
import getpass
import time

def get_non_followers(username: str, password: str) -> List[str]:
    """
    Get a list of users who you follow but don't follow you back.
    
    Args:
        username (str): Your Instagram username
        password (str): Your Instagram password
    
    Returns:
        List[str]: List of usernames who don't follow you back
    """
    # Create an instance of Instaloader
    L = instaloader.Instaloader()
    
    try:
        # Login to Instagram
        print("Logging in to Instagram...")
        try:
            L.login(username, password)
        except instaloader.exceptions.TwoFactorAuthRequiredException:
            # Handle 2FA
            print("\nTwo-factor authentication is required.")
            print("Please have your authenticator app ready.")
            print("The code expires quickly, so be prepared to enter it immediately.")
            
            max_attempts = 3
            for attempt in range(max_attempts):
                if attempt > 0:
                    print(f"\nAttempt {attempt + 1} of {max_attempts}")
                    print("Please request a new code from your authenticator app.")
                    time.sleep(1)  # Give user time to read
                
                code = input("Enter the 2FA code: ").strip()
                try:
                    L.two_factor_login(code)
                    break
                except instaloader.exceptions.TwoFactorAuthRequiredException as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print("Invalid or expired code. Please try again.")
                    continue
        
        print("Successfully logged in!")
        
        # Get your profile
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Get followers and following
        print("Getting your followers...")
        followers = set(follower.username for follower in profile.get_followers())
        print(f"Found {len(followers)} followers")
        
        print("Getting accounts you follow...")
        following = set(followee.username for followee in profile.get_followees())
        print(f"Found {len(following)} accounts you follow")
        
        # Find who doesn't follow you back
        non_followers = following - followers
        
        return sorted(list(non_followers))
        
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")
        return []

def main():
    print("Instagram Unfollower")
    print("-" * 30)
    
    # Get credentials securely
    username = input("Enter your Instagram username: ").strip()
    password = getpass.getpass("Enter your Instagram password: ").strip()
    
    if not username or not password:
        print("Username and password cannot be empty!")
        return
    
    # Get non-followers
    non_followers = get_non_followers(username, password)
    
    # Display results
    if non_followers:
        print("\nUsers who don't follow you back:")
        print("-" * 40)
        for i, username in enumerate(non_followers, 1):
            print(f"{i}. {username}")
        print(f"\nTotal: {len(non_followers)} users")
    else:
        print("No non-followers found or an error occurred.")

if __name__ == "__main__":
    main() 