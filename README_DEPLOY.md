# 🚀 Quick Deployment - READ THIS FIRST

## Easiest Way (One Command)

1. **Get your Hugging Face token:**
   - Go to: https://huggingface.co/settings/tokens
   - Click "New token"
   - Name it (e.g., "deployment")
   - Select "Write" permissions
   - Copy the token

2. **Run this command:**
   ```bash
   HF_TOKEN=your_token_here ./DEPLOY_NOW.sh
   ```
   
   Replace `your_token_here` with the token you copied.

That's it! The script will:
- ✅ Create the Space automatically
- ✅ Set up git remote
- ✅ Push your code
- ✅ Start the build process

## Alternative: Manual Steps

If you prefer manual control:

### Step 1: Create Space
1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Fill in:
   - **Space name**: `opinion-summarizer`
   - **SDK**: **Docker**
   - **Hardware**: CPU Basic (or GPU if available)
4. Click "Create Space"

### Step 2: Push Code
```bash
# Set up remote (if not already done)
git remote add space https://huggingface.co/spaces/Anshrathore01/opinion-summarizer

# Push (will prompt for username and token)
git push space main
# Username: Anshrathore01
# Password: [paste your HF token]
```

## Your Space URL

Once deployed: **https://huggingface.co/spaces/Anshrathore01/opinion-summarizer**

## Build Time

- First build: 10-15 minutes
- Subsequent updates: 5-10 minutes

Monitor progress in the Space's "Logs" tab.

## Troubleshooting

**"Authentication failed"**
- Make sure your token has "Write" permissions
- Token should start with `hf_`

**"Space not found"**
- Create it manually first (see Alternative steps above)
- Or use `DEPLOY_NOW.sh` which creates it automatically

**"Build failed"**
- Check the Logs tab in your Space
- Ensure all artifacts are present
- Verify Dockerfile is correct

## Files Ready for Deployment

✅ All deployment files are committed and ready:
- `Dockerfile` - Production Docker config
- `.dockerignore` - Build optimization
- `requirements.txt` - All dependencies
- `app.py` - Updated for port 7860
- `README.md` - Space metadata
- All artifacts included

