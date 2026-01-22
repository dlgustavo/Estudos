import re

texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you"
clean_text = re.sub(',|:|.', '', texto)
selected_words = []
python_word = ['p', 'y', 't', 'h', 'o', 'n']

for word in clean_text.split(' '):
    if word[0].lower() in python_word \
        or word[-1].lower() in python_word:
            selected_words.append(word)

print(len(selected_words))