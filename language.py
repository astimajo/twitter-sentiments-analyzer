from textblob import TextBlob

blob = TextBlob("ito ay naka sulat sa wikang tagalog")
print(blob.detect_language())

#translation
print(blob.translate(to="en"))