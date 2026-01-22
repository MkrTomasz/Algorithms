import requests
from time import time


def fetch_pi(start, digits):
    url = "https://api.pi.delivery/v1/pi"
    params = {"start": start, "numberOfDigits": digits}
    return requests.get(url, params=params).json()["content"]


def exec_time(func):
    def wrapped():
        start = time()
        func()
        end = time()
        print(f"Execution time: {end - start}")
    return wrapped


@exec_time
def largest_run_in_pi_no_list():
    # html = "https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000"
    # pi = requests.get(html).text

    result = []
    for i in range(100):
        chunk = fetch_pi(i * 1000, 1000)
        result.append(chunk)
    pi = "".join(result)

    max_len = 0
    max_digit = None

    cur_len = 0
    prev_digit = None

    for digit in pi:
        if not digit.isdigit():
            continue

        if digit == prev_digit:
            cur_len += 1
        else:
            cur_len = 1
            prev_digit = digit

        if cur_len > max_len:
            max_len = cur_len
            max_digit = digit

    print(f"Answer no list: {max_digit * max_len}")


@exec_time
def largest_run_in_pi_list():
    # html = "https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000"
    # pi = requests.get(html).text

    result = []
    for i in range(100):
        chunk = fetch_pi(i * 1000, 1000)
        result.append(chunk)
    pi = "".join(result)

    l_temp = []
    l_max_sequence = []

    for ch in pi:
        if not ch.isdigit():
            continue

        if not l_temp:
            l_temp.append(ch)

        if ch == l_temp[0]:
            l_temp.append(ch)
        elif len(l_temp) > len(l_max_sequence):
            l_max_sequence = l_temp
        else:
            l_temp = []

    max_sequence = ''.join(l_max_sequence)

    print(f"Answer list: {max_sequence}")


largest_run_in_pi_no_list()
largest_run_in_pi_list()
