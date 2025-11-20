#!/bin/bash
# Deployment script for Hugging Face Spaces

echo "🚀 Deploying Opinion Summarizer to Hugging Face Spaces..."
echo ""

# Check if Space remote exists
if ! git remote | grep -q "space"; then
    echo "❌ Space remote not found. Creating it..."
    git remote add space https://huggingface.co/spaces/Anshrathore01/opinion-summarizer
fi

echo "📦 Pushing to Hugging Face Space..."
echo ""

# Push to Space
git push space main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Deployment successful!"
    echo "🌐 Your app will be available at:"
    echo "   https://huggingface.co/spaces/Anshrathore01/opinion-summarizer"
    echo ""
    echo "⏳ Build will take 10-15 minutes. Check the Logs tab for progress."
else
    echo ""
    echo "❌ Push failed. You may need to:"
    echo "   1. Create the Space first at https://huggingface.co/spaces"
    echo "   2. Authenticate with: git credential approve"
    echo "   3. Or use HF token: git remote set-url space https://USERNAME:TOKEN@huggingface.co/spaces/Anshrathore01/opinion-summarizer"
fi

