# spy_cat_agency

## Description
This application allows you to manage spy cats, missions, and targets in a system. It provides endpoints for creating, updating, and deleting cats, missions, and targets. You can also associate targets with specific missions and manage their completion status.

## Requirements
- Docker

## Setup Instructions

1. **Clone the Repository**:
   First, clone the repository to your local machine.

2. **Create a `.env` File**:
   Copy the contents of the `.env.template` file and create a new `.env` file in the root directory of the project.

3. **Run the Application Using Docker**:
   Make sure Docker is installed and running on your machine. Then, execute the following command in your terminal:
   ```bash
   bash docker-launch.sh
   
4. **If the application doesn't start initially (due to the database being in the process of starting), follow these steps**:
   Start the database:
   ```bash
   docker-compose up db
   ```

   **Wait for the database to fully initialize, then start the backend**:
   ```bash
   docker-compose up backend
   ```

5. **Postman link**:
https://drive.google.com/file/d/1a0SVz9FbhIDMXOAmx7Vz5MpCI81gEPnf/view?usp=sharing