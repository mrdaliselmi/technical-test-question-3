# Facebook Scraper

This repository contains a Python Facebook scraper. The connector allows you to collect posts, including images, text, and related comments, based on a given topic.

## Requirements

- Python 3.x
- MongoDB

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mrdaliselmi/technical-test-question-3
   ```
2. Install the requirements:

   ```bash
    pip install -r requirements.txt
    ```
## Configuration

1. Create a file named credentials.py in the project root directory.

2. Define the following credentials in the credentials.py file:

    ```python
    from enum import Enum

    class Credentials(Enum):
        MONGODB_URI = "<your-mongodb-uri>"
        DB_NAME = "<your-database-name>"
        COLLECTION_NAME = "<your-collection-name>"
    ```

Replace `<your-mongodb-uri>`, `<your-database-name>`, and `<your-collection-name>` with your actual MongoDB connection URI, database name, and collection name.

## Usage

1. Modify the scrape.py file if necessary.

2. Run the following command to start the program:

    ```bash
    python scrape.py
    ```
3. Enter the topic to search for when prompted.

4. The program will collect posts related to the given topic from the specified public pages and store them in both a JSON file and the MongoDB database.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.