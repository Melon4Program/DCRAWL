import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import argparse
from urllib.parse import urlparse, parse_qs

def get_gallery_id_from_url(url):
    """Extracts the gallery ID from the URL's query string."""
    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        return query_params.get('id', [None])[0]
    except Exception:
        return 'gallery'

def crawl_gallery(base_url, page_range, search_word=None):
    """
    Crawls a DCInside gallery for a given URL and page range.
    
    Args:
        base_url (str): The base URL of the gallery list.
        page_range (tuple): A tuple containing the start and end page numbers.
        search_word (str, optional): A word to filter titles by. Defaults to None.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    all_posts = []
    start_page, end_page = page_range

    for page_num in range(start_page, end_page + 1):
        # The page parameter might already be in the URL, so we handle that.
        paginated_url = f"{base_url}&page={page_num}"
        print(f"Crawling page: {paginated_url}")

        try:
            response = requests.get(paginated_url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        
        for tr in soup.select('tbody > tr'):
            try:
                num = tr.select_one('.gall_num').text.strip()
                
                if not num.isdigit():
                    continue

                title_element = tr.select_one('.gall_tit a')
                title = title_element.text.strip()

                # --- Search Word Filter ---
                if search_word and search_word not in title:
                    continue

                link = 'https://gall.dcinside.com' + title_element['href']
                author = tr.select_one('.gall_writer').text.strip()
                views = tr.select_one('.gall_count').text.strip()
                liked = tr.select_one('.gall_recommend').text.strip()

                all_posts.append({
                    'Number': num,
                    'Title': title,
                    'Author': author,
                    'Views': views,
                    'Link': link,
                    'Liked': liked
                })
            except (AttributeError, TypeError):
                continue
        
        time.sleep(1)

    if not all_posts:
        print("No valid posts found across the specified pages with the given criteria.")
        return

    gallery_id = get_gallery_id_from_url(base_url)
    df = pd.DataFrame(all_posts)
    excel_filename = f"{gallery_id}.xlsx"
    df.to_excel(excel_filename, index=False)
    print(f"Saved {len(all_posts)} posts to {excel_filename}")

def main():
    parser = argparse.ArgumentParser(description="Crawl a DCInside gallery and save posts to an Excel file.")
    parser.add_argument('-l', '--link', required=True, help="The full URL of the gallery board list. E.g., 'https://gall.dcinside.com/mgallery/board/lists/?id=record'")
    parser.add_argument('-p', '--pages', required=True, help="The range of pages to crawl. E.g., '1-5'")
    parser.add_argument('-S', '--search-word', required=False, help="An optional word to search for in post titles.")
    
    args = parser.parse_args()
    
    try:
        start_page, end_page = map(int, args.pages.split('-'))
        if start_page <= 0 or end_page < start_page:
            raise ValueError("Page range must be positive and in increasing order (e.g., 1-5).")
    except ValueError as e:
        print(f"Error: Invalid page range format. {e}")
        return

    print("Running crawler...")
    crawl_gallery(args.link, (start_page, end_page), args.search_word)

if __name__ == "__main__":
    main()