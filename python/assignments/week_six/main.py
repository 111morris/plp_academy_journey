import requests 
import os 
from urllib.parse import urlparse 


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # this will ask the user for image url 
    url = input("please enter the image URL: ")

    try: 
        # this will create folder called "fetched_images' if it doesn't exist 
        os.makedirs("Fetched_Images", exist_ok=True)

        # this will download the image 
        response = requests.get(url, timeout=10)
        response.raise_for_status() # this will check for HTTP errors 

        # this will get the filenme from url 
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # this will set full path to save the image 
        filepath = os.path.join("Fetched_Images", filename) 

        # this will save the image to file in binary mode 
        with open(filepath, "wb") as file: 
            file.write(response.content)

        # this is the success message 
        print(f"\n Successfully fetched: {filename}")
        print(f"\n Image save to {filepath}")
        print("\n Connection strengthened. Community enriched.")
    except requests.exceptions.RequestException as e: 
        print(f"\n Network error: {e}")
    except Exception as e:
        print(f"\n Something went wrong: {e}")

if __name__=="__main__":
    main()
