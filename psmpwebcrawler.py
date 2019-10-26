import multiprocessing
import requests


def web_crawler(url):
    """child process"""
    try:
        p_name = multiprocessing.current_process().name
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as err:
        print(err)


def main():
    """parent process"""
    urls = ['http://python.org', 'http://linux.org', 'http://kernel.org', 'http://golang.org',
            'http://perllang.org']

    for url in urls:
        p = multiprocessing.Process(target=web_crawler, args=(url,))
        p.start()


if __name__ == '__main__':
    main()
