# Portfolio Website

A modern, responsive portfolio website with a beautiful dark theme. Built with Flask backend and vanilla HTML/CSS/JavaScript frontend.

## 🌟 Features

- **Dark Theme**: Sleek dark design with beautiful gradients and animations
- **Responsive Design**: Works perfectly on all devices and screen sizes
- **Fast Performance**: Optimized for speed and smooth user experience
- **API Integration**: RESTful API backend with dynamic content loading
- **Contact Form**: Functional contact form with email notifications
- **Blog System**: Dynamic blog posts with tags and categories
- **Project Showcase**: Featured projects with live demos and GitHub links
- **Skills Display**: Interactive skills section with proficiency levels
- **Experience Timeline**: Professional experience with timeline visualization

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/KaustubhMukdam/portfolio_website.git
cd portfolio_website
```

2. **Set up the backend**:
```bash
cd portfolio_backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

3. **Initialize the database**:
```bash
python create_tables.py
python seed_sample_data.py
```

4. **Start the servers**:
```bash
# From the root directory
python start_portfolio.py
```

This will start:
- Backend server at `http://localhost:5000`
- Frontend server at `http://localhost:3000`

## 🔧 Production Config

- Frontend API base URL: set in `portfolio_frontend/script.js`.
  - Development: `const API_BASE_URL = 'http://localhost:5000/api';`
  - Production (example): `const API_BASE_URL = 'https://<your-railway-domain>/api';`
- Resume file path (backend): put your PDF at `portfolio_backend/app/static/Kaustubh_Mukdam_Resume.pdf`.
- Profile photo path (backend): put your photo at `portfolio_backend/app/static/profile.jpg`.

## 🎯 Deploy (Recommended: Railway backend + GitHub Pages frontend)

### Backend → Railway

1. Push code to GitHub (this repository).
2. In Railway: New Project → Deploy from GitHub → select this repo.
3. Set service root/working directory to `portfolio_backend`.
4. Start command (if prompted): `python run.py`.
5. Add environment variables in Railway → Variables:
   - `FLASK_ENV=production`
   - `SECRET_KEY=<strong-random-value>`
   - `MAIL_SERVER=smtp.gmail.com`
   - `MAIL_PORT=587`
   - `MAIL_USE_TLS=true`
   - `MAIL_USERNAME=<your-email>`
   - `MAIL_PASSWORD=<your-app-password>`
6. Add a Postgres database (Railway → Add → Database → Postgres) and set `DATABASE_URL` to the provided connection string.
7. First-time setup: Railway shell → run:
   - `python create_tables.py`
   - optional: `python seed_sample_data.py`
8. Verify backend:
   - `https://<your-railway-domain>/api/about`
   - `https://<your-railway-domain>/api/resume`

### Frontend → GitHub Pages

1. In `portfolio_frontend/script.js`, set:
   - `const API_BASE_URL = 'https://<your-railway-domain>/api';`
2. Commit and push.
3. GitHub → Repo Settings → Pages:
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/portfolio_frontend`
4. Open the published URL: `https://<your-username>.github.io/portfolio_website/`

### Post-Deploy Checks

- Frontend loads About/Skills/Projects without CORS errors.
- Resume button downloads your PDF.
- Profile photo renders in a circle.
- Contact form POST works (`/api/contact`).
- If needed, restrict CORS to your frontend origin in `app/extensions.py`.

## 📁 Project Structure

```
portfolio_website/
├── portfolio_backend/          # Flask backend API
│   ├── app/
│   │   ├── routes/            # API endpoints
│   │   ├── models.py          # Database models
│   │   └── extensions.py      # Flask extensions
│   ├── migrations/            # Database migrations
│   ├── requirements.txt       # Python dependencies
│   └── run.py                # Backend entry point
├── portfolio_frontend/        # Frontend website
│   ├── index.html            # Main HTML file
│   ├── styles.css            # CSS styles
│   ├── script.js             # JavaScript functionality
│   └── server.py             # Frontend server
├── start_portfolio.py        # Startup script
└── deploy.md                 # Deployment guide
```

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework
- **SQLAlchemy**: ORM for database operations
- **Flask-Migrate**: Database migrations
- **Flask-Mail**: Email functionality
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Grid and Flexbox
- **JavaScript (ES6+)**: Interactive functionality
- **Font Awesome**: Icons
- **Google Fonts**: Typography

### Database
- **SQLite**: Development database
- **PostgreSQL**: Production database (recommended)

## 🎨 Customization

### Personal Information
Update your personal information in the backend API endpoints or directly in the database.

### Styling
Modify CSS variables in `portfolio_frontend/styles.css`:
```css
:root {
    --primary-color: #00d4ff;
    --secondary-color: #ff6b6b;
    --accent-color: #4ecdc4;
    /* ... other variables */
}
```

### Content
- Add your projects through the backend API
- Update skills and experience
- Write blog posts
- Customize the hero section

## 📱 API Endpoints

- `GET /api/about` - Personal information
- `GET /api/skills` - Skills and technologies
- `GET /api/projects` - Project portfolio
- `GET /api/experience` - Professional experience
- `GET /api/blog/posts` - Blog posts
- `POST /api/contact` - Contact form submission
- `GET /api/testimonials` - Client testimonials

## 🚀 Deployment

See [deploy.md](deploy.md) for detailed deployment instructions for various platforms including:
- GitHub Pages
- Netlify
- Vercel
- Heroku
- Railway

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Kaustubh Mukdam**
- GitHub: [@KaustubhMukdam](https://github.com/KaustubhMukdam)
- LinkedIn: [kaustubh-mukdam-ab0170340](https://www.linkedin.com/in/kaustubh-mukdam-ab0170340)
- Twitter: [@KMukdam9474](https://x.com/KMukdam9474)

## 🙏 Acknowledgments

- Font Awesome for the beautiful icons
- Google Fonts for the Inter font family
- Flask community for the excellent documentation
- All contributors and supporters

---

⭐ If you found this project helpful, please give it a star!