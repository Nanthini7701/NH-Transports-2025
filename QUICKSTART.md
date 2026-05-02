# Quick Start Guide - NH Transports Website

## ⚡ Fast Setup (5 minutes)

### 1. First Time Setup
```bash
cd nhtransport
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### 2. Start Development Server
```bash
python manage.py runserver
```

### 3. Access the Website
- **Website**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 📝 Common Commands

### Create Superuser
```bash
python manage.py createsuperuser
```

### Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Tests
```bash
python manage.py test
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Access Django Shell
```bash
python manage.py shell
```

### Check Project Status
```bash
python manage.py check
```

---

## 🎨 Quick Customizations

### Change Primary Color
File: `static/css/style.css`
```css
:root {
    --primary-color: #003d82;  /* Change this */
}
```

### Change Company Name
Files to edit:
1. `templates/base.html` (navbar and footer)
2. `templates/home.html` (hero title)
3. `myapp/apps.py` (verbose_name)

### Update Contact Information
File: `templates/base.html`
- Line in footer with phone, email, address

### Add Services
File: `myapp/views.py` - `services()` function

### Add Testimonials
1. Go to Admin: http://127.0.0.1:8000/admin/
2. Click "Testimonials"
3. Click "Add Testimonial"

---

## 📱 Pages Overview

### Home (/)
- Hero section with CTA buttons
- Features section (6 cards)
- Services preview (4 services)
- Statistics section
- Testimonials carousel
- Final CTA section

### About (/about/)
- Company overview
- Mission and vision
- Core values (4 items)
- Team members (3 members)
- Achievements (4 items)

### Services (/services/)
- Detailed service cards (6 services)
- How we work (4 steps)
- Fleet information (4 vehicle types)
- Call-to-action

### Contact (/contact/)
- Contact info cards (3 types)
- WhatsApp and call buttons
- Contact form with validation
- Operating hours table
- FAQs section
- Embedded map

---

## 🔐 Admin Panel Features

### Manage Contact Submissions
- Search by name, phone, location
- Filter by date
- View submission details
- Bulk actions

### Manage Testimonials
- Add/edit/delete testimonials
- Upload customer images
- Set star ratings
- Filter by rating

---

## 🐛 Debugging Tips

### Enable Debug Mode
In `nhtransport/settings.py`:
```python
DEBUG = True
```

### Enable JavaScript Debugging
In `static/js/script.js`:
```javascript
window.DEBUG = true;  // Enable logging
```

### Check Database
```bash
python manage.py shell
>>> from myapp.models import ContactSubmission
>>> ContactSubmission.objects.all()
```

### View Migrations
```bash
python manage.py showmigrations
```

---

## 📦 File Size Reference

- `style.css`: ~25KB
- `script.js`: ~15KB
- `index page load`: < 2MB (with images)

---

## ⚠️ Important Notes

1. **Change SECRET_KEY before production!**
   - In `settings.py`
   - Generate new key: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

2. **Set DEBUG=False in production**

3. **Back up database regularly**
   ```bash
   cp db.sqlite3 db.sqlite3.backup
   ```

4. **Never commit `.env` or `db.sqlite3` to GitHub**

---

## 🚀 Deployment Checklist

- [ ] Change SECRET_KEY
- [ ] Set DEBUG = False
- [ ] Update ALLOWED_HOSTS
- [ ] Configure email backend
- [ ] Set up HTTPS
- [ ] Collect static files
- [ ] Run tests
- [ ] Backup database
- [ ] Test form submissions
- [ ] Verify all pages load
- [ ] Test admin panel
- [ ] Check mobile responsiveness

---

## 📧 Contact Form Flow

User fills form → Validation checks → Data saved to DB → Success message → Admin notification

**Stored Data:**
- Name, Phone, Pickup Location, Drop Location, Message, Timestamp

---

## 🎯 Performance Tips

1. Enable caching
2. Minify CSS/JS in production
3. Use CDN for static files
4. Implement lazy loading for images
5. Use pagination for large data
6. Enable gzip compression
7. Optimize database queries

---

## 🔗 Useful Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

**Need Help?** Check the main README.md for detailed documentation!
