import os
import requests


def get_extensions(img_url: str) -> str | None:
    extensions: list[str] = [".png", ".jpg", ".jpeg", ".svg", ".gif"]
    for ext in extensions:
        if img_url.endswith(ext):
            return ext


def download_image(img_url: str, img_name: str) -> None:
    if ext := get_extensions(img_url):
        img_name: str = f"{img_name}{ext}"
    else:
        raise Exception("img extension not found in the list")

    # check the file already exit
    if os.path.exists(img_name):
        raise Exception("img name already exists")

    # download img
    try:
        img_content: bytes = requests.get(img_url).content
        with open(img_name, "wb") as handler:
            handler.write(img_content)
            print(f"Downloaded image {img_name} successfully")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    img_link: str = input("Enter the url of the Img: ")
    name: str = input("Enter the name of Img: ")

    print("Downloading image...")
    download_image(img_link, name)
