def add_sign_top():
    return "|￣￣￣￣￣￣ |"

def add_bunny():
    return "| ＿＿＿＿＿__|\n(\__/) ||\n(•ㅅ•) ||\n/ 　 づ\n"

def separate_words(sentence):
    words = " ".split(sentence)
    for word in words:
        # arbitrary for now
        if len(word) > 10:
            print(word, "is too long a word! Please use shorter words.")
            return EOFError
    return words

def separate_lines(words):
    # words should be a list of words, not a string
    lines = []
    # counts words for the for loop
    wordcount = len(words)
    # arbitrary
    line_length = 12
    for i in range(0, wordcount):
        words.pop(words[i])
        lines[i] += str( words[i] )
        line_length = len(lines[i])
        charcount = len(lines[i])
        # needs to try to add the next word only if the result will not make the line too long
        if charcount >= line_length:
            charcount = 0
        

def make_lines(words):
    line = ""