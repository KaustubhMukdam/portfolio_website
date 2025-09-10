// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Global state
let isLoading = true;

// DOM Elements
const loadingSpinner = document.getElementById('loading-spinner');
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    loadPortfolioData();
    initializeContactForm();
    initializeScrollEffects();
});

// Navigation functionality
function initializeNavigation() {
    // Mobile menu toggle
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Active navigation highlighting
    window.addEventListener('scroll', updateActiveNavLink);
}

function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}

// Load portfolio data from API
async function loadPortfolioData() {
    try {
        await Promise.all([
            loadAboutData(),
            loadSkillsData(),
            loadProjectsData(),
            loadExperienceData()
        ]);
        
        hideLoadingSpinner();
    } catch (error) {
        console.error('Error loading portfolio data:', error);
        showErrorMessage('Failed to load portfolio data. Please try again later.');
        hideLoadingSpinner();
    }
}

async function loadAboutData() {
    try {
        const response = await fetch(`${API_BASE_URL}/about`);
        const data = await response.json();
        
        // Update hero section
        document.getElementById('hero-subtitle').textContent = data.title || 'Full Stack Developer';
        document.getElementById('hero-description').textContent = data.bio || 'Passionate developer creating amazing digital experiences';
        document.getElementById('profile-name').textContent = data.name || 'Kaustubh Mukdam';
        document.getElementById('profile-location').textContent = data.location || 'Your Location';
        
        // Profile image
        const profileImageEl = document.getElementById('profile-image');
        if (data.image_url) {
            profileImageEl.innerHTML = '';
            // Ensure container behaves as circular avatar regardless of prior styles
            profileImageEl.style.width = '140px';
            profileImageEl.style.height = '140px';
            profileImageEl.style.borderRadius = '50%';
            profileImageEl.style.overflow = 'hidden';
            profileImageEl.style.background = 'transparent';
            const img = document.createElement('img');
            const isAbsolute = /^https?:\/\//i.test(data.image_url);
            const isBackendStatic = data.image_url.startsWith('/static');
            const backendBase = API_BASE_URL.replace(/\/api$/, '');
            img.src = isAbsolute ? data.image_url : (isBackendStatic ? `${backendBase}${data.image_url}` : data.image_url);
            img.alt = data.name || 'Profile photo';
            img.style.width = '100%';
            img.style.height = '100%';
            img.style.objectFit = 'cover';
            img.style.display = 'block';
            img.style.borderRadius = '50%';
            profileImageEl.appendChild(img);
        }
        
        // Resume download button
        const resumeBtn = document.getElementById('download-resume');
        if (resumeBtn) {
            resumeBtn.href = `${API_BASE_URL}/resume`;
        }
        
        // Update about section
        document.getElementById('about-bio').textContent = data.bio || 'Passionate developer creating amazing digital experiences';
        
        // Update contact section
        document.getElementById('contact-email').textContent = data.email || 'your.email@example.com';
        document.getElementById('contact-location').textContent = data.location || 'Your Location';
        
        // Update social links
        if (data.social_links) {
            updateSocialLinks(data.social_links);
        }
        
    } catch (error) {
        console.error('Error loading about data:', error);
        // Set fallback data
        document.getElementById('hero-subtitle').textContent = 'Full Stack Developer';
        document.getElementById('hero-description').textContent = 'Passionate developer creating amazing digital experiences';
        document.getElementById('profile-name').textContent = 'Kaustubh Mukdam';
        document.getElementById('profile-location').textContent = 'Your Location';
    }
}

async function loadSkillsData() {
    try {
        const response = await fetch(`${API_BASE_URL}/skills`);
        const skills = await response.json();
        
        const skillsGrid = document.getElementById('skills-grid');
        skillsGrid.innerHTML = '';
        
        skills.forEach(skill => {
            const skillCard = createSkillCard(skill);
            skillsGrid.appendChild(skillCard);
        });
        
        // Update skills count
        document.getElementById('skills-count').textContent = skills.length;
        
    } catch (error) {
        console.error('Error loading skills data:', error);
        // Show fallback skills
        showFallbackSkills();
    }
}

