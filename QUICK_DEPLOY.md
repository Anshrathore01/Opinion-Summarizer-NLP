# Quick Deployment Guide

## Step 1: Login to Hugging Face

Run this command and enter your Hugging Face token when prompted:

```bash
source venv/bin/activate
huggingface-cli login
```

Get your token from: https://huggingface.co/settings/tokens

## Step 2: Create Space and Deploy

Once logged in, run:

```bash
python create_space.py
```

This will:
- Create the Space on Hugging Face
- Set up the git remote
- Prepare everything for deployment

## Step 3: Push Your Code

After the Space is created, push your code:

```bash
git push space main
```

Or simply run:

```bash
./deploy.sh
```

## Alternative: Manual Space Creation

If you prefer to create the Space manually:

1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Fill in:
   - **Space name**: `opinion-summarizer`
   - **SDK**: Docker
   - **Hardware**: CPU Basic (or GPU if you have access)
4. Click "Create Space"
5. Then run: `./deploy.sh`

## Your Space URL

Once deployed, your app will be at:
**https://huggingface.co/spaces/Anshrathore01/opinion-summarizer**

Build time: 10-15 minutes (first time)

