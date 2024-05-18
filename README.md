# Kidsworld

Kidsworld is a children's story platform developed as a group project for the AXSOS Academy Dojo programming course. This application allows users to explore, read, and interact with various children's stories. Key features include user authentication, adding to favorites, search functionality, story details with PDF interaction, a rating system, and admin capabilities for managing stories.

## Technologies Used

- **Frontend**: HTML, CSS, SCSS, JavaScript, Bootstrap, jQuery
- **Backend**: Python, Django
- **Libraries**: Mixitup, PDF.js, Crispy Forms, AJAX
- **Other Tools**: Trello

## Deployment

The project is deployed on AWS. You can access it [here](http://16.171.135.225/).

## Features

### 1. User Authentication
- **Django Authentication**: Utilizes Django’s built-in user authentication system.
- **Custom Forms**: Forms customized using the crispy-forms library.
- **Validation**: Includes both frontend and backend validation.
- **AJAX**: Enhances user experience by avoiding page reloads during authentication processes.
- **[Watch Video](https://drive.google.com/file/d/1bfNjkt7KL0r9-0kS_2kZOuE6GciiHl9H/view?usp=sharing)**

### 2. Favorites Management
- Users can add stories to their favorites and remove them as needed.
- **[Watch Video](https://drive.google.com/file/d/1CAbBKVdOtfu72rM5JEgs9hWnOEoFytLe/view?usp=sharing)**

### 3. Search and Filtering
- **Title Search**: Allows users to search for stories by their titles.
- **Category Search**: Users can filter stories by category using the Mixitup library.
- **AJAX**: Implements AJAX for smooth and dynamic searching and filtering.
- **[Watch Video](https://drive.google.com/file/d/1rkEEeukveSZ1NL9GZlJih695Xn3rPJnQ/view?usp=sharing)**

### 4. Story Details and PDF Interaction
- **Story Details**: Detailed view of each story including comments and ratings.
- **PDF Interaction**: Users can read or download stories in PDF format using PDF.js.
- **Comments**: Users can add, delete, and view comments on stories.
- **[Watch Video](https://drive.google.com/file/d/1E8nn3tjmyq_lMt61osy0wpfZ9Cy6YzK2/view?usp=sharing)**

### 5. Rating System
- **Story Rating**: Users can rate stories.
- **Average Rating**: Each story’s average rating is dynamically updated based on user ratings.
- **[Watch Video](https://drive.google.com/uc?id=1Mfct5I8wmCLtwtUt5Nhf0M3UuULezzzK&export=download)**

### 6. Admin Capabilities
- **Story Management**: Admins can add new stories, view all stories, update existing stories, and delete stories.
- **[Watch Video](https://drive.google.com/file/d/1nS7LJoXBinUi34rImteIgDIg-Pu5SHnI/view?usp=sharing)**

## Installation

To run this project locally:

1. Clone the repository:
   git clone https://github.com/Farhoud-Rand/KidsWorld.git
2.Navigate to the project directory:
   cd kidsworld
3. Create a virtual environment:
   python -m venv env
4.Activate the virtual environment:
   - On Windows:
      .\env\Scripts\activate
   - On macOS and Linux:
      source env/bin/activate
5.Install the dependencies:
   pip install -r requirements.txt
6.Apply migrations:
   python manage.py migrate
7.Run the development server:
   python manage.py runserver
8.Open your web browser and go to http://127.0.0.1:8000/ to see the application in action.

## Contributors

- [Rand Farhoud](https://www.linkedin.com/in/rand-farhoud-301b64184/)
- [Sajeda Abu Ayyash](https://www.linkedin.com/in/sajeda-abu-ayyash-b09351251/)
- [Ziad Disi](https://www.linkedin.com/in/ziad-disi-7945b01ab/)

## Screenshots of the website (KidsWorld) :

Home page :
---

![image](https://github.com/Farhoud-Rand/KidsWorld/assets/162067676/0ce8ef08-1b9e-448e-a3ba-885a802637f8)

![image](https://github.com/Farhoud-Rand/KidsWorld/assets/162067676/e7915464-0dca-4c6f-96b4-0c93d5ce2334)


Profile :
---

![image](https://github.com/Farhoud-Rand/KidsWorld/assets/162067676/8cd6959c-152c-4b66-9377-5dce839a8927)

---

Favorite list :
---

![image](https://github.com/Farhoud-Rand/KidsWorld/assets/162067676/077fe1fe-6904-4cbe-9dc6-33a7e3df136d)

About Us :
---

![image](https://github.com/Farhoud-Rand/KidsWorld/assets/162067676/3c17069c-74d6-408c-a87f-863ae93bb3f5)

Contact page :
---

![image](https://github.com/Farhoud-Rand/KidsWorld/assets/162067676/a61eeab2-77f2-42d0-9efc-271cef5afc02)


Story details :
---

![image](https://github.com/Farhoud-Rand/KidsWorld/assets/162067676/88cc0196-5d74-48d1-bd0c-b7cbf871ebee)


![image](https://github.com/Farhoud-Rand/KidsWorld/assets/162067676/92dd8bec-9e64-45a8-b648-a14e361170fb)
