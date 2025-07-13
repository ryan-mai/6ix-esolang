# Deploying to Vercel

This guide will help you deploy your Flask app to Vercel.

## Prerequisites

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Make sure you have a Vercel account (sign up at https://vercel.com)

## Deployment Steps

### Option 1: Using Vercel CLI (Recommended)

1. **Login to Vercel**:
   ```bash
   vercel login
   ```

2. **Deploy your app**:
   ```bash
   vercel
   ```

3. **Follow the prompts**:
   - Link to existing project or create new one
   - Confirm deployment settings
   - Wait for deployment to complete

4. **Your app will be available at the provided URL**

### Option 2: Using GitHub Integration

1. **Push your code to GitHub**

2. **Connect your GitHub repository to Vercel**:
   - Go to https://vercel.com
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect it's a Python app

3. **Deploy automatically**:
   - Vercel will build and deploy automatically
   - Future pushes to your main branch will trigger automatic deployments

## Important Notes

- Your Flask app is configured to work with Vercel's serverless environment
- The `vercel.json` file tells Vercel how to build and route requests
- Static files (templates, CSS, JS) are automatically served
- Environment variables can be set in the Vercel dashboard

## Troubleshooting

If you encounter issues:

1. **Check the build logs** in the Vercel dashboard
2. **Verify all dependencies** are in `requirements.txt`
3. **Ensure your app doesn't use file system operations** that aren't supported in serverless
4. **Check that all imports work** in the serverless environment

## Custom Domain (Optional)

1. Go to your project settings in Vercel
2. Add your custom domain
3. Configure DNS settings as instructed 