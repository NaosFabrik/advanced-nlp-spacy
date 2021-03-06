#Selective processing
import spacy
​
nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)
​
# Only tokenize the text
doc = nlp(text)
print([token.text for token in doc])

#Part2
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)
​
# Disable the tagger and parser
with ____.____(____):
    # Process the text
    doc = ____
    # Print the entities in the doc
    print(____)
Run code