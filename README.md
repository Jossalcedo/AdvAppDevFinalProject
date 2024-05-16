# AdvAppDevFinalProject
Josue Salcedo's Advanced Application Development Final Project

# Star Wars Rebellion Application

Welcome to the Star Wars Rebellion Application! This app is built using `tkinter` and `customtkinter` to provide a Star Wars-themed GUI with various functionalities. There are two versions of this app:

1. **FinalApp.py**: The basic version without database integration.
2. **StarWarsAppWithDatabaseIntegration.py**: The enhanced version with SQLite database integration.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [FinalApp.py](#running-finalapppy)
- [StarWarsAppWithDatabaseIntegration.py](#running-starwarsappwithdatabaseintegrationpy)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Star Wars-themed GUI with background image
- Navigate through different planet pages with information and fun facts
- Send transmissions to different bases
- Login functionality
- Save and retrieve transmitted messages (only in the database integration version)

## Requirements

- Python 3.6+
- `tkinter`
- `customtkinter`
- `Pillow`
- `requests`
- `pytz`
- `sqlite3` (only for database integration version)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/jossalcedo75/AdvAppDevFinalProject
    cd star-wars-app
    ```

2. **Install required packages:**

    ```sh
    pip install customtkinter pillow requests pytz
    ```

## Running the App

### Running `FinalApp.py`

1. **Navigate to the project directory:**

    ```sh
    cd FinalProjectTkinter/FinalApp.py
    ```

2. **Run the app:**

    ```sh
    python FinalApp.py
    ```

### Running `StarWarsAppWithDatabaseIntegration.py`

1. **Navigate to the project directory:**

    ```sh
    cd FinalProjectTkinter/StarWarsAppWithDataabaseIntegration.py
    ```

2. **Run the app:**

    ```sh
    python StarWarsAppWithDatabaseIntegration.py
    ```

## Usage

- **Main Page:** Navigate to different planet pages.
- **Planet Pages:** View planet information, current time, and fun facts.
- **Transmissions Page:** Send transmissions to selected bases.
- **Login Page:** Use username `luke` and password `maythe4` to login and view transmitted messages.
- **Messages Page:** View all transmitted messages (only available after login in the database integration version).

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.
