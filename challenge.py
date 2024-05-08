import json
import logging
import sys
from lib.Process import Process

logger = logging.getLogger('name')

try:
    with open('jsons/users.json', 'r') as users_file:
        users_data = json.load(users_file)

    with open('jsons/companies.json', 'r') as companies_file:
        companies_data = json.load(companies_file)

except Exception as e:
    logger.error(f'Failed to upload file: {e}')
    sys.exit('Gracefully exiting...')

output = Process().start(users_data, companies_data)

try:
    with open("output.txt", "w") as result_file:
        result_file.write(output)
except Exception as e:
    logger.error(f'Failed: {e}')
    sys.exit('Gracefully exiting...')
