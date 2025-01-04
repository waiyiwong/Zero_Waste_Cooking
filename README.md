# Zero Waste Cooking

![Zero Waste Cooking Logo](static/images/zwc_logo.png)

Welcome to the Zero Waste Cooking project! This Django-based web application aims to promote sustainable cooking practices by helping users discover recipes based on ingredients they already have, reducing food waste and promoting a more environmentally friendly approach to cooking.

[View the live project here](https://zero-waste-cooking-dd20f248320d.herokuapp.com/)
(To open in a new tab/ window, press "ctrl" (or ⌘ for Mac) + click on the link)

![Responsive Mockup](static/images/responsive.png) 

## Contents

- [About the Site](#about-the-site)
- [User Experience (UX)](#user-experience-ux)
- [Scope/ Features](#features)
- [Page Features](#page-features)
  * [Landing Page with Navbar](#landing-page-with-navbar)
  * [Tagline](#tagline)
  * [Blog Post Page](#blog-post-page)
  * [Recipe Page](#recipe-page)
  * [About Page](#about-page)
  * [Footer](#footer)
- [Desktop, Tablet & Mobile View](#desktop-tablet--mobile-view)
  * [Desktop, Tablet & Mobile Differences](#desktop-tablet--mobile-differences)
  * [Tablet View](#tablet-view)
  * [Mobile View](#mobile-view)
- [Design](#design)
  * [Wireframes](#wireframes)
  * [Colour Scheme](#color-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
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

## User Experience (UX)

### User Stories

- (MVP) As a first-time visitor, I want to easily understand the main purpose of the site and learn more about zero-waste cooking, so that I can decide whether to use it or not.
- (MVP) See recipes and blog posts: As a user, I want to be able to see recipes and blog posts, so that I can learn more about zero-waste recipes and cooking techniques.
- (MVP) Sign up as a member to comment: As a user, I want to sign up as a member, so that I can comment on recipes and posts.
- (MVP) Sign in to post, edit, and delete posts and comments: As a logged-in user, I want to be able to post, edit, and delete posts and comments.
- (MVP) Comment on recipes and engage with other users: As a user, I want to be able to comment on recipes and engage with other users, so that I can learn from others, share my tips, and build a community around zero-waste cooking.
- Search for recipes by ingredients: As a user, I want to search for recipes based on ingredients I have available, so that I can use up what I have and avoid food waste.
- Share recipes with the community: As a registered user, I want to be able to share my own recipes with the community, so that I can contribute to the site and help others.
- Save favorite recipes: As a user, I want to be able to save my favorite recipes for easy access later, so that I can quickly find and cook the recipes I enjoy.
- Sign-in to see my personal profile page: As a user, I want to be able to sign in to the app so that I can access my personal information and settings.
- Scan food barcode to log ingredients: As a user, I want to be able to scan the barcode of a food item, so that I can easily log its ingredients.
- Show nutrition value and calculate calories: As a user, I want to be able to see the nutrition value of a food item and calculate its calories, so that I can make informed choices about what I eat.

## Scope / Key Features

- Ingredient-based recipe search
- Rich text editor for blog & recipe posts
- Image upload for blog & recipe posts
- User authentication (register, login, logout)
- Registered users reate, read, update, and delete comment on recipes
- Responsive design for various devices

## Page Features

### Landing Page with Navbar
The landing page features a hero image that visually communicates the purpose of the site — promoting zero waste cooking. It highlights the benefits of sustainable cooking practices, offering users an introduction to the core values of zero waste cooking.

### Tagline
"Cook Hero, Waste Hero" — A tagline that encapsulates the spirit of sustainable and mindful cooking, encouraging users to become heroes in their kitchens by reducing waste.

### Blog Post Page
  This page shares zero waste cooking tips, practical advice on reducing food waste, and insights into sustainable practices. It serves as an educational hub for visitors seeking to improve their cooking habits.

### Recipe Page
  The recipe page features zero waste cooking recipes, detailed instructions, and options for dietary preferences. The goal is to provide easy-to-follow, eco-conscious recipes that help users reduce waste in the kitchen.

### About Page
  Learn about the origins of the Zero Waste Cooking website, the motivations behind creating this platform, and the community it seeks to build. The page includes a call to join the zero waste community and a contact form with validation to ensure user inquiries are received and addressed.

### Footer
The footer includes essential copyright information and social media links for users to stay connected and engage with the Zero Waste Cooking community online.

## Desktop, Tablet & Mobile View
![Desktop, Tablet & Mobile View](static/images/responsive.png)
### **Desktop, Tablet & Mobile Differences**  
Bootstrap 5.3.3 was implemented to ensure full responsiveness across all devices. Key features include:

- Fluid containers and a responsive grid system that adapt to screen sizes.
- Content stacks vertically on mobile devices, while multi-column layouts are used on larger screens.
- The navbar transforms into a collapsible hamburger icon on smaller screens for easy navigation.

This approach provides an optimal viewing experience, maintaining readability and usability with minimal resizing and scrolling across all devices.

## Design

### Wireframes

Wireframe - Homepage Desktop & Mobile
![wireframe.png](static/images/wireframe.png)

### Color Scheme

The color scheme focuses on sustainability, complemented by a natural, organic feel.

![Zero Waste Cooking color scheme](static/images/color_scheme.png)

- Background Colors: #252426 & #F9FAFC
- Primary Color: #80A665
- Secondary Color: #FBFFFA
- Text Color: #577F40 & #ACC58E

[Adobe Color](https://color.adobe.com/create/color-wheel) is used to generate color scheme.

[Adobe Color](https://color.adobe.com/create/color-contrast-analyzer) checks the color contrast (accessibility) of the site.

For Dark Background
![color contrast test pass)](static/images/color_contrast.png)
For Light Background
![color contrast on nav bar test pass)](static/images/color_contrast2.png)

### Typography

The site uses a clean, modern "League Gothic", serif fonts for easy readability across devices. [Google Fonts](https://fonts.google.com/) is used to import the fonts.

### Imagery

I used AI image generation (via Freepik) to create the majority of the images on the site. These AI-generated images served as the foundation for redesigning and customizing the logo, hero image, and post images. The final designs were refined by myself using Adobe Fresco and Canva. 
The recipe imagery throughout the site is focused on fresh ingredients, completed dishes, and sustainable cooking practices.

## Features

### Existing Features

1. **Responsive Navigation Bar**: Allows users to easily navigate the site on all devices.
2. **User Authentication**: Enables users to register, log in, and log out.
3. **Recipe Search**: Allows users to search for recipes based on available ingredients.
4. **Dietary Preference Search**: filters dietary restrictions and cuisine type
5. **Recipe Details Page**: Displays full recipe information, including ingredients, instructions, and user comments.
6. **Commenting System**: Allows users to engage with recipes by leaving comments.
7. **Responsive Design**: Ensures the site is fully functional and visually appealing on all device sizes.

### Features Left to Implement

- Recipe rating system
- Like and add-to-favourite buttons
- User Profile page
- Social media sharing integration
- User Recipe Creation and Management

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
8. Google Dev Tools - to debug and for testing responsiveness 
9. [Am I Responsive](https://ui.dev/amiresponsive) and [Ignore X-Frame Headers Extension](https://chromewebstore.google.com/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe) - to acquire the responsiveness screenshot

## Testing
To ensure the functionality and reliability of the site, both automated and manual testing were adopted throughout the development process. 

Automated tests were implemented to check for common issues and verify the integrity of key features. 

Manual testing was performed on various devices, including the iPhone 15 Pro, Sony Xperia, iPad Pro, MacBook Air, and MacBook Pro, to assess the site's responsiveness, accessibility, and user experience across different screen sizes and platforms. This combination of automated and manual testing ensures the site’s performance and quality are maintained across a range of devices.

### Google Lighthouse performance
for auditing the website
<details open>
<summary>Google Lighthouse Performance Score</summary>  

![Google Lighthouse Performance.png](documentation/light_house_score.png)
</details>   

### HTML Validation
[W3C HTML Validation](https://validator.w3.org/) is used to validate html codes
<details open>
<summary>HTML validation</summary>  

![w3c_html_validation.png](documentation/html_validation.png)
</details>   

### CSS Validation
[Jigsaw](https://jigsaw.w3.org/css-validator/) is for validating my CSS
<details open>
<summary>CSS validation</summary>  

![w3c_css_validation.png](documentation/css_validation.png)
</details>

### Javascript Validation

<details open>
<summary>JS validation</summary>  

![w3c_css_validation.png](documentation/js_validation.png)
</details>   

### Python Validation
[Pep8](https://pep8ci.herokuapp.com/) is used to validate if my python code meet Pep8 Standards
<details open>
<summary>Python validation</summary>  

![python_validation.png](documentation/python_validation.png)
</details>  


### **Bugs & Fixes**
- Failed to render recipe app (- check all python files in recipe app and project level urls.py, seek help from Google, chatGPT and Slack community)
- Failed to load images when debug mode switched from true to false (1. check all python files in recipe app and project level urls.py, seek help from Google, chatGPT and Slack community. 2. make sure all images file in static folder and correct directory and then run command in terminal "python3 manage.py collectstatic". )
- Failed to load cloudinary images after deploying to Heroku (- Set Config Vars and Cloudinary_URL on Heroku)

### **Unsolved Bugs**

## Deployment

### Deploying to Heroku

This project is deployed on Heroku. Here are the steps to deploy:

1. Create a Heroku account and log in.
2. Click "New" and select "Create new app".
3. Choose a name for my app and select my region.
4. In the "Deploy" tab, connect your GitHub repository.
5. In the "Settings" tab, add the following config vars:
   - SECRET_KEY: My Django secret key
   - DATABASE_URL: My PostgreSQL database URL
   - CLOUDINARY_URL: My Cloudinary URL
6. Add the Python buildpack to your app.
7. In the "Deploy" tab, click "Deploy Branch" to deploy my app.

## Credits

### Code

- [Django Documentation](https://docs.djangoproject.com/): Used extensively for guidance on Django best practices and implementation.
- [Bootstrap Documentation](https://getbootstrap.com/docs/): Used for responsive design components and styling.

### Content

- All recipe content is added by the site admin for demonstration purposes.

### Media

- Default recipe images and site graphics are sourced from [Freepik](https://www.freepik.com/) and [Fontawesome](https://fontawesome.com/).

### AI Assistance
- V1
- ChatGPT

### Acknowledgements

- SME (Mark), coding coach (John and Roo) and facilitators (Marko, Shelly, Vasi) for continuous helpful feedback.
- The Code Institute Slack community for their support and advice.