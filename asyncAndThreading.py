import threading
import requests
import time
import asyncio
import aiohttp

def get_urls_list(urls):
    st = time.time()
    json_list=[]
    for url in urls:
        json_list.append(requests.get(url).json())
    et = time.time()
    elapsed_time = et - st
    print(f"elapsed time is {elapsed_time}")
    return json_list

class ThreadingDowlander(threading.Thread):
    json_array = []
    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array


def get_urls_threading(urls):
    st = time.time()
    thread_list = []
    for url in urls:
        t = ThreadingDowlander(url)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
        print(t)
    et = time.time()
    elapsed_time = et - st
    print(f"elapsed time is {elapsed_time}")

async def get_data_async_as_wrapper(urls):
    st = time.time()
    json_list = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                json_list.append(await resp.json())

    et = time.time()
    elapsed_time = et - st
    print(f"elapsed time is {elapsed_time}")
    return json_list


urls = ["https://postman-echo.com/delay/3"] * 10
#get_urls_list(urls) 36.45 s
#get_urls_threading(urls)
asyncio.run(get_data_async_as_wrapper(urls))