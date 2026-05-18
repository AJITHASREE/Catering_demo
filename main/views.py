from django.shortcuts import render

# Create your views here.
"""
Views for main app - M.S. Catering Services
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json


def home(request):
    """Home page view"""
    context = {
        'page_title': 'Premium South Indian Catering',
        'services': [
            {
                'title': 'Wedding Catering',
                'description': 'Elegant Tamil wedding catering with traditional taste',
                'icon': '💍',
                'color': 'from-pink-500 to-rose-500'
            },
            {
                'title': 'Corporate Events',
                'description': 'Professional catering for corporate gatherings and conferences',
                'icon': '🏢',
                'color': 'from-blue-500 to-cyan-500'
            },
            {
                'title': 'Birthday Celebrations',
                'description': 'Memorable celebrations with delicious cuisine',
                'icon': '🎉',
                'color': 'from-purple-500 to-pink-500'
            },
            {
                'title': 'Buffet Service',
                'description': 'Interactive buffet counters with live cooking',
                'icon': '🍽️',
                'color': 'from-orange-500 to-red-500'
            },
        ],
        'testimonials': [
            {
                'name': 'Priya Sharma',
                'role': 'Wedding Bride - 2023',
                'text': 'M.S. Catering made our wedding reception absolutely memorable. The food, service, and attention to detail were impeccable.',
                'rating': 5
            },
            {
                'name': 'Vikram Iyer',
                'role': 'Corporate Director',
                'text': 'Professional, reliable, and delicious. They catered our company annual dinner and everyone was impressed.',
                'rating': 5
            },
            {
                'name': 'Anjali Kumar',
                'role': 'Birthday Host - 2024',
                'text': 'Outstanding service! The traditional South Indian menu was authentic and beautifully presented.',
                'rating': 5
            },
        ],
        'stats': [
            {'number': '1000+', 'label': 'Events Catered'},
            {'number': '50K+', 'label': 'Happy Guests'},
            {'number': '22', 'label': 'Years of Excellence'},
            {'number': '100%', 'label': 'Client Satisfaction'},
        ]
    }
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    context = {
        'page_title': 'About M.S. Catering Services',
        'company_story': {
            'founded': '2002',
            'founder': 'Mr. Muralidharan Iyer',
            'mission': 'To deliver authentic South Indian culinary excellence with premium service for every celebration',
            'vision': 'To be the most trusted luxury catering brand for traditional and modern events across Chennai and Tamil Nadu',
        },
        'team_highlights': [
            {
                'name': 'Mr. Muralidharan Iyer',
                'role': 'Founder & Head Chef',
                'expertise': '22 years of culinary excellence in South Indian cuisine'
            },
            {
                'name': 'Mrs. Lakshmi Iyer',
                'role': 'Operations Manager',
                'expertise': 'Event coordination and customer relations'
            },
            {
                'name': 'Chef Ramesh Kumar',
                'role': 'Executive Chef',
                'expertise': 'Traditional Tamil wedding menus and specialty dishes'
            },
            {
                'name': 'Priya Srinivasan',
                'role': 'Pastry Chef',
                'expertise': 'Traditional South Indian sweets and desserts'
            },
        ]
    }
    return render(request, 'about.html', context)


def services(request):
    """Services page view"""
    context = {
        'page_title': 'Our Premium Catering Services',
        'services': [
            {
                'title': 'Wedding Catering',
                'tagline': 'Your Special Day, Our Culinary Masterpiece',
                'description': 'Experience luxury wedding catering with traditional Tamil cuisine, modern presentation, and impeccable service.',
                'features': [
                    'Multi-cuisine options (Traditional & Modern)',
                    'Customized wedding menus',
                    'Live cooking stations',
                    'Professional service staff',
                    'Premium tableware and decor coordination',
                    'Dietary accommodation'
                ],
                'min_guests': '50',
                'image_placeholder': 'wedding-catering'
            },
            {
                'title': 'Corporate Catering',
                'tagline': 'Professional Events, Premium Experience',
                'description': 'Impress your clients and colleagues with sophisticated corporate catering solutions.',
                'features': [
                    'Breakfast & lunch packages',
                    'Conference refreshments',
                    'Executive dining',
                    'Hygiene certified kitchen',
                    'Timely delivery',
                    'Flexible menu options'
                ],
                'min_guests': '25',
                'image_placeholder': 'corporate-catering'
            },
            {
                'title': 'Birthday Celebrations',
                'tagline': 'Make Every Moment Special',
                'description': 'Celebrate birthdays with customized menus and dedicated service.',
                'features': [
                    'Age-specific menu options',
                    'Dessert & cake arrangements',
                    'Themed decoration coordination',
                    'Kids-friendly options',
                    'Interactive service',
                    'Custom portions'
                ],
                'min_guests': '15',
                'image_placeholder': 'birthday-catering'
            },
            {
                'title': 'Buffet Catering',
                'tagline': 'Interactive Dining Experience',
                'description': 'Engage your guests with live buffet counters and interactive cooking.',
                'features': [
                    'Live dosa counter',
                    'Live paneer counter',
                    'Dessert station',
                    'Vegetarian & non-vegetarian options',
                    'Professional chefs on-site',
                    'Equipment provided'
                ],
                'min_guests': '30',
                'image_placeholder': 'buffet-catering'
            },
            {
                'title': 'Outdoor Catering',
                'tagline': 'Celebrations Anywhere, Anytime',
                'description': 'Complete catering solution for outdoor events with complete setup.',
                'features': [
                    'Outdoor kitchen setup',
                    'Generators & lighting',
                    'Complete tableware',
                    'Weather protection',
                    'Setup & cleanup',
                    'Full service staff'
                ],
                'min_guests': '50',
                'image_placeholder': 'outdoor-catering'
            },
            {
                'title': 'Festival Catering',
                'tagline': 'Celebrate Traditions in Style',
                'description': 'Special catering for traditional festivals and celebrations.',
                'features': [
                    'Traditional festival menus',
                    'Authentic recipes',
                    'Seasonal specialties',
                    'Family preferences accommodation',
                    'Flexible timings',
                    'Expert coordination'
                ],
                'min_guests': '20',
                'image_placeholder': 'festival-catering'
            },
        ]
    }
    return render(request, 'services.html', context)


def menu(request):
    """Menu page view"""
    context = {
        'page_title': 'Our Signature Menu',
        'menu_categories': [
            {
                'name': 'Traditional Meals',
                'items': [
                    {
                        'name': 'Samai Sadam with Sambar',
                        'description': 'Traditional millet rice with sambar and vegetables'
                    },
                    {
                        'name': 'Kozhambu Annam',
                        'description': 'Rice with traditional curry and pickle'
                    },
                    {
                        'name': 'Curd Rice',
                        'description': 'Authentic yogurt rice with tempering'
                    },
                ]
            },
            {
                'name': 'Wedding Specials',
                'items': [
                    {
                        'name': 'Biryani',
                        'description': 'Fragrant rice with tender meat and spices'
                    },
                    {
                        'name': 'Paneer 65',
                        'description': 'Crispy paneer preparation with tangy spices'
                    },
                    {
                        'name': 'Murgh Makhani',
                        'description': 'Butter chicken in rich gravy'
                    },
                ]
            },
            {
                'name': 'Buffet Specials',
                'items': [
                    {
                        'name': 'Live Dosa Counter',
                        'description': 'Fresh dosas prepared right in front of your guests'
                    },
                    {
                        'name': 'Live Paneer Tikka',
                        'description': 'Grilled paneer pieces with Indian spices'
                    },
                    {
                        'name': 'Raita Selection',
                        'description': 'Variety of yogurt-based side dishes'
                    },
                ]
            },
            {
                'name': 'Desserts',
                'items': [
                    {
                        'name': 'Payasam',
                        'description': 'Traditional South Indian sweet dish'
                    },
                    {
                        'name': 'Gulab Jamun',
                        'description': 'Soft milk solids in sugar syrup'
                    },
                    {
                        'name': 'Jalebi',
                        'description': 'Golden crispy sweet spirals'
                    },
                ]
            },
            {
                'name': 'Breakfast Menu',
                'items': [
                    {
                        'name': 'Masala Dosa',
                        'description': 'Crispy dosa with spiced potato filling'
                    },
                    {
                        'name': 'Idli Sambar',
                        'description': 'Steamed cakes with lentil curry'
                    },
                    {
                        'name': 'Uttapam',
                        'description': 'Thick pancake with vegetable toppings'
                    },
                ]
            },
            {
                'name': 'Non-Veg Specials',
                'items': [
                    {
                        'name': 'Chicken Curry 65',
                        'description': 'Spicy fried chicken preparation'
                    },
                    {
                        'name': 'Fish Fry',
                        'description': 'Crispy fried fish with spices'
                    },
                    {
                        'name': 'Chettinadu Chicken',
                        'description': 'Aromatic chicken with coconut and spices'
                    },
                ]
            },
        ]
    }
    return render(request, 'menu.html', context)


def gallery(request):
    """Gallery page view"""
    context = {
        'page_title': 'Event Gallery',
        'gallery_sections': [
            {
                'title': 'Weddings',
                'count': '250+',
                'images': [
                    {'id': 1, 'alt': 'Wedding decoration and setup'},
                    {'id': 2, 'alt': 'Bride and groom celebration'},
                    {'id': 3, 'alt': 'Wedding feast presentation'},
                    {'id': 4, 'alt': 'Reception party'},
                ]
            },
            {
                'title': 'Corporate Events',
                'count': '180+',
                'images': [
                    {'id': 5, 'alt': 'Corporate dining setup'},
                    {'id': 6, 'alt': 'Professional service'},
                    {'id': 7, 'alt': 'Conference catering'},
                    {'id': 8, 'alt': 'Corporate buffet'},
                ]
            },
            {
                'title': 'Birthday Parties',
                'count': '320+',
                'images': [
                    {'id': 9, 'alt': 'Birthday celebration'},
                    {'id': 10, 'alt': 'Cake and desserts'},
                    {'id': 11, 'alt': 'Party setup'},
                    {'id': 12, 'alt': 'Happy guests'},
                ]
            },
            {
                'title': 'Buffet Highlights',
                'count': '420+',
                'images': [
                    {'id': 13, 'alt': 'Live dosa counter'},
                    {'id': 14, 'alt': 'Buffet spread'},
                    {'id': 15, 'alt': 'Food plating'},
                    {'id': 16, 'alt': 'Chef in action'},
                ]
            },
        ]
    }
    return render(request, 'gallery.html', context)


def blog(request):
    """Blog page view"""
    context = {
        'page_title': 'Catering Blog',
        'featured_post': {
            'title': 'The Art of South Indian Wedding Feasts',
            'excerpt': 'Discover the traditions and techniques behind authentic South Indian wedding catering.',
            'date': 'March 15, 2024',
            'author': 'Chef Muralidharan',
        },
        'blog_posts': [
            {
                'title': 'Planning the Perfect Wedding Menu',
                'excerpt': 'Essential tips for selecting and planning your wedding catering menu.',
                'date': 'March 10, 2024',
                'author': 'Priya Srinivasan',
                'category': 'Wedding Planning'
            },
            {
                'title': 'Traditional Payasam: A Sweet Tradition',
                'excerpt': 'Explore the history and variations of South India\'s beloved dessert.',
                'date': 'March 5, 2024',
                'author': 'Chef Ramesh Kumar',
                'category': 'Recipes'
            },
            {
                'title': 'Corporate Catering Excellence',
                'excerpt': 'How to impress your clients with professional corporate catering.',
                'date': 'February 28, 2024',
                'author': 'Lakshmi Iyer',
                'category': 'Corporate'
            },
            {
                'title': 'Live Cooking Stations: Engaging Your Guests',
                'excerpt': 'The benefits and best practices of interactive buffet experiences.',
                'date': 'February 20, 2024',
                'author': 'Chef Muralidharan',
                'category': 'Buffet Service'
            },
            {
                'title': 'Dietary Accommodations: Serving Everyone',
                'excerpt': 'How we ensure every guest is catered to with dietary preferences in mind.',
                'date': 'February 15, 2024',
                'author': 'Priya Srinivasan',
                'category': 'Special Diets'
            },
            {
                'title': 'Seasonal Specialties for Your Event',
                'excerpt': 'Make the most of seasonal ingredients with our seasonal catering menu.',
                'date': 'February 10, 2024',
                'author': 'Chef Ramesh Kumar',
                'category': 'Seasonal'
            },
        ]
    }
    return render(request, 'blog.html', context)


def contact(request):
    """Contact page view"""
    context = {
        'page_title': 'Contact Us',
        'contact_info': {
            'phone': '+91 44-XXXX-XXXX',
            'whatsapp': '+91 98765-43210',
            'email': 'info@mscatering.com',
            'address': 'Chennai, Tamil Nadu, India',
            'business_hours': {
                'weekdays': '10:00 AM - 9:00 PM',
                'weekends': '10:00 AM - 10:00 PM',
                'closed': 'Mondays'
            }
        }
    }
    return render(request, 'contact.html', context)


def book_now(request):
    """Book now page view"""
    context = {
        'page_title': 'Book Your Event',
        'event_types': [
            'Wedding',
            'Corporate Event',
            'Birthday Party',
            'Anniversary',
            'Engagement',
            'Reception',
            'Conference',
            'Buffet Service',
            'Other'
        ],
        'guest_range': [
            '25-50',
            '50-100',
            '100-200',
            '200-500',
            '500+',
            'Unsure'
        ]
    }
    return render(request, 'book-now.html', context)


@require_http_methods(["POST"])
def submit_booking(request):
    """Handle booking form submission"""
    try:
        data = json.loads(request.body)
        # Process booking data
        # This would typically save to database
        return JsonResponse({
            'status': 'success',
            'message': 'Your booking request has been received. We will contact you soon!'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


@require_http_methods(["POST"])
def submit_contact(request):
    """Handle contact form submission"""
    try:
        data = json.loads(request.body)
        # Process contact data
        # This would typically save to database and send email
        return JsonResponse({
            'status': 'success',
            'message': 'Thank you! We have received your message. We will get back to you shortly.'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)