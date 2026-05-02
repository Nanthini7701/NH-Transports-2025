# NH Transports - Component Documentation

## Page Components Overview

### Base Template (`templates/base.html`)
Navigation bar and footer shared across all pages.

**Navbar Features:**
- Logo with icon
- Responsive hamburger menu
- smooth scroll to sections
- Sticky positioning
- Active link highlighting

**Footer Features:**
- Company information
- Quick links
- Services list
- Contact information
- Social links
- WhatsApp button
- Copyright and policies

---

## Home Page (`templates/home.html`)

### 1. Hero Section
```
┌─────────────────────────────────┐
│  Professional Transport Heading  │
│  Tagline + Description          │
│  [Get Quote] [Learn More]      │
│  [Truck Icon Animation]        │
└─────────────────────────────────┘
```
- Large heading with gradient background
- Animated truck icon on right
- Two CTA buttons
- Auto-animated elements

### 2. Why Choose Us Section
- 6 feature cards in responsive grid
- Icons with titles and descriptions
- Hover animations
- Alternating card colors

### 3. Services Preview
- 4 service cards
- Icon + title + description
- Link to full services page

### 4. Statistics Section
- Counter animation on scroll
- 4 key metrics
- Blue background with white text

### 5. Testimonials Section
- Carousel of customer testimonials
- Star ratings
- Company names
- Auto-rotating

### 6. Final CTA Section
- "Ready to Move Your Cargo?"
- Contact button

---

## About Page (`templates/about.html`)

### 1. Page Header
- Title and subtitle
- Blue gradient background

### 2. Company Overview
- Two-column layout
- Company image placeholder
- Mission statement
- Vision statement

### 3. Core Values
- 4 value cards
- Icons and descriptions
- Centered layout

### 4. Leadership Team
- 3 team member cards
- Profile images
- Names, titles, descriptions

### 5. Achievements
- 4 achievement cards
- Icons and details
- Milestone information

---

## Services Page (`templates/services.html`)

### 1. Page Header
- Page title
- Subtitle

### 2. Main Services
- 6 detailed service cards
- Icon, title, description
- Feature list with checkmarks
- Quote button for each service

**Services Included:**
1. Local Transport
2. Interstate Transport
3. Heavy Equipment Transport
4. Cargo Management
5. Climate Controlled Transport
6. 24/7 Customer Support

### 3. How We Work
- 4-step process
- Numbered steps
- Icons and descriptions

### 4. Fleet Information
- 4 vehicle types
- Icons and counts

### 5. Final CTA

---

## Contact Page (`templates/contact.html`)

### 1. Page Header

### 2. Contact Information Cards
- Phone info
- Email info
- Address info
- WhatsApp and Call buttons

### 3. Contact Form
**Form Fields:**
- Full Name (required)
- Phone Number (required)
- Pickup Location (required)
- Drop Location (required)
- Message (required)
- Terms checkbox

**Features:**
- Real-time validation
- Error messages
- Responsive layout
- Bootstrap styling

### 4. Operating Hours
- Table format
- Monday-Sunday
- Holiday exceptions

### 5. FAQs Accordion
- 5 common questions
- Collapsible answers
- Bootstrap accordion

### 6. Contact Map
- Embedded Google Map
- Responsive sizing

---

## CSS Classes & Utilities

### Common Classes
```css
.btn-primary          /* Primary button style */
.btn-outline-primary  /* Outline button style */
.btn-hover            /* Hover animation */
.section-title        /* Section heading */
.feature-card         /* Feature card styling */
.service-item         /* Service item styling */
.page-header          /* Page header styling */
.cta-section          /* Call-to-action section */
```

### Responsive Breakpoints
```
Extra Large: > 1200px
Large:      992px - 1200px
Medium:     768px - 992px
Small:      576px - 768px
Extra Small: < 576px
```

### Color Variables
```css
--primary-color: #003d82       (Dark Blue)
--secondary-color: #f39c12     (Orange)
--danger-color: #e74c3c        (Red)
--success-color: #27ae60       (Green)
--dark-color: #1a1a1a          (Very Dark)
--light-color: #f8f9fa         (Off White)
```

---

## JavaScript Functions

### Animation Functions
- `initializeScrollAnimations()` - Scroll-triggered animations
- `initializeNavbar()` - Sticky navbar
- `initializeButtons()` - Button hover effects
- `dismissAlerts()` - Auto-dismiss alerts
- `animateCounters()` - Number counters

### Utility Functions
- `formatPhoneNumber()` - Format phone numbers
- `getWhatsAppLink()` - Generate WhatsApp link
- `debounce()` - Debounce function
- `log()` - Console logging

