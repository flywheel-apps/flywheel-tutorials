import json
import os
import requests
import logging

DENYLIST = ['index', 'template']

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
log = logging.getLogger('root')

def main():
    try:
        os.chdir('/builds/flywheel-io/public/flywheel-tutorials/public')
        current_dir = os.getcwd()
        ZD_PERMISSION_GROUP_ID = os.environ.get('ZD_PERMISSION_GROUP_ID')
        ZD_USER_SEGMENT_ID = os.environ.get('ZD_USER_SEGMENT_ID')

        if os.path.isdir(current_dir):
            for file in os.listdir(current_dir):
                if file.endswith('.html') and not any(file.startswith(name) for name in DENYLIST):
                    title = file.replace('-', ' ').replace('_', ' ').replace('.html', '').title()
                    log.info(f'*** Processing File {title} ***')
                    article_obj = create_article_obj(file, title, ZD_PERMISSION_GROUP_ID, ZD_USER_SEGMENT_ID)

                    if len(article_obj) >= 0:
                        with open('article.json', 'w') as output_files:
                            json.dump(article_obj, output_files)

                        publish_article(article_obj, title)

    except (OSError, IOError) as e:
        log.exception(f'Error: {e}')
    except Exception as exception:
        log.exception(f'Error: {exception}')


def create_article_obj(filepath, title, permission_group_id, user_segment_id):
    body_value = f"<div><iframe width=\"900\" height=\"800\" src=\"https://flywheel-io.gitlab.io/public/flywheel-tutorials/{filepath}\"></iframe></div>"

    article_dict = {"article": {
        "body": body_value,
        "locale": "en-us",
        "permission_group_id": int(permission_group_id),
        "title": title,
        "user_segment_id": int(user_segment_id)},
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
        log.exception(f'Status: {response.status_code}. Problem with the request and unable to publish {title}. Exiting.')
    else:
        # Report success
        log.info(f'Successfully created {title} on ZenDesk.')


if __name__ == "__main__":
    main()
