from scraping.scrape import main
from summarizer.summarise import translate, summarise
from tts.gTTS_functions import ensure_audio_directory, generate_audio
from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["POST"])
def search():
    if request.method == "POST": # if sending via post, receiving a link from user
        textInput = request.form.get("search_query")
        #language = request.form.get("language")
        
        print(textInput)
        #print(language)

        text = main(textInput)
        summary = summarise(''.join(text))
        translatedText = translate(summary, "en", "ch")

        print(summary)
        print(translatedText)

        ensure_audio_directory()

        generate_audio(summary, 'en', 'uk')
        generate_audio(summary, 'en', 'us')
        generate_audio(translatedText, 'zh-CN', 'cn')
        generate_audio(translatedText, 'zh-TW', 'tw')

        return send_file("\\audio\\gtts_en_uk.mp3", as_attachment=True)
    else: #if arrived at this page by themselves, is going to search
        return 0

if __name__ == '__main__':  
   app.run()