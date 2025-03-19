import tkinter as tk
import nltk
nltk.data.path.append("C:/Vscode Projects/")
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'https://edition.cnn.com/2023/07/27/politics/takeaways-new-charges-trump-classified-documents/index.html'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')