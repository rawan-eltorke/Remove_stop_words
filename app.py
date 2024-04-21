import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK stopwords data
nltk.download('stopwords')
nltk.download('punkt')

# Read the contents of the text file
with open('paragraphs.txt', 'r') as file:
    text = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count word frequencies
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.most_common():
    print(f'{word}: {freq}')
