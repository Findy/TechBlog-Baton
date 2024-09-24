import requests
from bs4 import BeautifulSoup
import yaml
import re
from datetime import datetime

INPUT_FILE = '_data/external_articles.yml'
OUTPUT_FILE = '_data/articles_data.yml'

def fetch_opengraph_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; OpenGraphFetcher/1.0)'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # タイトルと画像を取得
    og_title = soup.find('meta', property='og:title')
    og_image = soup.find('meta', property='og:image')

    title = og_title['content'] if og_title and 'content' in og_title.attrs else 'No Title'
    image = og_image['content'] if og_image and 'content' in og_image.attrs else 'https://via.placeholder.com/300x200?text=No+Image'

    # 公開日を取得
    og_published = soup.find('meta', property='article:published_time') or soup.find('meta', {'itemprop': 'datePublished'})
    
    if og_published and 'content' in og_published.attrs:
        published_raw = og_published['content']
        # Unixタイムスタンプを日付に変換
        if re.match(r'^\d{10}$', published_raw):
            published = datetime.utcfromtimestamp(int(published_raw)).strftime('%Y-%m-%d')
        else:
            published = published_raw
    else:
        published = '公開日不明'

    return {
        'url': url,
        'title': title,
        'image': image,
        'published': published
    }

def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    topics_data = []

    for topic in data['topics']:
        topic_data = {
            'title': topic['title'],
            'articles': []
        }

        for article in topic['articles']:
            url = article['url']
            print(f"Fetching Open Graph data from: {url}")
            data = fetch_opengraph_data(url)
            if data:
                topic_data['articles'].append(data)
            else:
                print(f"Failed to fetch data for {url}")

        topics_data.append(topic_data)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump({'topics': topics_data}, f, allow_unicode=True)

if __name__ == "__main__":
    main()
