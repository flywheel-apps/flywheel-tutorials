import json
import requests
import os 

# Set the target Zendesk subdomain (subdomain.zendesk.com)
subdomain = 'flywheelio'

try:
	ZD_USER = os.getenv('ZD_USER')
	ZD_API_TOKEN = os.getenv('ZD_TOKEN')
	ZD_SECTION_ID = os.getenv('ZD_SECTION_ID')
except Exception as e:
	print(f'Error: {e}')

# Set the request parameters
apiEndPoint = '/api/v2/help_center/sections/' + ZD_SECTION_ID 
url = 'https://' + subdomain + '.zendesk.com' + apiEndPoint + '/articles'

def publish_article(json_file_path):

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
	    print('Status:', response.status_code, 'Problem with the request. Exiting.')
	    exit()
	else:

		# Report success
		print('Successfully created the article.')