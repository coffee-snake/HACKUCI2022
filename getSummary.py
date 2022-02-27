import requests
def get_summary(api_key, user_url):
    api_site = "https://api.smmry.com"
    response = requests.get(api_site + '/&SM_API_KEY=' + api_key +'&SM_IGNORE_LENGTH'+ '&SM_URL=' + user_url )
    sm_response = response.json()
    print(sm_response)
    if('sm_api_error' in sm_response):
        return -1
    

    summary = sm_response['sm_api_content']
    return summary

if __name__ == "__main__":
    # testing an usage example
    # user_url = 'https://www.cbsnews.com/live-updates/russia-ukraine-invasion-war-donbas-kyiv-troops-today/'
    # print(get_summary(user_url))
    pass