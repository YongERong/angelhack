from scraping.scrape import main
from summarizer.summarise import translate, summarise
from tts.gTTS_functions import ensure_audio_directory, generate_audio
from flask import Flask, render_template, request, send_file, make_response
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
CORS(app)

@app.route("/", methods=["GET"])
@cross_origin()
def search():
 # if sending via post, receiving a link from user
    textInput = request.args.get("search_query")
    #language = request.args.get("language")
    
    print(textInput)
    #print(language)

   #  text = main(textInput)
   #  summary = summarise(''.join(text))
   #  translatedText = translate(summary, "en", "ch")

   #  print(summary)
   #  print(translatedText)

   #  ensure_audio_directory()

   #  generate_audio(summary, 'en', 'uk')
   #  generate_audio(summary, 'en', 'us')
   #  generate_audio(translatedText, 'zh-CN', 'cn')
   #  generate_audio(translatedText, 'zh-TW', 'tw')
   #  print("HELLO")
   #  response = )
   #  response.headers["Access-Control-Allow-Origin"]="*"
    return send_file("audio2/gtts_en_uk.mp3", mimetype="audio/mp3")

if __name__ == '__main__':  
   app.run()