# Deployment Guide for Hugging Face Spaces

This guide will help you deploy the Opinion Summarizer to Hugging Face Spaces.

## Prerequisites

1. A Hugging Face account (sign up at https://huggingface.co)
2. Docker installed on your local machine (for testing)
3. Git installed

## Steps to Deploy

### 1. Create a New Space on Hugging Face

1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Fill in the details:
   - **Space name**: `opinion-summarizer` (or your preferred name)
   - **SDK**: Select **Docker**
   - **Hardware**: Choose based on your needs (CPU Basic is fine for testing, GPU may be needed for faster model loading)
   - **Visibility**: Public or Private
4. Click "Create Space"

### 2. Push Your Code to the Space

Hugging Face Spaces uses Git, so you'll need to push your code:

```bash
# Initialize git if not already done
git init

# Add Hugging Face Space as remote (replace YOUR_USERNAME and SPACE_NAME)
git remote add space https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME

# Add all files
git add .

# Commit
git commit -m "Initial deployment"

# Push to Hugging Face Space
git push space main
```

Alternatively, you can use the Hugging Face CLI:

```bash
# Install HF CLI if not already installed
pip install huggingface_hub

# Login
huggingface-cli login

# Upload files (from project root)
cd /Users/anshrathore/Desktop/Opinion-Summarizer-NLP
huggingface-cli upload YOUR_USERNAME/SPACE_NAME . --repo-type=space
```

### 3. Wait for Build

After pushing, Hugging Face Spaces will automatically:
1. Build the Docker image using the Dockerfile
2. Install all dependencies from requirements.txt
3. Start the application on port 7860

You can monitor the build progress in the Space's "Logs" tab.

### 4. Access Your Deployed App

Once the build completes, your app will be available at:
`https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME`

## Testing Locally with Docker

Before deploying, you can test the Docker build locally:

```bash
# Build the Docker image
docker build -t opinion-summarizer .

# Run the container
docker run -p 7860:7860 opinion-summarizer

# Access at http://localhost:7860
```

## Important Notes

1. **Artifacts**: The `artifacts/` directory is included in the Docker image. Make sure all required files (embeddings, cleaned data, summaries) are present.

2. **Model Downloads**: Models will be downloaded automatically from Hugging Face Hub on first run:
   - `sentence-transformers/all-MiniLM-L6-v2` (embedding model)
   - `google/pegasus-xsum` (summarization model)

3. **Port**: The app must run on port 7860 (Hugging Face Spaces requirement).

4. **Memory**: The app loads embeddings and models into memory. Ensure your Space has sufficient RAM/GPU memory.

5. **Build Time**: First build may take 10-15 minutes due to model downloads and dependency installation.

## Troubleshooting

- **Build fails**: Check the Logs tab in your Space for error messages
- **App doesn't start**: Verify port 7860 is exposed and app binds to 0.0.0.0
- **Models not loading**: Check internet connectivity and model names in config
- **Out of memory**: Upgrade to a Space with more RAM/GPU

## Updating Your Deployment

To update your Space after making changes:

```bash
git add .
git commit -m "Update description"
git push space main
```

The Space will automatically rebuild with your changes.

