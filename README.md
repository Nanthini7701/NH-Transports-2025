# NH Transports - Professional Transport Website

A modern, responsive Django-based website for a professional transport and logistics company. Built with Django 4.2, Bootstrap 5, and custom CSS/JavaScript.

## Features

✅ **Professional Design**
- Modern hero section with gradient background
- Responsive layout (mobile, tablet, desktop)
- Smooth animations and transitions
- Professional color scheme

✅ **Multiple Pages**
- **Home Page**: Hero section, features, services preview, statistics, testimonials, CTA
- **About Page**: Company info, mission/vision, core values, team, achievements
- **Services Page**: Detailed service cards, process steps, fleet information
- **Contact Page**: Contact form with database storage, contact info, FAQs, map embed

✅ **Backend Features**
- Django database with SQLite
- Contact form submissions stored in database
- Admin panel to manage submissions
- Django ORM for database operations
- Form validation

✅ **Frontend Features**
- Responsive navbar with smooth scrolling
- Scroll animations for cards and sections
- Auto-dismissing alerts
- Form validation with error messages
- Scroll-to-top button
- WhatsApp integration button
- Mobile-optimized design

✅ **Admin Panel**
- View all contact submissions
- Search and filter submissions
- Custom admin interface styling
- Testimonials management

## Project Structure

```
nhtransport/
├── nhtransport/              # Project settings folder
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project URL configuration
│   ├── asgi.py              # ASGI configuration
│   ├── wsgi.py              # WSGI configuration
│   └── __init__.py
├── myapp/                    # Django app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL routing
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py              # App configuration
│   ├── tests.py             # Unit tests
│   ├── migrations/          # Database migrations
│   └── __init__.py
├── templates/               # HTML templates
│   ├── base.html           # Base template (navbar + footer)
│   ├── home.html           # Home page
│   ├── about.html          # About page
│   ├── services.html       # Services page
│   └── contact.html        # Contact page
├── static/                  # Static files
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── script.js       # JavaScript animations
│   └── images/             # Image assets
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── db.sqlite3             # Database (auto-created)
└── README.md              # This file
```

## Model Schema

### ContactSubmission Model
```python
- name (CharField): Customer name
- phone (CharField): Contact phone number
- pickup_location (CharField): Pickup location
- drop_location (CharField): Drop location
- message (TextField): Message content
- created_at (DateTimeField): Submission timestamp
```

