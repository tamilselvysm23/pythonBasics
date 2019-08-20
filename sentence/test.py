def sentence_maker(text):
    question_words=("Who","Whom","Whose", "What", "When", "Where", "Which", "Why", "How")
    capitalize_text=text.capitalize()
    # print (capitalize_text)
    if capitalize_text.startswith(question_words):
        return "{}?".format(capitalize_text)
    else:
        return "{}.".format(capitalize_text)

final_output=[]
while True:
    user_input=input("Type something.....")
    if user_input == "/end":
        break
    else:
        final_output.append(sentence_maker(user_input))

print(" ".join(final_output))