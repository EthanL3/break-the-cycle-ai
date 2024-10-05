# break-the-cycle-ai

A Flask-based web application that provides therapy solutions for users struggling with different mental health issues, using principles of Cognitive Behavioral Therapy (CBT). The app walks users through a series of questions and provides appropriate therapy solutions based on their responses. The app also handles immediate crises, recommending contact with professional services if needed.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- Guided question flow based on a predefined CBT flowchart.
- Generates therapy solutions tailored to the user's answers using Cognitive Behavioral Therapy (CBT) principles.
- Provides urgent recommendations if the user indicates they are at risk of harm or relapse.
- Dynamically updates questions and prompts without reloading the page.
- Integration with emergency contact information for high-risk users.

## Technologies
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI/LLM**: Pre-built CBT-based responses (can be expanded to use an AI model for more dynamic responses)
- **Video**: Background video support for aesthetic and calming effects
- **Version Control**: Git

## Setup
### Prerequisites
- Python 3.x
- `pip` (Python package manager)
- A virtual environment for managing dependencies (optional but recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cbt-assistant.git
   cd cbt-assistant
   ```
2. **Create and activate a virtual environment (optional)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the flask app:**:
    ```bash
    flask run
    ```
5. The app should now be running at http://127.0.0.1:5000/.

