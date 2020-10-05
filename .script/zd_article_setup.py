import json
import os
import requests
import logging

from pathlib import Path

DENY_LIST = ['index', 'template', 'TOC']
BASE_PATH = Path('/builds/flywheel-io/public/flywheel-tutorials/')

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%y %H:%M:%S')
log = logging.getLogger('root')

def main():
    try:
        public_dir = BASE_PATH / 'public'
        os.chdir(public_dir)
        current_dir = os.getcwd()
        ZD_PERMISSION_GROUP_ID = os.environ.get('ZD_PERMISSION_GROUP_ID')
        

        if os.path.isdir(current_dir):
            for file in os.listdir(current_dir):
                if file.endswith('.html') and not any(file.startswith(name) for name in DENY_LIST):
                    title = file.replace('-', ' ').replace('_', ' ').replace('.html', '').title()
                    log.info(f'*** Processing File {title} ***')
                    article_obj = create_article_obj(file, title, ZD_PERMISSION_GROUP_ID)

                    if len(article_obj) >= 0:
                        with open('article.json', 'w') as output_files:
                            json.dump(article_obj, output_files)
                        article_json_path = public_dir / 'article.json'
                        publish_article(article_json_path, title)

    except (OSError, IOError) as e:
        log.exception(f'Error: {e}')
    except Exception as exception:
        log.exception(f'Error: {exception}')


def create_article_obj(filepath, title, permission_group_id):
    body_value = f"<div><iframe width=\"900\" height=\"800\" src=\"https://flywheel-io.gitlab.io/public/flywheel-tutorials/{filepath}\"></iframe></div>"

    article_dict = {"article": {
        "body": body_value,
        "locale": "en-us",
        "permission_group_id": int(permission_group_id),
        "title": title,
        "user_segment_id": None},
        "notify_subscribers": False}

    return article_dict


def publish_article(json_file_path, title):
    log.info(f'--- Publishing {title} to ZenDesk ---')
    # Set the target Zendesk subdomain (subdomain.zendesk.com)
    subdomain = 'flywheelio'

    try:
        ZD_USER = os.environ.get('ZD_USER')
        ZD_API_TOKEN = os.environ.get('ZD_TOKEN')
        ZD_SECTION_ID = os.environ.get('ZD_SECTION_ID')
    except Exception as e:
        log.exception(f'Error: {e}')

    # Set the request parameters
    apiEndPoint = '/api/v2/help_center/sections/' + ZD_SECTION_ID
    url = 'https://' + subdomain + '.zendesk.com' + apiEndPoint + '/articles'

    # Get the file containing the article in JSON
    articleJSON = json_file_path

    # New article data packaged in a dictionary matching the expected JSON
    with open(articleJSON, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    # Encode the data to create a JSON payload
    payload = json.dumps(data)

    headers = {'content-type': 'application/json'}

    # Do the HTTP post request
    response = requests.post(url, data=payload, auth=(ZD_USER, ZD_API_TOKEN), headers=headers)

    # Check for HTTP codes other than 201 (Created)
    if response.status_code != 201:
        log.exception(
            f'Status: {response.status_code}. Problem with the request and unable to publish {title}. Exiting.')
    else:
        # Report success
        log.info(f'Successfully created {title} on ZenDesk.')


if __name__ == "__main__":
    main()
