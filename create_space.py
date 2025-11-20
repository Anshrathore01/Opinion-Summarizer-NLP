#!/usr/bin/env python3
"""Create Hugging Face Space and set up deployment."""

from huggingface_hub import HfApi, create_repo
import subprocess
import sys

username = "Anshrathore01"
space_name = "opinion-summarizer"
repo_id = f"{username}/{space_name}"

print(f"🚀 Creating Hugging Face Space: {repo_id}")
print("")

try:
    api = HfApi()
    
    # Create the Space
    print(f"📦 Creating Space '{space_name}'...")
    create_repo(
        repo_id=repo_id,
        repo_type="space",
        space_sdk="docker",
        private=False,
        exist_ok=True
    )
    
    print(f"✅ Space created successfully!")
    print(f"🌐 Space URL: https://huggingface.co/spaces/{repo_id}")
    print("")
    
    # Set up git remote
    print("🔗 Setting up git remote...")
    try:
        subprocess.run(
            ["git", "remote", "remove", "space"],
            capture_output=True,
            check=False
        )
        subprocess.run(
            ["git", "remote", "add", "space", f"https://huggingface.co/spaces/{repo_id}"],
            check=True
        )
        print("✅ Git remote configured")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Could not set up git remote: {e}")
        print(f"   You can add it manually: git remote add space https://huggingface.co/spaces/{repo_id}")
    
    print("")
    print("📤 Next step: Push your code with:")
    print(f"   git push space main")
    print("")
    print("   Or run: ./deploy.sh")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("")
    print("You may need to login first:")
    print("   huggingface-cli login")
    print("")
    print("Or create the Space manually at:")
    print(f"   https://huggingface.co/spaces?create=true")
    print("   Then select Docker SDK and name it: opinion-summarizer")
    sys.exit(1)

