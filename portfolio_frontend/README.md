# Portfolio Website Frontend

A beautiful, modern, and responsive portfolio website with a dark theme built using vanilla HTML, CSS, and JavaScript.

## Features

- 🌙 **Dark Theme**: Sleek dark design with beautiful gradients
- 📱 **Responsive Design**: Works perfectly on all devices
- ⚡ **Fast Loading**: Optimized for performance
- 🎨 **Modern UI/UX**: Clean and professional design
- 🔗 **API Integration**: Connects to Flask backend
- 📧 **Contact Form**: Functional contact form with validation
- 🎯 **Smooth Scrolling**: Enhanced navigation experience
- 📊 **Dynamic Content**: Loads data from backend API

## Sections

- **Hero**: Introduction with call-to-action buttons
- **About**: Personal information and statistics
- **Skills**: Technical skills with proficiency levels
- **Projects**: Featured projects with links
- **Experience**: Professional timeline
- **Blog**: Latest blog posts
- **Contact**: Contact form and social links

## Getting Started

### Prerequisites

- A running Flask backend server (portfolio_backend)
- Modern web browser

### Installation

1. Clone the repository:
```bash
git clone https://github.com/KaustubhMukdam/portfolio_website.git
cd portfolio_website/portfolio_frontend
```

2. Open `index.html` in your web browser or serve it using a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js (if you have http-server installed)
npx http-server

# Using PHP
php -S localhost:8000
```

3. Make sure your Flask backend is running on `http://localhost:5000`

### Configuration

Update the API base URL in `script.js` if your backend is running on a different port:

```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

## Customization

### Colors

The color scheme can be customized by modifying CSS variables in `styles.css`:

```css
:root {
    --primary-color: #00d4ff;
    --secondary-color: #ff6b6b;
    --accent-color: #4ecdc4;
    --background-dark: #0a0a0a;
    /* ... other variables */
}
```

### Content

- Update personal information in the backend API
- Modify the hero section text in `index.html`
- Add your own projects, skills, and experience through the backend

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance

- Optimized CSS with minimal external dependencies
- Efficient JavaScript with async/await
- Responsive images and lazy loading
- Smooth animations and transitions

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

If you have any questions or need help, please open an issue on GitHub.
