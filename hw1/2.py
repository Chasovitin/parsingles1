#Use the API provided by the BTC Mining Pool to obtain the mining pool operation status and user account information in real time.

#API Structure
#The call path is as follows:

#https://${Endpoint}/${Version}/${Path}

#among them:

#Endpoint: pool.api.btc.com

#Version: v1

#Path: Specific API path, see definition below.

#Authentication
#Calling the user-related interface requires that the querystring provide access_key and puid authentication.     * AccessKey is the user identity credentials, corresponding to an account. Please keep your own AccessKey.     * puid is the mine pool sub-account id used to distinguish multiple sub-accounts under an account.
#AccessKey and puid can be logged in to pool.btc.com and accessed from the subaccount management page.
#response
#All response types are application/json, as follows:

#{
   #   "err_msg": null
#}
#The data, err_no, and ʻerr_msg` fields in the response body are fixed fields and have the following meanings:

#data, the specific API response data.
#error_no, error code, 0 is normal, non0 is wrong, check the error_msg field specifically.
#error_msg, error message for debugging use. If there are no errors, this field does not appear.

# ShzCA5eyJJSJ1V0gbAJ2tXDefZU0SLmY25tgBbul

import requests
nickname = input( 'User Nickname:')
main_link = f'https://pool.api.btc.com/v1/$ShzCA5eyJJSJ1V0gbAJ2tXDefZU0SLmY25tgBbul'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36' ,
            'Accept':'*/*'}
response = requests.get(main_link, headers=headers)
user_data = response.json()

repos_link = user_data['repos_url']
response=requests.get(repos_link,headers=headers)
repos_data=response.text
file_name = f'{nickname}_repose.jason'

with open(file_name, 'w') as f:
    f.write(repos_data)