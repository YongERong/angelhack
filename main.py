from scraping.scrape import main
from summarizer.summarise import translate, summarise

text = main()
summary = summarise(''.join(text))

print(text)