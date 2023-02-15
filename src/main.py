import argparse
from lyrics import Lyrics
from tts import TextToSpeech


def cmdargs():
    help_msg = "Generate eminem lyrics using a LLMs"
    parser = argparse.ArgumentParser(help_msg)

    parser.add_argument("-l", "--maxlength", help = "Maximum length of lyrics to generate", type = int, default = 1)

    args = parser.parse_args()
    return args


def main():
    args = cmdargs()
    
    l = Lyrics(args.maxlength)
    lyrics = l.from_huggingartists()
    lyrics_text = lyrics[0]['generated_text']
    print(lyrics_text)

    text_to_speech = TextToSpeech()
    text_to_speech.make_request(lyrics_text)
    try:
        text_to_speech.track_request()
    except Exception as e:
        print(e)
    text_to_speech.download_audiofile()


if __name__ == "__main__":
    main()
