# sidr-ai

## Table of Contents

- [Project Installation](#installation)
- [License](#license)
- [Acknowledgments](#acknowledgments)


## Project Installation

1. Clone the repository

### Frontend Installation

1. Take a pull from repo

2. Navigate to the Frontend directory:
    ```shell
   cd sidr-ai/frontend

3. Run command to install dependency:
    - npm install

4. Run command to install dependency:
    - npm run build

5. Start an react app
    - npm start

### Backend Installation

2. Navigate to the project directory:
    ```shell
   cd sidr-ai

3. Create a virtual environment:
   ```shell
   python -m venv .venv-sidr

4. Activate virtual environment:
   - Navigate to the virtual environment directory:
      ```shell
      cd .venv-sidr
   - For windows
      - ```shell
         cd Scripts
      - ```shell
         activate
   - For Mac
      ```shell
      source bin/activate

5. Navigate to the backend directory.

6. Install pip-tools using below command:
    ```shell
   pip install pip-tools

7. Generate requirements.txt file from requirements.in:
    ```shell
   pip-compile requirements.in -o requirements.txt

8. Install dependencies using pip:
    ```shell
   pip install -r requirements.txt

9. Set up your environment variables as described in the Configuration section.
    - set app_env in confif/.env file to developmet or production (Optional)

10. Copy the Frontend Build to the Backend:
    - Make Sure you are in sidr-ai folder in terminal
    ```shell
    cp -r frontend/build backend/  

11. Start the FastAPI application:
   - To start the FastAPI application, use the following commands depending on your environment:

      - ### Development Environment
         ```shell
         APP_ENV=development uvicorn app.main:app
      - ### Production Environment
         ```shell
         APP_ENV=production uvicorn app.main:app

- Or simply run below command
     ```shell
    uvicorn app.main:app


Test the authentication:
1. Hit login endpoint with below payload
    - Endpoint: http://127.0.0.1:8000/sidr-ai/login
    - payload : {
                    "username": "user1",  // change username as per ldap
                    "password": "password1" // change password as per ldap
                }
