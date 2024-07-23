# Flask Application with User and Task Management

## Setup Instructions

### Prerequisites
- Python 3.10
- PostgreSQL

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yogesh976398/UserManagementFlaskApplication..git

2. python -m venv venv
   On Windows use `venv\Scripts\activate`

3. pip install -r requirements.txt

4. Configure the PostgreSQL database:
    Create a database named fullstack_test
    change to database url in config.py file 
    'postgresql://username:password@localhost/fullstack_test'
       
   
5. flask run 

## CI/CD Pipeline

This repository uses GitHub Actions to implement a CI/CD pipeline, ensuring continuous integration and deployment.

### Workflow Description

The GitHub Actions workflow is defined in the `.github/workflows/ci-cd.yml` file and includes the following steps:

1. **Trigger Events:**
   - The workflow is triggered on pushes to the `main` branch.
   - The workflow is also triggered on pull requests to the `main` branch.

2. **Jobs:**
   - **Build:**
     - The job runs on an `ubuntu-latest` runner.
     - A PostgreSQL service is set up to use as a database for tests.
     - Steps within the job:
       1. Checkout the code from the repository.
       2. Set up Python and install backend dependencies.
       3. Run backend tests.
       4. Set up Node.js and install frontend dependencies.
       5. Build the frontend.
       6. Deploy to Heroku if the branch is `main`.

### CI/CD Steps

1. **Continuous Integration:**
   - Automatically triggered on code changes.
   - Ensures that the codebase remains functional by running tests and builds.

2. **Continuous Deployment:**
   - Automatically deploys to Heroku when changes are pushed to the `main` branch.
   - Ensures that the latest changes are always live on the production environment.

### How It Works

1. **On Push or Pull Request:**
   - The workflow is triggered.
   - The code is checked out and dependencies are installed.
   - Backend tests are run to ensure the functionality of the backend services.
   - The frontend code is built to ensure there are no build-time errors.

2. **On Successful CI:**
   - If the branch is `main`, the code is automatically deployed to Heroku.
   - This ensures that the production environment always has the latest version of the code.

### Setting Up the CI/CD Pipeline

1. **Create a Heroku App:**
   - Create a new app on Heroku.
   - Add the Heroku Git URL to the workflow file.

2. **Add Secrets to GitHub:**
   - Add the `HEROKU_API_KEY` to the repository secrets in GitHub.

This setup ensures that any changes to the codebase are automatically tested and deployed, providing a seamless integration and deployment process.
