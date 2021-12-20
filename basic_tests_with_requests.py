import requests

ENDPOINT = "http://suggestqueries.google.com/complete/search"
payload_goo = {
    'client': 'chrome',
    'q': 'goo',
    'hl': 'en'
}

payload_selenium = {
    'client': 'chrome',
    'q': 'selenium  ',
    'hl': 'en'
}

EXCLUDE_LIST = ['testing', 'test', 'selenium', 'interview', 'download', 'tutorial', 'maven', 'dependency', 'seleniumhq', 'ide', 'questions', 'java', 'python', 'webdriver', 'qa']

def google_test_for_partial_keyword_goo_with_api():
    response = requests.get(url=ENDPOINT, params=payload_goo)
    print(response.status_code)
    output = response.json()
    required_output = output[1]
    print(required_output)

    for i in required_output:  # omitting last item as it is ''
        if 'google' not in i.lower():
            print(f"the search item {i} may not belong to google and is at list index position of {required_output.index(i)}")
    else: print("All search items relate to Google")



google_test_for_partial_keyword_goo_with_api()