function createSkillCard(skill) {
    const skillCard = document.createElement('div');
    skillCard.className = 'skill-card';
    
    const proficiencyLevel = skill.proficiency_level || 3;
    const levelDots = Array.from({length: 5}, (_, i) => 
        `<span class="level-dot ${i < proficiencyLevel ? 'active' : ''}"></span>`
    ).join('');
    
    skillCard.innerHTML = `
        <div class="skill-icon">
            <i class="${skill.icon_class || 'fas fa-code'}"></i>
        </div>
        <h3 class="skill-name">${skill.name}</h3>
        <p class="skill-category">${skill.category}</p>
        <div class="skill-level">
            ${levelDots}
        </div>
    `;
    
    return skillCard;
}

async function loadProjectsData() {
    try {
        const response = await fetch(`${API_BASE_URL}/projects?featured=true`);
        const projects = await response.json();
        
        const projectsGrid = document.getElementById('projects-grid');
        projectsGrid.innerHTML = '';
        
        projects.slice(0, 6).forEach(project => {
            const projectCard = createProjectCard(project);
            projectsGrid.appendChild(projectCard);
        });
        
        // Update projects count
        document.getElementById('projects-count').textContent = projects.length;
        
    } catch (error) {
        console.error('Error loading projects data:', error);
        // Show fallback projects
        showFallbackProjects();
    }
}

function createProjectCard(project) {
    const projectCard = document.createElement('div');
    projectCard.className = 'project-card';
    
    const technologies = Array.isArray(project.technologies) 
        ? project.technologies 
        : (project.technologies ? JSON.parse(project.technologies) : []);
    
    const techTags = technologies.map(tech => 
        `<span class="tech-tag">${tech}</span>`
    ).join('');
    
    projectCard.innerHTML = `
        <div class="project-image">
            <i class="fas fa-laptop-code"></i>
        </div>
        <div class="project-content">
            <h3 class="project-title">${project.title}</h3>
            <p class="project-description">${project.description}</p>
            <div class="project-tech">
                ${techTags}
            </div>
            <div class="project-links">
                ${project.github_url ? `<a href="${project.github_url}" class="project-link" target="_blank"><i class="fab fa-github"></i> GitHub</a>` : ''}
                ${project.live_demo_url ? `<a href="${project.live_demo_url}" class="project-link" target="_blank"><i class="fas fa-external-link-alt"></i> Live Demo</a>` : ''}
            </div>
        </div>
    `;
    
    return projectCard;
}

async function loadExperienceData() {
    try {
        const response = await fetch(`${API_BASE_URL}/experience`);
        const experiences = await response.json();
        
        const timeline = document.getElementById('timeline');
        timeline.innerHTML = '';
        
        experiences.forEach(experience => {
            const timelineItem = createTimelineItem(experience);
            timeline.appendChild(timelineItem);
        });
        
        // Calculate years of experience
        if (experiences.length > 0) {
            const firstJob = experiences[experiences.length - 1];
            const startDate = new Date(firstJob.start_date);
            const currentDate = new Date();
            const yearsExperience = Math.floor((currentDate - startDate) / (365.25 * 24 * 60 * 60 * 1000));
            document.getElementById('experience-years').textContent = yearsExperience || 1;
        }
        
    } catch (error) {
        console.error('Error loading experience data:', error);
        // Show fallback experience
        showFallbackExperience();
    }
}

function createTimelineItem(experience) {
    const timelineItem = document.createElement('div');
    timelineItem.className = 'timeline-item';
    
    const startDate = new Date(experience.start_date).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short'
    });
    
    const endDate = experience.end_date 
        ? new Date(experience.end_date).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short'
        })
        : 'Present';
    
    timelineItem.innerHTML = `
        <div class="timeline-dot"></div>
        <div class="timeline-content">
            <h3 class="experience-title">${experience.position}</h3>
            <p class="experience-company">${experience.company}</p>
            <p class="experience-date">${startDate} - ${endDate}</p>
            <p class="experience-description">${experience.description || 'No description available.'}</p>
        </div>
    `;
    
    return timelineItem;
}

