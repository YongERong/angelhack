from gtts import gTTS
import os

def ensure_audio_directory():
    """Ensure the audio directory exists."""
    if not os.path.exists('audio2'):
        os.makedirs('audio2')

def generate_audio(text, lang, accent):
    """Generate audio file from text in the specified language and accent."""
    # Mapping for language and accent to tld
    tld_map = {
        'en': {
            'uk': 'co.uk',
            'us': 'us'
        },
        'zh-CN': {
            'cn': 'com',
        },
        'zh-TW': {
            'tw': 'com'
        }
    }

    if lang in tld_map and accent in tld_map[lang]:
        tld = tld_map[lang][accent]
        filename = f"audio2/gtts_{lang}_{accent}.mp3"
        tts = gTTS(text, lang=lang, tld=tld)
        tts.save(filename)
        print(f"Audio saved as {filename}")
    else:
        raise ValueError("Invalid language or accent")

if __name__ == "__main__":
    # Ensure the audio directory exists
    ensure_audio_directory()
    
    # Example texts
    english_text = "This week, the number of people hospitalized with coronary disease has risen to about 280, and Health Minister Wang Yikang once again reminds the public to protect themselves and calls on the elderly to be vaccinated against coronary disease once a year."
    chinese_text = "本周因患冠病住院的人数上升至约280人，卫生部长王乙康再次提醒公众自我防护, 呼吁年长者应该每年接种一次冠病疫苗。"

    # Generating audio with dynamic text, language, and accent
    generate_audio(english_text, 'en', 'uk')
    generate_audio(english_text, 'en', 'us')
    generate_audio(chinese_text, 'zh-CN', 'cn')
    generate_audio(chinese_text, 'zh-TW', 'tw')