### Scroll Features
- Smooth scroll on anchor clicks
- Scroll-to-top button
- Intersection Observer for lazy animations

---

## Form Submission Flow

```
User Input
    ↓
Client-side Validation
    ↓
CSRF Token Validation
    ↓
Server-side Validation
    ↓
Database Storage (ContactSubmission)
    ↓
Success Message Display
    ↓
Admin Notification (Optional)
    ↓
Redirect to Contact Page
```

---

## Database Models

### ContactSubmission
```
Fields:
- id (Auto, PK)
- name (CharField, max 100)
- phone (CharField, max 20)
- pickup_location (CharField, max 255)
- drop_location (CharField, max 255)
- message (TextField)
- created_at (DateTime, auto)

Methods:
- __str__() returns "Name - Phone"
- Meta: ordering by -created_at
```

### Testimonial
```
Fields:
- id (Auto, PK)
- name (CharField, max 100)
- company (CharField, max 100, optional)
- message (TextField)
- rating (IntegerField, 1-5)
- image (ImageField, optional)
- created_at (DateTime, auto)

Methods:
- __str__() returns name
- Meta: ordering by -created_at
```

---

## URL Routing

### Project URLs (`nhtransport/urls.py`)
```
/admin/        → Django admin
/              → Include myapp.urls
```

### App URLs (`myapp/urls.py`)
```
/              → home (home page)
/about/        → about (about page)
/services/     → services (services page)
/contact/      → contact (contact page & form submission)
```

---

## Admin Customizations

### ContactSubmission Admin
- Display: name, phone, pickup, drop, created_at
- Search: name, phone, locations
- Filter: created_at
- Layout: Organized fieldsets
- Read-only: created_at

### Testimonial Admin
- Display: name, company, rating, created_at
- Search: name, company, message
- Filter: rating, created_at

---

## Static Files Structure

```
static/
├── css/
│   └── style.css      (~25KB, fully commented)
├── js/
│   └── script.js      (~15KB, fully documented)
└── images/            (For logos, icons, etc.)
    ├── logo.png
    ├── hero-bg.jpg
    └── ...
```

---

## Browser DevTools Debugging

### Console Commands
```javascript
log('message')           // Custom logging
formatPhoneNumber('num') // Format numbers
getWhatsAppLink('123')   // Get WhatsApp URL
window.DEBUG = true      // Enable debug mode
```

### Useful Inspector Methods
- Check class names for styling issues
- Inspect element for layout debugging
- Check network tab for asset loading
- Review console for JavaScript errors

---

## Performance Metrics

### Load Time
- CSS: < 100ms
- JavaScript: < 100ms
- Bootstrap CDN: < 500ms
- Total: < 2-3 seconds (with images)

### Optimization Done
- CSS minification-ready
- Lazy animations
- Debounced scroll events
- Efficient selectors

---

## Accessibility Features

✅ Semantic HTML
✅ ARIA labels on buttons
✅ Form labels properly associated
✅ Color contrast adequate
✅ Keyboard navigation support
✅ Mobile touch-friendly buttons

---

## SEO Considerations

- Page titles in block tags
- Meta descriptions ready (add in templates)
- Semantic HTML structure
- Alt text for images (add manually)
- Structured data ready (schema.org)

---

## Security Checklist

✅ CSRF protection enabled
✅ SQL injection prevention (Django ORM)
✅ XSS protection (template escaping)
✅ Form validation on client and server
✅ No sensitive data in frontend
✅ Environment variables for secrets

---

## Customization Hotspots

**Easy to Customize:**
1. Colors (CSS variables)
2. Contact information (base.html)
3. Services list (views.py)
4. Team members (about.html)
5. Testimonials (admin panel)

**Moderate Difficulty:**
1. Page layout
2. Add new pages
3. Modify models
4. Change animations

**Advanced:**
1. Database schema
2. Admin customizations
3. Complex validations
4. API integration

---

## Common Modifications

### Add New Service
1. Edit `myapp/views.py` - services() function
2. Add dictionary to services_list
3. HTML will auto-render

### Add New Testimonial
1. Admin: http://127.0.0.1:8000/admin/
2. Testimonials → Add Testimonial
3. Fill form and save
4. Auto-appears on home page

### Change Color Scheme
1. Edit `static/css/style.css`
2. Modify :root CSS variables
3. All colors update site-wide

### Add New Page
1. Create template in `templates/`
2. Add view in `myapp/views.py`
3. Add URL route in `myapp/urls.py`
4. Link in navbar (base.html)

---

**Version**: 1.0.0
**Last Updated**: 2024
**Comprehensive Documentation Complete**
