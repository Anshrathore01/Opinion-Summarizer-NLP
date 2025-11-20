#!/bin/bash
# Setup git authentication for Hugging Face Spaces

echo "🔐 Setting up Git authentication for Hugging Face"
echo ""

# Check if git credential helper is configured
if ! git config --global credential.helper | grep -q "store"; then
    echo "📝 Configuring git credential helper..."
    git config --global credential.helper store
    echo "✅ Credential helper configured"
    echo ""
fi

echo "To authenticate, you'll need to:"
echo ""
echo "1. Get your Hugging Face token from:"
echo "   https://huggingface.co/settings/tokens"
echo ""
echo "2. When you push, git will ask for credentials:"
echo "   Username: Anshrathore01"
echo "   Password: [paste your HF token here]"
echo ""
echo "3. Or set it up now by running:"
echo "   echo 'https://Anshrathore01:YOUR_TOKEN@huggingface.co' > ~/.git-credentials"
echo ""
echo "Then run: ./deploy.sh"

