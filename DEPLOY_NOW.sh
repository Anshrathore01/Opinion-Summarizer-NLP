#!/bin/bash
# One-command deployment script
# Usage: HF_TOKEN=your_token ./DEPLOY_NOW.sh

set -e

echo "🚀 Deploying Opinion Summarizer to Hugging Face Spaces"
echo ""

# Check for token
if [ -z "$HF_TOKEN" ]; then
    echo "❌ Error: HF_TOKEN environment variable not set"
    echo ""
    echo "Usage:"
    echo "  HF_TOKEN=your_token_here ./DEPLOY_NOW.sh"
    echo ""
    echo "Get your token from: https://huggingface.co/settings/tokens"
    exit 1
fi

USERNAME="Anshrathore01"
SPACE_NAME="opinion-summarizer"
REPO_ID="${USERNAME}/${SPACE_NAME}"

echo "📦 Step 1: Installing huggingface_hub if needed..."
python3 -m pip install huggingface_hub -q --user 2>/dev/null || python3 -m pip install huggingface_hub -q

echo "📦 Step 2: Creating Space (if it doesn't exist)..."
python3 << EOF
import os
import sys
try:
    from huggingface_hub import create_repo
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "huggingface_hub", "-q", "--user"])
    from huggingface_hub import create_repo

try:
    create_repo(
        repo_id="${REPO_ID}",
        repo_type="space",
        space_sdk="docker",
        private=False,
        token=os.environ["HF_TOKEN"],
        exist_ok=True
    )
    print("✅ Space ready")
except Exception as e:
    if "409" in str(e) or "already exists" in str(e).lower():
        print("✅ Space already exists")
    else:
        raise
EOF

echo ""
echo "🔗 Step 3: Setting up git remote..."
git remote remove space 2>/dev/null || true
git remote add space "https://${USERNAME}:${HF_TOKEN}@huggingface.co/spaces/${REPO_ID}"

echo "✅ Git remote configured"
echo ""
echo "📤 Step 4: Pushing code..."
git push space main

echo ""
echo "=================================================="
echo "✅ DEPLOYMENT SUCCESSFUL!"
echo "=================================================="
echo ""
echo "🌐 Your app is deploying at:"
echo "   https://huggingface.co/spaces/${REPO_ID}"
echo ""
echo "⏳ Build will take 10-15 minutes"
echo "   Monitor progress: https://huggingface.co/spaces/${REPO_ID}/settings"

