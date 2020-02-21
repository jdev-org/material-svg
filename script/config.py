
'''
To create forlder name as theme
'''
THEME = "round"

'''
Path to save theme and sub category folders
'''
WORKING_PATH = './svg'

'''
Get icons from github clone
https://github.com/google/material-design-icons
'''
ORIGINAL_SVG_PATH = './svg/baseline/fr/'

'''
Version
'''
VERSION = "v5"

'''
Example full url :
    https://fonts.gstatic.com/s/i/materialiconsround/airline_seat_individual_suite/v4/24px.svg?download=true
get others URl from :
    https://material.io/resources/icons/

Next we replace icons name and version into url by {} :
    https://fonts.gstatic.com/s/i/materialiconsround/{}/{}/24px.svg?download=true
'''
URL = "https://fonts.gstatic.com/s/i/materialiconsround/{}/{}/24px.svg?download=true"

'''
To use multiThread
'''
MAX_THREAD = 10

'''
Path to Write erros.json file
'''
ERRORS_PATH = WORKING_PATH + '/' + THEME + '/errors_' + VERSION +'.json'

'''
Boolean to copy not found or not to target folder
'''
COPY = False