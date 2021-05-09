#Getting Started
# Import the English language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

# Process a text
doc = nlp("This is a sentence.")

# Print the document text
print(doc.text)

# Import the German language class
from spacy.lang.de import German
​
# Create the nlp object
nlp = German()
​
# Process a text (this is German for: "Kind regards!")
doc = nlp("Ich glaube dass heute ist der Europatag!")
​
# Print the document text
print(doc.text)
