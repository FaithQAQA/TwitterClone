# Musker - Twitter Clone

A social media platform inspired by Twitter, built with Django. Users can post "Meeps" (similar to tweets), follow other users, like posts, reply to meeps, and upload videos.

## Features

- **User Authentication**: Register, login, and logout functionality
- **User Profiles**: Custom profiles with bio, profile picture, and social media links
- **Meeps**: Post text-based messages (up to 200 characters) with optional video uploads
- **Likes**: Like and unlike meeps
- **Replies**: Reply to meeps
- **Following System**: Follow and unfollow other users
- **Search**: Search for users and meeps
- **CRUD Operations**: Edit and delete your own meeps
- **Followers/Following Lists**: View who follows you and who you follow

## Technologies Used

- **Backend**: Django 4.2.7
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS, JavaScript
- **Media Handling**: Django's file upload system for images and videos

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd TwitterClone
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install django
   ```

5. **Navigate to the Django project directory**:
   ```bash
   cd social
   ```

6. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser (optional, for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- **Register**: Create a new account
- **Login**: Log in with your credentials
- **Home**: View all meeps from all users
- **Profile**: View and edit your profile
- **Post Meep**: Share your thoughts with text and optional video
- **Like/Reply**: Interact with other users' meeps
- **Follow**: Follow users to see their meeps in your feed
- **Search**: Find users or specific meeps

## Project Structure

```
social/
├── db.sqlite3                    # SQLite database
├── manage.py                     # Django management script
├── media/                        # User-uploaded media files
│   ├── images/                   # Profile images
│   └── meep_videos/              # Meep videos
├── musker/                       # Main Django app
│   ├── migrations/               # Database migrations
│   ├── static/                   # Static files (CSS, JS, images)
│   ├── templates/                # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                  # Django forms
│   ├── models.py                 # Database models
│   ├── tests.py
│   ├── urls.py                   # URL patterns
│   └── views.py                  # View functions
└── social/                       # Django project settings
    ├── __init__.py
    ├── asgi.py
    ├── settings.py               # Project settings
    ├── urls.py                   # Main URL configuration
    └── wsgi.py
```

## Models

- **User**: Django's built-in User model
- **Profile**: Extended user profile with bio, links, and profile image
- **Meep**: Main content model (posts) with text, video, likes, and timestamps
- **Reply**: Replies to meeps

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open-source. Feel free to use and modify it.

## Disclaimer

This is a learning project and not intended for production use without proper security audits and optimizations.</content>
<parameter name="filePath">D:\FixProjects\TwitterClone\README.md