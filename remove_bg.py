import requests
import json

API_KEY = json.load(open('config.json'))['remove_bg_api_key']

def remove_bg(filename: str) -> None:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(filename, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': API_KEY},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

def main():
    print('API_KEY:', API_KEY)


if __name__ == '__main__':
    main()