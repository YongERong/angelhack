from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
import requests
from newsapi import NewsApiClient
from gnews import GNews

load_dotenv()

GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
JIGSAW_STACK_API_KEY = os.getenv("JIGSAW_STACK_API_KEY")
NEWS_API_KEY=os.getenv("NEWS_API_KEY")

def google_search(search_term, api_key, cse_id, **kwargs):
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        print(res)
        links = [result["link"] for result in res["items"]]
        print(links)
        
    except (TimeoutError, IndexError) as e:
        print(e)
        # return error message

    return links

def google_news(search_term):
    news = GNews().get_news(search_term)
    links = [i["url"] for i in news]

    return links
    

def news_search(search_term):
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    all_articles = newsapi.get_everything(q=search_term,
                                      language='en',
                                      country="sg",
                                      sort_by='relevancy')
    articles = all_articles["articles"]
    out = [a['content'] for a in articles]

    #res = requests.get(f"https://newsapi.org/v2/all-articles?q=cpf&country=sg&apiKey={NEWS_API_KEY}")
    # articles = res["articles"]
    # out = [a['content'] for a in articles]
        
    return out


def scrape_page(links):
    out = []
    headers = {
        "Content-Type": "application/json",
        "x-api-key": JIGSAW_STACK_API_KEY,
    }
    try:
        for link in links:
            res = requests.post(
                "https://api.jigsawstack.com/v1/ai/scrape",
                headers=headers,
                json={"url": link, "element_prompts": ["text"]},
            )
            print(res)

            raw_data = res.json()
            for i in raw_data["data"]:
                out.append(i["results"][0]["text"])
            print(out)

    except(TimeoutError, IndexError, KeyError) as e:
        print(e)
        # return error message
    return out

def main():
    query = input("Input a search query.")
    search_links = google_search(query, GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_ENGINE_ID, num=2)
    data = scrape_page(search_links)
    return data

if __name__ == "__main__":
    main()
    
