#!/usr/bin/env python3
"""Try to deploy using available authentication methods."""

import os
import subprocess
import sys

def try_deploy():
    print("🔍 Attempting deployment with available credentials...")
    print()
    
    # Try to get token from various sources
    token = None
    
    # Check environment
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    if token:
        print("✅ Found token in environment")
    else:
        # Check git credentials
        try:
            with open(os.path.expanduser("~/.git-credentials"), "r") as f:
                for line in f:
                    if "huggingface.co" in line:
                        # Extract token from URL
                        parts = line.strip().replace("https://", "").split("@")[0]
                        if ":" in parts:
                            token = parts.split(":")[1]
                            print("✅ Found token in git credentials")
                            break
        except:
            pass
    
    if not token:
        # Try to use HF CLI login
        try:
            from huggingface_hub import whoami
            user_info = whoami()
            print(f"✅ Logged in as: {user_info.get('name', 'Unknown')}")
            # Token might be in cache
            token = "cached"  # Will use default authentication
        except:
            print("❌ No authentication found")
            print()
            print("Please run one of these:")
            print("  1. huggingface-cli login")
            print("  2. export HF_TOKEN=your_token")
            print("  3. Or manually create space and push")
            return False
    
    # Try to create space and push
    try:
        from huggingface_hub import create_repo, HfApi
        
        repo_id = "Anshrathore01/opinion-summarizer"
        
        print(f"📦 Creating/verifying Space: {repo_id}")
        try:
            create_repo(
                repo_id=repo_id,
                repo_type="space",
                space_sdk="docker",
                private=False,
                exist_ok=True
            )
            print("✅ Space ready")
        except Exception as e:
            if "409" in str(e) or "already exists" in str(e).lower():
                print("✅ Space already exists")
            else:
                raise
        
        # Set up git and push
        print()
        print("🔗 Setting up git remote...")
        subprocess.run(["git", "remote", "remove", "space"], capture_output=True)
        
        if token and token != "cached":
            remote_url = f"https://Anshrathore01:{token}@huggingface.co/spaces/{repo_id}"
        else:
            remote_url = f"https://huggingface.co/spaces/{repo_id}"
        
        subprocess.run(["git", "remote", "add", "space", remote_url], check=True)
        print("✅ Git remote configured")
        
        print()
        print("📤 Pushing code...")
        result = subprocess.run(["git", "push", "space", "main"])
        
        if result.returncode == 0:
            print()
            print("=" * 50)
            print("✅ DEPLOYMENT SUCCESSFUL!")
            print("=" * 50)
            print()
            print(f"🌐 Your app: https://huggingface.co/spaces/{repo_id}")
            return True
        else:
            print("❌ Push failed - authentication required")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = try_deploy()
    sys.exit(0 if success else 1)

