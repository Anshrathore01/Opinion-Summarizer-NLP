# Pre-Deployment Checklist

Use this checklist to verify everything is ready before deploying to Hugging Face Spaces.

## Required Files

- [x] `Dockerfile` - Docker configuration for HF Spaces
- [x] `.dockerignore` - Excludes unnecessary files from build
- [x] `requirements.txt` - Includes Flask and gunicorn
- [x] `README.md` - Contains HF Spaces metadata (title, emoji, sdk: docker)
- [x] `app.py` - Updated for production (port 7860, host 0.0.0.0)

## Artifacts Verification

Verify these files exist in your `artifacts/` directory:

- [x] `artifacts/cleaned_data/clean_reviews.parquet` - Cleaned review data
- [x] `artifacts/embeddings/review_embeddings.npy` - Review embeddings
- [x] `artifacts/summaries/cluster_summaries.json` - Cluster summaries

## Configuration

- [x] `src/config/config.yaml` - Contains correct paths (relative paths work in Docker)
- [x] Port configured to 7860 (HF Spaces requirement)
- [x] Host set to 0.0.0.0 for container networking

## Application Features

- [x] Error handling added to `/results` route
- [x] Health check endpoint at `/health` for monitoring
- [x] Templates handle error display

## Testing (Optional but Recommended)

Before deploying, you can test locally:

```bash
# Start Docker Desktop first, then:
docker build -t opinion-summarizer .
docker run -p 7860:7860 opinion-summarizer

# Visit http://localhost:7860 to test
```

## Deployment Steps

1. Create Space on Hugging Face (https://huggingface.co/spaces)
   - Select Docker SDK
   - Choose appropriate hardware (CPU Basic works, GPU recommended for faster model loading)

2. Push code to Space:
   ```bash
   git init  # if not already a git repo
   git add .
   git commit -m "Initial deployment"
   git remote add space https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME
   git push space main
   ```

3. Monitor build in Space's "Logs" tab

4. Access your app once build completes

## Notes

- First build may take 10-15 minutes (model downloads)
- Models will auto-download from Hugging Face Hub on first run
- Ensure your Space has sufficient memory for embeddings and models
- The app uses ~110MB of artifacts (embeddings + cleaned data)

