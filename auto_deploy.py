#!/usr/bin/env python3
"""Automated deployment script for Hugging Face Spaces."""

import os
import subprocess
import sys
from pathlib import Path

try:
    from huggingface_hub import HfApi, create_repo
except ImportError:
    print("Installing huggingface_hub...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "huggingface_hub", "-q"])
    from huggingface_hub import HfApi, create_repo

username = "Anshrathore01"
space_name = "opinion-summarizer"
repo_id = f"{username}/{space_name}"

def main():
    print("🚀 Opinion Summarizer - Automated Deployment")
    print("=" * 50)
    print()
    
    # Check for token
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    
    if not token:
        print("📝 Hugging Face Token Required")
        print()
        print("Please provide your Hugging Face token.")
        print("Get it from: https://huggingface.co/settings/tokens")
        print()
        token = input("Enter your HF token (or press Enter to use git push): ").strip()
        
        if not token:
            print()
            print("⚠️  No token provided. Will attempt git push instead.")
            print("   Make sure you're authenticated with git credential helper.")
            print()
            token = None
    
    # Step 1: Create Space
    if token:
        try:
            print(f"📦 Creating Space: {repo_id}")
            api = HfApi(token=token)
            
            try:
                create_repo(
                    repo_id=repo_id,
                    repo_type="space",
                    space_sdk="docker",
                    private=False,
                    token=token,
                    exist_ok=True
                )
                print("✅ Space created/verified successfully!")
            except Exception as e:
                if "already exists" in str(e).lower() or "409" in str(e):
                    print("✅ Space already exists, continuing...")
                else:
                    raise
            print()
        except Exception as e:
            print(f"⚠️  Could not create Space via API: {e}")
            print("   Will try git push instead...")
            print()
            token = None
    
    # Step 2: Set up git remote
    print("🔗 Setting up git remote...")
    try:
        subprocess.run(
            ["git", "remote", "remove", "space"],
            capture_output=True,
            check=False
        )
        
        if token:
            remote_url = f"https://{username}:{token}@huggingface.co/spaces/{repo_id}"
        else:
            remote_url = f"https://huggingface.co/spaces/{repo_id}"
        
        subprocess.run(
            ["git", "remote", "add", "space", remote_url],
            check=True
        )
        print("✅ Git remote configured")
        print()
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Could not set up git remote: {e}")
        print()
    
    # Step 3: Push to Space
    print("📤 Pushing code to Hugging Face Space...")
    print()
    
    try:
        if token:
            # Use token in URL for authentication
            env = os.environ.copy()
            result = subprocess.run(
                ["git", "push", "space", "main"],
                env=env,
                check=True
            )
        else:
            # Try regular push (will prompt for credentials)
            result = subprocess.run(
                ["git", "push", "space", "main"],
                check=True
            )
        
        print()
        print("=" * 50)
        print("✅ DEPLOYMENT SUCCESSFUL!")
        print("=" * 50)
        print()
        print(f"🌐 Your app is deploying at:")
        print(f"   https://huggingface.co/spaces/{repo_id}")
        print()
        print("⏳ Build will take 10-15 minutes.")
        print("   Check progress in the 'Logs' tab of your Space.")
        print()
        print("📊 Monitor build: https://huggingface.co/spaces/{}/settings".format(repo_id))
        
    except subprocess.CalledProcessError as e:
        print()
        print("=" * 50)
        print("❌ Push failed")
        print("=" * 50)
        print()
        print("Possible solutions:")
        print()
        print("1. Create Space manually first:")
        print(f"   https://huggingface.co/spaces?create=true")
        print("   - Name: opinion-summarizer")
        print("   - SDK: Docker")
        print()
        print("2. Authenticate with git:")
        print("   git credential approve")
        print("   # Then enter your HF username and token")
        print()
        print("3. Or set token as environment variable:")
        print("   export HF_TOKEN=your_token_here")
        print("   python auto_deploy.py")
        print()
        sys.exit(1)

if __name__ == "__main__":
    main()

