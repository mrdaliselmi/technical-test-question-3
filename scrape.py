from facebook_scraper import get_posts
from datetime import datetime
from pymongo import MongoClient
from credentials import Credentials
import json

def getPosts(keyword, public_pages, load_comments=True):
    """
    Returns a list of posts from the given public pages that contain the given keyword.
    
    Parameters:
        keyword (str): The keyword to search for in the posts.
        public_pages (list): A list of public pages to search for posts.
        load_comments (bool): Whether to load the comments of the posts or not.
    
    Returns:
        list: A list of posts that contain the given keyword.
    """
    data = []
    keyword = keyword.lower()
    
    for page in public_pages:
        for post in get_posts(page, pages=10, options={"comments": load_comments}):
            if (post['text'] is not None):
                text = post['text']
                if (text.lower().find(keyword) != -1):
                    p = {
                        'post_text': post['text'],
                        'post_comments': post['comments'],
                        'likes': post['likes'],
                        'image': post['image'],
                        'post_url': post['post_url'],
                        'post_id': post['post_id'],
                        'shares': post['shares'],
                        'reaction_count': post['reaction_count']
                    }
                    data.append(p)
        if not data:
            break
    return data

def writeToFile(data,keyword):
    """
    Writes the given data to a JSON file.
    
    Parameters:
        data (list): The data to write to the file.
        keyword (str): The keyword used to search for the data.
        
    Returns:
        str: The name of the file that the data was written to.
    """
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    file_name = f"{keyword}_{timestamp}.json"

    with open(file_name, 'w') as file:
        json.dump(data, file)
    return file_name

def saveToDatabase(data, collection_name):
    """
    Saves the given data to the database.
    
    Parameters:
        data (list): The data to save to the database.
        collection_name (str): The name of the collection to save the data to.
    """
    client = MongoClient(Credentials.MONGODB_URI.value)
    db = client[Credentials.DB_NAME.value]
    collection = db[collection_name]
    collection.insert_many(data)
    client.close()


def main():
    football_pages = ['ESPNFC','BleacherReportFootball','goalglobal','goal','90minFootball','SkySportsFootball','BBCSport','SportsCenter']
    news_pages = ['cnn','FRANCE24', 'BBCWorld', 'AJEnglish', 'AlJazeeraEnglish', 'euronews', 'euronewsfr', 'euronewsar', 'euronewsit', 'euronewsde', 'euronewspt', 'euronewsru', 'euronewsfa', 'euronewsgr', 'euronewsen', 'euronewsuk', 'euronewses', 'euronewstr']
    tunisian_pages = ['mosaiquefm', 'sabrafm', 'Radio.JawharaFM', 'TVN.Tunisie']
    test = ['ESPNFC']
    keyword = input("Enter the topic to search: ")
    data = getPosts(keyword, test, load_comments=False)
    file_name = writeToFile(data, keyword)
    saveToDatabase(data, keyword)
    print(f"Data written to {file_name} successfully.")

if __name__ == "__main__":
    main()