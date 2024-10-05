# flask-feedback-application with CI/CD pipeline on AWS
This project is a Flask-based feedback application that is deployed using a CI/CD pipeline on AWS. The application is containerized using Docker and automatically deployed with each code change.

File Structure
---
flask-feedback-app/
│
├── app.py                  # Main Flask application
├── Dockerfile              # Docker configuration file for building the image
├── requirements.txt        # Python dependencies for the project
├── templates/              # HTML templates for the Flask app
│   └── index.html          #feedback form html template
|   └── thankyou.html       #thankyou greeting form template     
├── appspec.yml             #configuration file used by codedeploy     
├── buildspec.yml           #configuration file for codebuild
├── start_container.sh      #applicationstart script
├── README.md               # Project documentation
---