async function loadBlogData() {
    try {
        const response = await fetch(`${API_BASE_URL}/blog/posts?published=true`);
        const posts = await response.json();
        
        const blogGrid = document.getElementById('blog-grid');
        blogGrid.innerHTML = '';
        
        posts.slice(0, 3).forEach(post => {
            const blogCard = createBlogCard(post);
            blogGrid.appendChild(blogCard);
        });
        
    } catch (error) {
        console.error('Error loading blog data:', error);
        // Show fallback blog posts
        showFallbackBlog();
    }
}

function createBlogCard(post) {
    const blogCard = document.createElement('div');
    blogCard.className = 'blog-card';
    
    const tags = Array.isArray(post.tags) 
        ? post.tags 
        : (post.tags ? JSON.parse(post.tags) : []);
    
    const tagElements = tags.map(tag => 
        `<span class="blog-tag">${tag}</span>`
    ).join('');
    
    const createdDate = new Date(post.created_at).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
    
    blogCard.innerHTML = `
        <div class="blog-content">
            <h3 class="blog-title">${post.title}</h3>
            <p class="blog-excerpt">${post.excerpt || 'No excerpt available.'}</p>
            <div class="blog-meta">
                <span>${createdDate}</span>
                <div class="blog-tags">
                    ${tagElements}
                </div>
            </div>
        </div>
    `;
    
    return blogCard;
}

function updateSocialLinks(socialLinks) {
    const socialLinksContainer = document.getElementById('social-links');
    socialLinksContainer.innerHTML = '';
    
    const socialPlatforms = {
        github: { icon: 'fab fa-github', label: 'GitHub' },
        linkedin: { icon: 'fab fa-linkedin', label: 'LinkedIn' },
        twitter: { icon: 'fab fa-twitter', label: 'Twitter' },
        email: { icon: 'fas fa-envelope', label: 'Email' }
    };
    
    Object.entries(socialLinks).forEach(([platform, url]) => {
        if (url && socialPlatforms[platform]) {
            const link = document.createElement('a');
            link.href = url;
            link.className = 'social-link';
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
            link.innerHTML = `<i class="${socialPlatforms[platform].icon}"></i>`;
            link.title = socialPlatforms[platform].label;
            socialLinksContainer.appendChild(link);
        }
    });
}

// Contact form functionality
function initializeContactForm() {
    const contactForm = document.getElementById('contact-form');
    
    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(contactForm);
        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            subject: formData.get('subject'),
            message: formData.get('message')
        };
        
        try {
            const response = await fetch(`${API_BASE_URL}/contact`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            if (response.ok) {
                showSuccessMessage('Message sent successfully! I\'ll get back to you soon.');
                contactForm.reset();
            } else {
                const errorData = await response.json();
                showErrorMessage('Failed to send message. Please try again.');
            }
        } catch (error) {
            console.error('Error sending message:', error);
            showErrorMessage('Failed to send message. Please try again.');
        }
    });
}

// Scroll effects
function initializeScrollEffects() {
    // Navbar background on scroll
    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(10, 10, 10, 0.98)';
        } else {
            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
        }
    });
    
    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all sections for animation
    document.querySelectorAll('section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
}

// Utility functions
function hideLoadingSpinner() {
    setTimeout(() => {
        loadingSpinner.classList.add('hidden');
        isLoading = false;
    }, 1000);
}

function showSuccessMessage(message) {
    showNotification(message, 'success');
}

function showErrorMessage(message) {
    showNotification(message, 'error');
}

