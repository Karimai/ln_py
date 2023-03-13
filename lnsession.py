import time

import requests
url = 'https://unsplash.com/photos/'
photo_ids = ['KR2mdHJ5qMg', 'LBI7cgq3pbM', 'oOiWArPH5qQ', 'joQWCp70NHQ']


def get_photos():
    for photo_id in photo_ids:
        photo = requests.get(url=url+photo_id)
        print(photo.elapsed.microseconds)


def get_photos_with_session():
    for photo_id in photo_ids:
        photo = s.get(url=url+photo_id)
        print(photo.elapsed.microseconds)


if __name__ == '__main__':
    st = time.perf_counter()
    get_photos()
    ed = time.perf_counter()
    print(ed - st)
    # http request will be quicker!
    """
    In Python, the code outside of functions, classes, and other code 
    structures are executed in the global namespace. 
    So, any variables defined in the global namespace, 
    including those defined in the if __name__ == '__main__': block, 
    are considered global variables and can be accessed by any function 
    in the same module.
    """
    s = requests.Session()
    st = time.perf_counter()
    get_photos_with_session()
    ed = time.perf_counter()
    print(ed - st)
