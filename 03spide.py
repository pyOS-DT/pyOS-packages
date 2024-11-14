import requests
from lxml import html

def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.content
    except requests.RequestException as e:
        print(f'Error fetching the URL: {e}')
        return None

def parse_content(content):
    tree = html.fromstring(content)

    # 提取视频
    videos = tree.xpath('//video/@src') + tree.xpath('//source/@src')
    
    # 提取文本
    texts = tree.xpath('//text()')
    texts = [text.strip() for text in texts if text.strip()]

    # 提取图片
    images = tree.xpath('//img/@src')

    # 提取链接
    links = tree.xpath('//a/@href')

    return {
        'videos': videos,
        'texts': texts,
        'images': images,
        'links': links
    }

def main():
    url = input("url:")  # 替换为您要爬取的网页
    content = fetch_content(url)
    
    if content:
        result = parse_content(content)

        print('视频:')
        for video in result['videos']:
            print(video)

        print('\n文本:')
        for text in result['texts']:
            print(text)

        print('\n图片:')
        for image in result['images']:
            print(image)

        print('\n链接:')
        for link in result['links']:
            print(link)

if __name__ == '__main__':
    main()