function showNotification(message, type) {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#4ecdc4' : '#ff6b6b'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Fallback data functions
function showFallbackSkills() {
    const fallbackSkills = [
        { name: 'JavaScript', category: 'Programming', proficiency_level: 5, icon_class: 'fab fa-js-square' },
        { name: 'Python', category: 'Programming', proficiency_level: 4, icon_class: 'fab fa-python' },
        { name: 'React', category: 'Framework', proficiency_level: 4, icon_class: 'fab fa-react' },
        { name: 'Node.js', category: 'Backend', proficiency_level: 4, icon_class: 'fab fa-node-js' },
        { name: 'HTML/CSS', category: 'Frontend', proficiency_level: 5, icon_class: 'fab fa-html5' },
        { name: 'Git', category: 'Tool', proficiency_level: 4, icon_class: 'fab fa-git-alt' }
    ];
    
    const skillsGrid = document.getElementById('skills-grid');
    skillsGrid.innerHTML = '';
    
    fallbackSkills.forEach(skill => {
        const skillCard = createSkillCard(skill);
        skillsGrid.appendChild(skillCard);
    });
    
    document.getElementById('skills-count').textContent = fallbackSkills.length;
}

function showFallbackProjects() {
    const fallbackProjects = [
        {
            title: 'Portfolio Website',
            description: 'A modern, responsive portfolio website built with HTML, CSS, and JavaScript.',
            technologies: ['HTML', 'CSS', 'JavaScript', 'Flask'],
            github_url: 'https://github.com/KaustubhMukdam/portfolio_website',
            live_demo_url: '#'
        },
        {
            title: 'E-commerce Platform',
            description: 'Full-stack e-commerce application with user authentication and payment integration.',
            technologies: ['React', 'Node.js', 'MongoDB', 'Stripe'],
            github_url: '#',
            live_demo_url: '#'
        },
        {
            title: 'Task Management App',
            description: 'Collaborative task management application with real-time updates.',
            technologies: ['Vue.js', 'Express', 'Socket.io', 'PostgreSQL'],
            github_url: '#',
            live_demo_url: '#'
        }
    ];
    
    const projectsGrid = document.getElementById('projects-grid');
    projectsGrid.innerHTML = '';
    
    fallbackProjects.forEach(project => {
        const projectCard = createProjectCard(project);
        projectsGrid.appendChild(projectCard);
    });
    
    document.getElementById('projects-count').textContent = fallbackProjects.length;
}

function showFallbackExperience() {
    const fallbackExperience = [
        {
            position: 'Machine Learning Student',
            company: 'IBM Machine Learning Specialization',
            start_date: '2024-01-01',
            end_date: null,
            description: 'Currently pursuing IBM Machine Learning Professional Certificate on Coursera. Learning advanced machine learning concepts, data analysis, and AI applications.'
        },
        {
            position: 'Python Developer Course Graduate',
            company: '100 Days of Python Programming',
            start_date: '2023-06-01',
            end_date: '2023-09-30',
            description: 'Completed comprehensive Python programming course by Dr. Angela Yu on Udemy. Built 100+ projects including web applications, games, and automation tools.'
        },
        {
            position: 'Competitive Programmer & Developer',
            company: 'Hackathon Participant',
            start_date: '2023-01-01',
            end_date: null,
            description: 'Active participant in various hackathons and coding competitions. Developed innovative solutions and collaborated with teams to solve real-world problems.'
        }
    ];
    
    const timeline = document.getElementById('timeline');
    timeline.innerHTML = '';
    
    fallbackExperience.forEach(experience => {
        const timelineItem = createTimelineItem(experience);
        timeline.appendChild(timelineItem);
    });
    
    document.getElementById('experience-years').textContent = 1;
}

function showFallbackBlog() {
    const fallbackPosts = [
        {
            title: 'Getting Started with Web Development',
            excerpt: 'A comprehensive guide for beginners who want to start their journey in web development.',
            tags: ['Web Development', 'Beginner', 'Tutorial'],
            created_at: new Date().toISOString()
        },
        {
            title: 'Modern JavaScript Features',
            excerpt: 'Exploring the latest JavaScript features and how to use them effectively.',
            tags: ['JavaScript', 'ES6+', 'Programming'],
            created_at: new Date(Date.now() - 86400000).toISOString()
        },
        {
            title: 'Building Responsive Websites',
            excerpt: 'Best practices for creating websites that work perfectly on all devices.',
            tags: ['CSS', 'Responsive Design', 'Web Design'],
            created_at: new Date(Date.now() - 172800000).toISOString()
        }
    ];
    
    const blogGrid = document.getElementById('blog-grid');
    blogGrid.innerHTML = '';
    
    fallbackPosts.forEach(post => {
        const blogCard = createBlogCard(post);
        blogGrid.appendChild(blogCard);
    });
}
