from deep_translator import GoogleTranslator as google
word = 'Блять'
print (google(source='english', target='uk').translate(word))