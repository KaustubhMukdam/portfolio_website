# Deployment Guide

This guide will help you deploy your portfolio website to various platforms.

## Prerequisites

1. **Backend Setup**: Ensure your Flask backend is properly configured
2. **Database**: Set up your database with sample data
3. **Environment Variables**: Configure production environment variables

## Deployment Options

### 1. GitHub Pages (Frontend Only)

For static frontend hosting:

1. Push your code to GitHub
2. Go to repository Settings > Pages
3. Select source branch (usually `main`)
4. Your site will be available at `https://username.github.io/portfolio_website`

**Note**: You'll need to update the API URL in `script.js` to point to your deployed backend.

### 2. Netlify (Frontend + Backend)

1. Connect your GitHub repository to Netlify
2. Set build command: `echo "Static site"`
3. Set publish directory: `portfolio_frontend`
4. Deploy your backend separately (Heroku, Railway, etc.)

### 3. Vercel (Frontend + Backend)

1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in your project directory
3. Follow the prompts to deploy

### 4. Heroku (Full Stack)

1. Install Heroku CLI
2. Create `Procfile` in root directory:
```
web: cd portfolio_backend && python run.py
```
3. Deploy:
```bash
heroku create your-portfolio-app
git push heroku main
```

### 5. Railway (Full Stack)

1. Connect your GitHub repository to Railway
2. Railway will automatically detect your Flask app
3. Set environment variables in Railway dashboard
4. Deploy

## Environment Variables

Create a `.env` file for production:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## Database Setup

1. **Local Development**:
```bash
cd portfolio_backend
python create_tables.py
python seed_data.py
```

2. **Production**: Use PostgreSQL or similar production database

## CORS Configuration

Ensure your backend allows requests from your frontend domain:

```python
# In app/extensions.py
cors = CORS(resources={
    r"/api/*": {
        "origins": ["https://yourdomain.com", "http://localhost:3000"]
    }
})
```

## SSL/HTTPS

For production deployment:
1. Use HTTPS for both frontend and backend
2. Update API URLs to use HTTPS
3. Configure proper CORS origins

## Performance Optimization

1. **Frontend**:
   - Minify CSS and JavaScript
   - Optimize images
   - Enable gzip compression

2. **Backend**:
   - Use production WSGI server (Gunicorn)
   - Enable caching
   - Optimize database queries

## Monitoring

Set up monitoring for:
- Application performance
- Error tracking
- Uptime monitoring
- Analytics

## Backup Strategy

1. Regular database backups
2. Code repository backups
3. Environment configuration backups

## Troubleshooting

### Common Issues

1. **CORS Errors**: Check CORS configuration in backend
2. **API Not Found**: Verify API endpoints and URLs
3. **Database Connection**: Check database credentials and connection
4. **Static Files**: Ensure proper static file serving

### Debug Mode

For development, enable debug mode:
```python
app.run(debug=True)
```

For production, always disable debug mode:
```python
app.run(debug=False)
```

## Security Considerations

1. Use environment variables for sensitive data
2. Enable HTTPS
3. Implement rate limiting
4. Validate all inputs
5. Use CSRF protection
6. Keep dependencies updated

## Support

If you encounter issues during deployment, check:
1. Application logs
2. Server logs
3. Browser console
4. Network tab in developer tools
