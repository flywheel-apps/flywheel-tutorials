import json
import os
from .setup import *


def main():
    try:
        os.chdir('/builds/flywheel-io/public/flywheel-tutorials/public')
        current_dir = os.getcwd()
        ZD_PERMISSION_GROUP_ID = os.getenv('ZD_PERMISSION_GROUP_ID')
        ZD_USER_SEGMENT_ID = os.getenv('ZD_USER_SEGMENT_ID')

        if os.path.isdir(current_dir):
            for file in os.listdir(current_dir):
                if file.endswith('.html') and not file.startswith(('TOC', 'template')):
                    title = file.replace('_', '').title()
                    article_obj = create_article_obj(file, title, ZD_PERMISSION_GROUP_ID, ZD_USER_SEGMENT_ID)

                    if len(article_obj) >= 0:
                        with open('article.json', 'w') as output_files:
                            json.dump(article_obj, output_files)

                        publish_article('/builds/flywheel-io/public/flywheel-tutorials/public/article.json')

    except (OSError, IOError) as e:
        print(f'Error: {e}')
    except Exception as exception:
        print(f'Error: {exception}')


def create_article_obj(filepath, title, permission_group_id, user_segment_id):
    # example url-> https: // flywheel - io.gitlab.io / public / flywheel - tutorials / Flywheel - SDK - Example.html
    body_value = f"<div><iframe width=\"900\" height=\"800\" src=\"https://flywheel-io.gitlab.io/public/flywheel-tutorials/{filepath}\"></iframe></div>"

    article_dict = {"article": {
        "body": body_value,
        "locale": "en-us",
        "permission_group_id": int(permission_group_id),
        "title": title,
        "user_segment_id": int(user_segment_id)},
        "notify_subscribers": False}

    return article_dict


if __name__ == "__main__":
    main()