### Testimonial Model
```python
- name (CharField): Customer name
- company (CharField): Company name
- message (TextField): Testimonial text
- rating (IntegerField): 1-5 star rating
- image (ImageField): Customer image (optional)
- created_at (DateTimeField): Creation timestamp
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (optional)

### Step 1: Navigate to Project Directory
```bash
cd nhtransport
```

### Step 2: Create Virtual Environment

**On Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
When prompted, enter:
- Username: admin
- Email: admin@nhtransports.com
- Password: (your chosen password)

### Step 6: Run Development Server
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## Usage

### Access the Website
- **Frontend**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

### Test Contact Form
1. Navigate to Contact page
2. Fill in all required fields:
   - Full Name
   - Phone Number
   - Pickup Location
   - Drop Location
   - Message
3. Click "Send Message"
4. View submission in Admin Panel

### Manage Content via Admin
1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Manage Contact Submissions
4. Manage Testimonials

## Settings Configuration

### Important Settings in `settings.py`

**Development vs Production:**
```python
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['*']  # Restrict in production
```

**Secret Key:**
⚠️ **IMPORTANT**: Change the SECRET_KEY in production!
```python
SECRET_KEY = 'your-secret-key-change-in-production'
```

**Static Files:**
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

**Database:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Customization Guide

### Change Company Name
1. Edit `templates/base.html` - Change "NH Transports" in navbar and footer
2. Edit `templates/home.html` and other templates as needed
3. Modify `myapp/apps.py` - Update `verbose_name`

### Change Colors
In `static/css/style.css`, update the CSS variables:
```css
:root {
    --primary-color: #003d82;        /* Main blue */
    --secondary-color: #f39c12;      /* Orange accent */
    --danger-color: #e74c3c;         /* Red */
    --success-color: #27ae60;        /* Green */
}
```

### Change Contact Information
Edit `templates/base.html` footer:
- Phone number
- Email address
- Address
- WhatsApp number

### Add Testimonials
1. Go to Admin Panel (http://127.0.0.1:8000/admin/)
2. Click "+ Add Testimonial"
3. Fill in details:
   - Name
   - Company
   - Message
   - Rating (1-5 stars)
   - Optional: Upload image

### Modify Services
Edit `myapp/views.py` in the `services()` function to add/remove services.

### Add Team Members
Edit `templates/about.html` to add more team member cards in the team section.

## Production Deployment

### Before Deploying:
1. Set `DEBUG = False` in settings.py
2. Generate a strong SECRET_KEY
3. Set proper ALLOWED_HOSTS
4. Use PostgreSQL instead of SQLite (recommended)
5. Set up HTTPS
6. Configure email backend for contact form
7. Use environment variables for sensitive data

### Recommended Hosting Platforms:
- Heroku
- PythonAnywhere
- AWS
- DigitalOcean
- Railway

## URL Routes

| URL | View | Purpose |
|-----|------|---------|
| `/` | home | Home page |
| `/about/` | about | About page |
| `/services/` | services | Services page |
| `/contact/` | contact | Contact form |
| `/admin/` | admin | Admin panel |

## API Endpoints

### Contact Form (POST)
- **URL**: `/contact/`
- **Method**: POST
- **Required Fields**:
  - name
  - phone
  - pickup_location
  - drop_location
  - message

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'django'`
**Solution**: Make sure virtual environment is activated and requirements.txt is installed:
```bash
pip install -r requirements.txt
```

### Issue: Port 8000 already in use
**Solution**: Use a different port:
```bash
python manage.py runserver 8001
```

### Issue: Database errors or migrations fail
**Solution**: Reset database (will clear all data):
```bash
rm db.sqlite3
python manage.py migrate
```

### Issue: Static files not loading
**Solution**: Collect static files:
```bash
python manage.py collectstatic
```

### Issue: Form submission not working
**Solution**: 
1. Check browser console for JavaScript errors
2. Ensure form has CSRF token (already included in base.html)
3. Verify database migrations are applied

## Testing

Run unit tests:
```bash
python manage.py test
```

Run with verbose output:
```bash
python manage.py test --verbosity=2
```

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Optimization

### CSS
- Minified stylesheet included
- Bootstrap CDN for faster loading
- Optimized animations

### JavaScript
- Conditional loading
- Debounced scroll events
- Intersection Observer for animations

### Images
- Use optimized formats (WebP, JPEG)
- Lazy loading recommended
- Consider CDN for media files

## Security Features

✅ CSRF Protection (Django built-in)
✅ SQL Injection Prevention (Django ORM)
✅ XSS Protection (Django templating)
✅ Form validation
✅ Secure headers ready

## Future Enhancements

- [ ] Email notifications for contact submissions
- [ ] Customer login system
- [ ] Online booking system
- [ ] Payment gateway integration
- [ ] Multi-language support
- [ ] SEO optimization
- [ ] Analytics integration
- [ ] Chat support widget
- [ ] Invoice generation
- [ ] API for mobile app

## License

This project is open source and available for modification and distribution.

## Support

For issues or inquiries:
- Email: support@nhtransports.com
- Phone: +1-800-TRANSPORT
- WhatsApp: +1-234-567-8900

## Credits

Built with:
- Django Framework
- Bootstrap 5
- Font Awesome Icons
- Custom CSS/JavaScript

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Author**: NH Transports Development Team

