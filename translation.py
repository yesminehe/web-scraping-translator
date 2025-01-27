# -*- coding: utf-8 -*-
"""translation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WtB7H6_4RkJFGs4xni_AlX3moSPvt8kr
"""

!pip install langdetect

import os
from google.cloud import translate_v2 as translate
from langdetect import detect
import requests
from bs4 import BeautifulSoup
from google.cloud import translate_v2 as translate

# Set Google Application Credentials environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/content/bustling-tuner-425318-j8-ae77ac10f779.json'

# Example translation using Google Translate API
client = translate.Client()

# Example text to translate
text = 'Hello, how are you?'

# Translate to another language (e.g., French)
result = client.translate(text, target_language='fr')

print(f"Original: {text}")
print(f"Translated: {result['translatedText']}")

# Example function to scrape and translate content
def scrape_and_translate(url):
    # Scraping content from the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Assuming text is under certain tags like <p>
    texts = soup.find_all('p')

    translated_texts = []

    # Using Google Translate API for translation
    client = translate.Client()

    for text in texts:
        original_text = text.get_text()

        # Detect language
        language = detect(original_text)

        # Translate to English (for example)
        if language != 'en':  # Skip if already English
            translation = client.translate(original_text, target_language='en')
            translated_texts.append({
                'original_text': original_text,
                'translated_text': translation['translatedText'],
                'language': language
            })

    return translated_texts

# Example usage
url = 'https://tocodepro.com/'  # Replace with your target URL
translated_content = scrape_and_translate(url)
for item in translated_content:
    print(f"Original ({item['language']}): {item['original_text']}")
    print(f"Translated: {item['translated_text']}")
    print("---")