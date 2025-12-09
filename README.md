# Professional Portfolio Platform

Full-stack web application demonstrating proficiency in Django development, RESTful architecture, and modern web technologies. This production-ready portfolio system showcases end-to-end software engineering capabilities including database design, API development, and deployment automation.

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)


---

## Technical Highlights

**Core Competencies Demonstrated:**
- Django ORM with complex model relationships and custom managers
- RESTful API design principles and MVC architecture
- Custom middleware implementation for analytics tracking
- Database schema design with migrations and data integrity
- Multi-language support (i18n) for global reach
- Production deployment with CI/CD considerations
- Security best practices (CSRF protection, SQL injection prevention, XSS mitigation)

**Key Features:**
- Content management system with CRUD operations
- Image processing and media file handling
- Visitor analytics and tracking system
- Responsive UI with mobile-first approach
- Performance optimization with static file compression
- SEO implementation with meta tags and structured data

---

## Technology Stack

**Backend:** Django 4.2 (Python 3.8+) | Pillow | python-decouple | Gunicorn

**Frontend:** Vanilla JavaScript | CSS3 (Grid, Flexbox, Custom Properties) | ScrollReveal.js

**Database:** SQLite (development) | PostgreSQL/MySQL ready

**DevOps:** WhiteNoise | Railway | Git version control



## Quick Start

**Prerequisites:** Python 3.8+, pip, Git

### Local Development Setup

```bash
# Clone repository
git clone https://github.com/guinb0/Portifolio.git
cd Portifolio

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/MacOS

# Install dependencies
pip install -r requirements.txt

# Database setup
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

**Access:** http://127.0.0.1:8000/

---

## Architecture & Design Patterns

**Design Patterns Implemented:**
- **MVC/MVT Architecture:** Clean separation of models, views, and templates
- **Modular CSS Architecture:** Component-based styling for maintainability
- **Custom Middleware:** Request/response processing for analytics
- **Django Admin Customization:** Extended admin interface with custom actions

**Code Quality:**
- DRY (Don't Repeat Yourself) principles
- Reusable template components with partials
- Organized file structure following Django best practices
- Comprehensive model relationships (One-to-Many, Many-to-Many)

---

## Production Deployment

**Deployment Capabilities:**
- Railway/Heroku ready with Procfile configuration
- WhiteNoise for static file serving without CDN dependency
- Gunicorn WSGI server for production
- Environment variable configuration for security
- PostgreSQL/MySQL database migration support

**Production Checklist:**
```bash
# Static files optimization
python manage.py collectstatic --noinput

# Database migration
python manage.py migrate

# Production server
gunicorn config.wsgi:application
```

**Environment Configuration:**
```
SECRET_KEY=<secure-random-key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://...  # If using PostgreSQL
```

---

## Database Schema

**Models & Relationships:**

- **Project:** Portfolio items with media management, tagging system, ordering
- **Certificate:** Professional credentials with image uploads and external verification
- **Course:** Educational content with one-to-many lesson relationship
- **Blog Post:** Content management with SEO optimization and slug generation
- **Visitor:** Analytics tracking with IP-based identification and session management
- **SiteConfig:** Singleton pattern for global site settings

**Database Features:**
- Custom model managers and querysets
- Automated timestamp tracking (created_at, updated_at)
- Data validation and integrity constraints
- Efficient indexing for performance

---

## Security Implementation

**Security Measures:**
- CSRF protection on all forms
- XSS prevention with Django template escaping
- SQL injection protection via ORM
- Secure password hashing with PBKDF2
- Environment variable management for sensitive data
- HTTPS enforcement in production
- Clickjacking protection via X-Frame-Options
- Content Security Policy headers

**Production Security:**
- `SECRET_KEY` externalized to environment variables
- `DEBUG=False` enforcement
- Restricted `ALLOWED_HOSTS`
- Secure session cookies
- SQL injection testing completed

---

## Skills Demonstrated

**Backend Development:**
- Django framework proficiency
- Python object-oriented programming
- Database design and optimization
- RESTful API principles
- Server-side rendering
- File upload and media management

**Frontend Development:**
- Responsive web design
- JavaScript DOM manipulation
- CSS architecture and methodology
- Cross-browser compatibility
- Progressive enhancement

**Software Engineering:**
- Git version control
- Code organization and documentation
- Testing and debugging
- Performance optimization
- Deployment automation
- Security best practices

---

## Author

**Guilherme Nunes**

GitHub: [@guinb0](https://github.com/guinb0) | Project: [github.com/guinb0/Portifolio](https://github.com/guinb0/Portifolio)

