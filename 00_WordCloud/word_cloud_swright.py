# UC San Diego X: Python for Data Science
# Week 2 Assignment
# Word cloud - find the most frequently occurring words in a text file
#
# I chose Walden, and On The Duty Of Civil Disobedience for my word cloud. I used Andreas Mueller's wordcloud package (http://amueller.github.io/word_cloud/)
# to generate the word cloud image.
# This code was based on OrigFiles/word_cloud.py.

import collections
from wordcloud import WordCloud

# Read in text file and stopwords file
main_text = open('C:\\Users\\sewright\\Documents\\Python for Data Science\\Assignments\\00_WordCloud\\205-0.txt', encoding = "utf8")  # Text of Walden, and On The Duty Of Civil Disobedience
stopwords = set(sw.strip() for sw in open('C:\\Users\\sewright\\Documents\\Python for Data Science\\Assignments\\00_WordCloud\\stopwords'))

# Initialize dictionary
wordcloud = {}

# Iterate through word list
# Clean the input: set all words to lowercase and split into a list
for word in main_text.read().lower().split():
	word = word.strip('.,?();:-/“!&*')  # Remove punctuation

	# Ignore stopwords
	if word not in stopwords:
		if word in wordcloud:
			wordcloud[word] += 1  # If word is in dictionary, add to its count
		else:
			wordcloud[word] = 1  # If word is not in dictionary, add it with count of 1
	
# Sort words from most to least common and extract the top 10
top_ten = collections.Counter(wordcloud).most_common(10)

for word, freq in top_ten:
	print(word, ": ", freq)
	
wc = WordCloud(background_color = "white", max_words = 1000, width = 800, height = 400).generate_from_frequencies(wordcloud)
wc.to_file('C:\\Users\\sewright\\Documents\\Python for Data Science\\Assignments\\00_WordCloud\\wordcloud.png')

