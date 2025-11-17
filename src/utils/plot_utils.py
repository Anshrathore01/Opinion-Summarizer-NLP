import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

def plot_wordcloud(texts, max_words=100):
    text = " ".join(texts)
    wc = WordCloud(width=800, height=400, background_color="white", max_words=max_words)
    wc.generate(text)
    plt.figure(figsize=(12,6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    return plt
