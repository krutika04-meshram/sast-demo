import requests

def get_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url, timeout=5)
    print(response.json())

if __name__ == "__main__":
    get_data()