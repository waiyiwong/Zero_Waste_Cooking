# Zero Waste Cooking

![Zero Waste Cooking Logo](/static/images/logo.jpg)

Welcome to the Zero Waste Cooking project! This Django-based web application aims to promote sustainable cooking practices by helping users discover recipes based on ingredients they already have, reducing food waste and promoting a more environmentally friendly approach to cooking.

[View the live project here](#) (Link to be added when deployed)

![Responsive Mockup](#) 

## Contents

- [About the Site](#about-the-site)
- [User Experience (UX)](#user-experience-ux)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## About the Site

### Primary Goal

The Zero Waste Cooking website aims to reduce food waste and promote more environmentally friendly cooking habits by providing a platform for users to discover recipes based on ingredients they already have, share their own recipes, and learn about sustainable cooking practices.

### Target Users

Our target audience includes:

- Anyone looking to save money by making the most of their existing ingredients
- Home cooks of all skill levels seeking inspiration for meal preparations using available ingredients
- People interested in sharing their own zero-waste recipes and cooking tips
- Environmentally conscious individuals looking to reduce food waste

### Key Features

- Ingredient-based recipe search
- User authentication (register, login, logout)
- Create, read, update, and delete recipes
- Image upload for recipes
- Comment on recipes
- Responsive design for various devices
- Rich text editor for recipe instructions
- User profile pages for saving preferences and favorite recipes

## User Experience (UX)

### User Stories

- (MVP) As a first-time visitor, I want to easily understand the main purpose of the site and learn more about zero-waste cooking, so that I can decide whether to use it or not.
- (MVP) See recipes and blog posts: As a user, I want to be able to see recipes and blog posts by the admin, so that I can learn more about zero-waste recipes and cooking techniques.
- (MVP) Sign up as a member to comment: As a user, I want to sign up as a member, so that I can comment on recipes and posts.
- (MVP) Sign in to post, edit, and delete posts and comments: As a logged-in user, I want to be able to post, edit, and delete posts and comments.
- (MVP) Comment on recipes and engage with other users: As a user, I want to be able to comment on recipes and engage with other users, so that I can learn from others, share my tips, and build a community around zero-waste cooking.
- Search for recipes by ingredients: As a user, I want to search for recipes based on ingredients I have available, so that I can use up what I have and avoid food waste.
- Share recipes with the community: As a registered user, I want to be able to share my own recipes with the community, so that I can contribute to the site and help others.
- Save favorite recipes: As a user, I want to be able to save my favorite recipes for easy access later, so that I can quickly find and cook the recipes I enjoy.
- Sign-in to see my personal profile page: As a user, I want to be able to sign in to the app so that I can access my personal information and settings.
- Scan food barcode to log ingredients: As a user, I want to be able to scan the barcode of a food item, so that I can easily log its ingredients.
- Show nutrition value and calculate calories: As a user, I want to be able to see the nutrition value of a food item and calculate its calories, so that I can make informed choices about what I eat.


### Design

#### Color Scheme

The color scheme focuses on sustainability, complemented by a natural, organic feel.

- Primary Color: #
- Secondary Color: # 
- Text Color: #
- Background Color: #

#### Typography

The site uses a clean, modern sans-serif font for easy readability across devices.

#### Imagery

The imagery used throughout the site focuses on fresh ingredients, finished dishes, and sustainable cooking practices. User-uploaded images for recipes play a central role in the visual experience.

## Features

### Existing Features

1. **Responsive Navigation Bar**: Allows users to easily navigate the site on all devices.
2. **User Authentication**: Enables users to register, log in, and log out.
3. **Recipe Search**: Allows users to search for recipes based on available ingredients.
4. **Recipe Creation and Management**: Users can create, edit, and delete their own recipes.
5. **Recipe Details Page**: Displays full recipe information, including ingredients, instructions, and user comments.
6. **User Profiles**: Personal pages for users to manage their recipes and preferences.
7. **Commenting System**: Allows users to engage with recipes by leaving comments.
8. **Responsive Design**: Ensures the site is fully functional and visually appealing on all device sizes.

### Features Left to Implement

- Recipe rating system
- Social media sharing integration
- Advanced search filters (dietary restrictions, cuisine type, etc.)
- Meal planning feature

## Technologies Used

### Languages Used

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks, Libraries & Programs Used

1. [Django](https://www.djangoproject.com/): The main framework used to build the project.
2. [PostgreSQL](https://www.postgresql.org/): Database used to store recipe and user data.
3. [Bootstrap](https://getbootstrap.com/): Used for responsive design and styling.
4. [Git](https://git-scm.com/): Used for version control.
5. [GitHub](https://github.com/): Used to store the project repository.
6. [Cloudinary](https://cloudinary.com/): Used for image hosting and management. (If implemented)
7. [Gunicorn](https://gunicorn.org/): Used as the HTTP server for deploying the Django application.

## Testing

HTML
CSS
Python

## Deployment

### Deploying to Heroku

This project is deployed on Heroku. Here are the steps to deploy:

1. Create a Heroku account and log in.
2. Click "New" and select "Create new app".
3. Choose a name for your app and select your region.
4. In the "Deploy" tab, connect your GitHub repository.
5. In the "Settings" tab, add the following config vars:
   - SECRET_KEY: Your Django secret key
   - DATABASE_URL: Your PostgreSQL database URL
   - ALLOWED_HOSTS: The URL of your Heroku app
6. Add the Python buildpack to your app.
7. In the "Deploy" tab, enable automatic deploys from your main branch.
8. Click "Deploy Branch" to deploy your app.

## Credits

### Code

- [Django Documentation](https://docs.djangoproject.com/): Used extensively for guidance on Django best practices and implementation.
- [Bootstrap Documentation](https://getbootstrap.com/docs/): Used for responsive design components and styling.

### Content

- All recipe content is user-generated or added by the site admin for demonstration purposes.

### Media

- Default recipe images and site graphics are sourced from [Pexels](https://www.pexels.com/) and [Fontawesome](https://fontawesome.com/).

### Acknowledgements

- SME (Mark), coding coach (John and Roo) and facilitators (Marko, Shelly, Vasi) for continuous helpful feedback.
- The Code Institute Slack community for their support and advice.