*Instagram Fetcher API*

1) System Overview

The Instagram Fetcher API is a Django-based service that retrieves the latest post (caption and image URL) from a specified Instagram account. If Instagram API access is unavailable, web scraping is used as a fallback.

Architecture
	1.	The client sends a request to fetch the latest Instagram post.
	2.	The system retrieves the latest post’s caption and image URL using either:
	•	Instagram’s API (if access is granted).
	•	Web scraping (if API access is restricted).
	3.	The API returns a structured response containing the caption and image URL.
	4.	Errors such as network failures or API rate limits are logged appropriately.

2) Setup Instructions

Prerequisites
	•	Python 3.8 or higher
	•	Django 4.0 or higher
	•	pip (Python package manager)
	•	GitHub account (for source code management)
	•	Virtual environment (recommended)

Installation
	1.	Clone the repository using Git.
	2.	Navigate into the project directory.
	3.	Create and activate a virtual environment.
	4.	Install dependencies using the requirements.txt file.
	5.	Create an .env file in the root directory and add the required environment variables such as Instagram username and password.
	6.	Apply database migrations.
	7.	Run the development server and access the API via the provided endpoint.

3) Project Structure

The project follows Django’s default structure with the main app named fetcher, responsible for handling Instagram post retrieval.
	•	The fetcher app contains the necessary files for handling API requests, including views.py for request handling and urls.py for defining API endpoints.
	•	The main Django project directory contains the settings and configuration files.
	•	The .env file stores environment variables required for API authentication.
	•	The requirements.txt file lists all required dependencies for setting up the project.

4) API Endpoints

The API provides a single endpoint for fetching the latest Instagram post.
	•	Method: GET
	•	Endpoint: /fetcher/fetch-latest-post/
	•	Description: Fetches the latest Instagram post, including its caption and image URL.
	•	Response Format: Returns a JSON response containing the username, caption, and image URL.
	•	Error Handling: If the post cannot be fetched, an error message is returned in JSON format.

5) Configuration

The Instagram username can be modified by updating the .env file and restarting the server. This allows flexibility in targeting different Instagram accounts.

6) Deployment

Deploying with Docker
	1.	Build the Docker image using the provided Dockerfile.
	2.	Run the container with the necessary environment variables.
	3.	Access the API at the specified local or deployed URL.

7) Automation

Linux/macOS (Cron Job)

To schedule the fetching process at regular intervals, a cron job can be configured to run the fetch command at a specified time interval.

8) Windows (Task Scheduler)

The Task Scheduler can be used to run the fetch script periodically by creating a new scheduled task that executes the appropriate command.

Contribution
	•	Fork the repository and create a new branch for any modifications.
	•	Submit pull requests for improvements or bug fixes.
	•	Report any issues via the GitHub Issues section.
