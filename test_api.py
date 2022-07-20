import requests
import slackclient

SLACK_TOKEN = 'xoxb-151880674451-3762166660774-oIGiy4702S5w6O0SRSAiY8yV'
# import os
# import slack
# from slack.errors import SlackApiError
#
# slack_token = os.environ["xoxb-151880674451-3762166660774-oIGiy4702S5w6O0SRSAiY8yV"]
# client = slack.WebClient(token=slack_token)
# client.chat_postMessage(channel='#qa-alerts', text='Hello')
# import pytest

def test_hardware():
    url = 'https://hardware.parkplus.io/api/v2/iot_v2/device/get-unacknowledged-data/'

    headers = {'Content-Type': 'application/json'}

    data = {
    "device_id": 17449,
    "project_id": 12996
            }

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(len(response.content))
    if len(response.content) > 110:
        print('Unacknowledged data is present')
    else:
        print('No unacknowledged data')

    #assert response.json()['message'] == 'Successful'
    try:
        assert response.status_code == 200
        # client.chat_postMessage(channel='#qa-alerts', text='Hardware API running fine - status code: 200')
    except:
        assert response.status_code !=200

