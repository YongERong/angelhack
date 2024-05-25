from scraping.scrape import main
from summarizer.summarise import translate, summarise
from tts.gTTS_functions import ensure_audio_directory, generate_audio

text = main()
summary = summarise(''.join(text))
translatedText = translate(summary, "en", "ch")

print(summary)
print(translatedText)

ensure_audio_directory()

generate_audio(summary, 'en', 'uk')
generate_audio(summary, 'en', 'us')
generate_audio(translatedText, 'zh-CN', 'cn')
generate_audio(translatedText, 'zh-TW', 'tw')