# E-Recruitment Platform

## Overview

The E-Recruitment Platform is a sophisticated tool designed to streamline the hiring process by integrating various technologies such as OCR, TF-IDF, PyResparser, Supabase Database, sentiment analysis, and automated email/calendar invite generation for parsed resumes.

## Features

- *OCR (Optical Character Recognition):*
  - Extracts text data from scanned or image-based resumes.
  
- *TF-IDF (Term Frequency-Inverse Document Frequency):*
  - Utilizes TF-IDF for analyzing the importance of words in resumes, aiding in efficient candidate shortlisting.

- *PyResparser:*
  - Extracts relevant information from resumes using PyResparser, facilitating easy categorization of candidate details.

- *Supabase Database:*
  - Leverages Supabase as the database for secure and scalable storage of candidate information.

- *Sentiment Analysis:*
  - Performs sentiment analysis on resumes to gain insights into the emotional tone of candidate applications.

- *Automated Email and Calendar Invites:*
  - Automates the process of sending emails and calendar invites to candidates, enhancing communication efficiency.

## Getting Started

1. *Installation:*
   - Clone this repository: git clone https://github.com/your-username/e-recruitment-platform.git
   - Navigate to the project directory: cd e-recruitment-platform
   - Install dependencies: pip install -r requirements.txt

2. *Configuration:*
   - Set up Supabase credentials and configure the database connection in config.py.
   - Ensure proper API keys for email and calendar integration.

3. *Running the Application:*
   - Execute the application: python app.py
   - Access the platform at http://localhost:5000 in your web browser.

## Usage

1. *Upload Resumes:*
   - Use the provided interface to upload resumes in various formats, including scanned documents.

2. *Resume Processing:*
   - The platform automatically processes resumes using OCR, TF-IDF, and PyResparser.

3. *Database Management:*
   - Candidate details are stored securely in the Supabase database, allowing for easy retrieval and analysis.

4. *Sentiment Analysis:*
   - View sentiment analysis results to understand the emotional tone of each candidate's application.

5. *Automated Communication:*
   - The platform automatically sends personalized emails and calendar invites to shortlisted candidates.

## Dependencies

- [PyResparser](https://github.com/OmkarPathak/pyresparser)
- [Supabase](https://supabase.io/)
- [NLTK](https://www.nltk.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Other dependencies listed in requirements.txt]

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
