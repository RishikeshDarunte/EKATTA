# Password Generator – Secure and Customizable  

![Password Generator](https://img.shields.io/badge/Password%20Generator-Python%20%7C%20Flask%20%7C%20Interactive-brightgreen)  

## Overview  

- This repository provides a **Password Generator** application with both **Web-based** and **Command-line** implementations.  
- The application allows users to generate secure passwords with a mix of alphabets, numbers, and special characters, based on user-defined length criteria.

---

## Features  

 ### Command-line Password Generator:  
  - Text-based user interface for generating passwords via the terminal.  
  - Validates user input to accept only lengths >= 4.  
  - Ensures a randomized password with:  
  - 50% alphabets (uppercase and lowercase).  
  - 30% numeric digits.  
  - 20% special characters.  

 ### Web-based Password Generator:  
 - Interactive UI built with HTML and styled using CSS.  
 - Flask-powered backend for generating secure passwords.  
 - Input validation to ensure the password length is sufficient.  
 - Real-time password generation and display in the browser.  

---

## Prerequisites  

  ### For Web-based Application:  
   - Python 3.x  
   - Flask library (`pip install flask`)

  ### For Command-line Application:  
   - Python 3.x installed on your system.

---

## Installation  

1. Clone the repository:  

   ```bash
   git clone https://github.com/yourusername/password-generator.git  
   cd password-generator
   
2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv  
    source venv/bin/activate   # For Linux/Mac  
    venv\Scripts\activate      # For Windows  
 
3. Install dependencies for the Flask app:

   ```bash
   pip install flask
   ---
 
## Usage

  1. Web-based Application:
    - Navigate to the project directory.
    - Start the Flask server:
    ```bash
     python app.py  
    ``` 
    - Open your browser and go to http://127.0.0.1:5000/.
    - Enter the desired password length in the input field and click "Generate Password".

  2. Command-line Application:
   - Run the script:
   ```bash
     python Password_Generator.py 
   ```
   - Follow the on-screen instructions to enter the desired password length.
   - View the generated secure password in the terminal.

## File Structure
```bash
password-generator/  
│  
├── Password_Generator.py              # Command-line password generator script  
├── app.py                             # Flask-based backend for the web application  
├── templates/  
│   └── index.html                     # HTML template for the web app  
├── static/  
│   └── style.css                      # CSS file for styling the web app  
├── README.md                          # Project documentation  
├── requirements.txt                   # Dependencies file for the Flask app  
```

---
## Templates and Styles

  ### HTML Template (templates/index.html):
  - Displays a form for password length input.
  - The generated password dynamically.

  ### CSS (static/style.css):
  - Provides a clean, modern design for the web application.
---

## Dependencies

 - Install the required Python packages using:
    ```bash
    pip install -r requirements.txt  
    ```
---
## Customization

  ### Modifying Character Sets:

   - Edit the generate_password function in app.py or Password_Generator.py to include/exclude specific characters.

  ### Styling the Web App:

  - Update the static/style.css file to customize the appearance of the web application.

## License

   - This project is open-source under the MIT License. Contributions are welcome!
