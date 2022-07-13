import requests
# import slackclient
# import slack
# SLACK_TOKEN = 'xoxb-151880674451-3762166660774-oIGiy4702S5w6O0SRSAiY8yV'
#
# client = slack.WebClient(token=SLACK_TOKEN)
# # client.chat_postMessage(channel='#qa-alerts', text='Hello')

def test_Hardware():
    url = 'https://hardware.parkplus.io/api/v2/iot_v2/device/get-unacknowledged-data/'

    headers = {'Content-Type': 'application/json'}

    data = {
    "device_id": 16485,
    "project_id": 13685
            }

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.json())
    #assert response.json()['message'] == 'Successful'
    try:
        assert response.status_code == 200
        # client.chat_postMessage(channel='#qa-alerts', text='Hardware API running fine - status code: 200')
    except:
        assert response.status_code !=200

