import pysrt

subs = pysrt.open('/Users/mac/Documents/Git/subtitle_vectorizer/babylon.berlin.(2017).tv.s01.ger.9cd/episode 1/Babylon Berlin S01E01 Episode 1 1080p Netflix WEB-DL DD5.1 x264-TrollHD_deu.srt')
# If you get a UnicodeDecodeError try to specify the encoding
# subs = pysrt.open('some/file.srt', encoding='iso-8859-1')

import spacy



subs_texts = [line.text for line in subs]

nlp = spacy.load('de')

for line in subs_texts:
    doc = nlp(line)
    for token in doc:
        print(token.text, token.pos_, token.dep_)

print(subs)