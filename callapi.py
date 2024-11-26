import requests
url="https://dummy.restapiexample.com/api/v1/employees"
def get_books():
    try:
        response=requests.get(url)
        if response.status_code==200:
            books=response.json()
            print(books)
        else:
            print("failed to retrive the data",response.status_code)
    except requests.exceptions.RequestException as e:
        print("error fetching")
get_books()