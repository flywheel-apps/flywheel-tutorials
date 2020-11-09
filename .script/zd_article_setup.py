import json
import os
import requests
import logging

from pathlib import Path

DENY_LIST = ['index', 'template', 'TOC']
BASE_PATH = Path('/builds/flywheel-io/public/flywheel-tutorials/')
SUBDOMAIN = 'flywheelio'


try:
    ZD_USER = os.environ.get('ZD_USER')
    ZD_API_TOKEN = os.environ.get('ZD_TOKEN')
    ZD_SECTION_ID = os.environ.get('ZD_SECTION_ID')
    ZD_PERMISSION_GROUP_ID = os.environ.get('ZD_PERMISSION_GROUP_ID')

except Exception as e:
    log.exception(f'Error: {e}')


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%y %H:%M:%S')
log = logging.getLogger('root')

def main():
    # Current notebook in repo
    current_notebook = get_all_current_notebooks()

    # Get article in Zendesk
    data, errors = get_all_current_articles()

    zd_articles_w_id = dict()

    # If there is no error message
    if errors is None:
        # If there is at least one article in Zendesk
        if data['count'] > 0 :
            for article in data['articles']:
                # key: article name; value: article id
                zd_articles_w_id[article['name']] = article['id']

            # Check if there is any new notebook being added to the gitlab repo
            new_notebook = set(current_notebook.keys())-set(zd_articles_w_id.keys())

            # If there is new notebook, publish the notebook into ZenDesk
            if len(list(new_notebook)) > 0:
                for notebook_title in list(new_notebook):
                    proccess_notebook(notebook_title, current_notebook[notebook_title])

            # Update existing notebook in ZenDesk
            for article_name, article_id in zd_articles_w_id.items():
                update_existing_notebook(str(article_id), current_notebook[article_name])



        # if there is no article in Zendesk yet, add notebook to Zendesk
        else:
            for notebook_title, filename in current_notebook.items():
                proccess_notebook(notebook_title, filename)

    else:
        log.error('Error occurred when getting data from Zendesk.')
        


def update_existing_notebook(article_id, filename):

    apiEndPoint = '/api/v2/help_center/articles/'+article_id+'/translations/en-us.json'

    url = 'https://' + SUBDOMAIN + '.zendesk.com' + apiEndPoint 

    headers = {'Content-Type': 'application/json',}

    body_value = f"<div><iframe width=\"900\" height=\"800\" src=\"https://flywheel-io.gitlab.io/public/flywheel-tutorials/{filename}\"></iframe></div>"

    data = '{"translation": {"body": ' +'\"'+ body_value + '\"'+'}}'

    payload = json.dumps(data)

    response = requests.put(url, headers=headers, data=payload, auth=(ZD_USER, ZD_API_TOKEN))

    # Check for HTTP codes other than 201 (Created)
    if response.status_code != 200:
        log.exception(
            f'Status: {response.status_code}. Problem with the request and unable to update {filename}. Exiting.')
    else:
        # Report success
        log.info(f'Successfully updated {filename} on ZenDesk.')

def proccess_notebook(notebook_title, filename):

    log.info(f'*** Processing File {notebook_title} ***')
    article_obj = create_article_obj(filename, notebook_title)

    try:
        if len(article_obj) > 0 :
            public_dir = BASE_PATH / 'public'
            with open('article.json', 'w') as output_files:
                json.dump(article_obj, output_files)
            article_json_path = public_dir / 'article.json'
            publish_article(article_json_path, notebook_title)
    except Exception as e:
        log.exception(f'Error occurred. {e}')



def get_all_current_notebooks():

    try:
        public_dir = BASE_PATH / 'public'
        os.chdir(public_dir)
        current_dir = os.getcwd()

        # key: article name; value: file name
        current_notebook = dict()

        if os.path.isdir(current_dir):
            for file in os.listdir(current_dir):
                if file.endswith('.html') and not any(file.startswith(name) for name in DENY_LIST):
                    title = file.replace('-', ' ').replace('_', ' ').replace('.html', '').title()
                    current_notebook[title] = file
                    

    except (OSError, IOError) as e:
        log.exception(f'Error: {e}')
    except Exception as exception:
        log.exception(f'Error: {exception}')

    return current_notebook

def create_article_obj(filepath, title, permission_group_id=ZD_PERMISSION_GROUP_ID):
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


    # Set the request parameters
    apiEndPoint = '/api/v2/help_center/sections/' + ZD_SECTION_ID
    url = 'https://' + SUBDOMAIN + '.zendesk.com' + apiEndPoint + '/articles'

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

def get_all_current_articles():

    try:
        # Set the request parameters
        apiEndPoint = '/api/v2/help_center/sections/' + ZD_SECTION_ID
        url = 'https://' + SUBDOMAIN + '.zendesk.com' + apiEndPoint + '/articles.json'

        response = requests.get(url)

        response.raise_for_status()  
        data = response.json()
        return data, None
    except Exception as e:
        log.exception(f'Error occurred. More detail: {e}')
        log.exception(f'Error Message from request: {response.text}')
        return None, e

    



if __name__ == "__main__":
    main()
