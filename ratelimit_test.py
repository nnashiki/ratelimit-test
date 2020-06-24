import requests
from ratelimit import limits, sleep_and_retry

ONE_MINUTES = 60

# 1分間に10回だけAPIをたたく
@sleep_and_retry
@limits(calls=10, period=ONE_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response


if __name__ == '__main__':

    for i in range(100):
        call_api("http://localhost:3000/profile")
