# Decorator give detiails about funciton to python
# They are not compulsory

# non - staic
class Wordset:
    def __init__(self):
        self.words = set()
    def word(self,sen):
        #text = (self.clean(sen)) # self is used because it will search for fun. within the class
        text = Wordset.clean(sen) #can also work when usig static method instead
        for item in text.split():
            self.words.add(item)
        return self.words
    #non - static method
    #def clean(self,sen):
    #    text = sen.replace('!'," ").replace(','," ").replace("?"," ").replace("."," ")
    #    return text
    
    # static method
    # same for all instances of class
    def clean(sen):
        text = sen.replace('!'," ").replace(','," ").replace("?"," ").replace("."," ")
        return text
    
set1 = Wordset().word("My name is Nikhil. I? hello,dhi")
set2 = Wordset().word("I am form Uttarakhand,India 2005")
print(set1)
print(set2)

# static 
class Wordset:
    replacePun = ['!',"?",".",","]
    def __init__(self):
        self.words = set()
    def addText(self,sen):
        text = Wordset.clean(sen)
        for item in text.split():
            self.words.add(item)
        return self.words

    @staticmethod # called - decorator not compulsory
    def clean(sen):
        text = sen
        for punc in Wordset.replacePun:
            text = sen.replace(punc,"")
        return text.lower()

wordSet1 = Wordset().addText("This is a, static methods")
wordSet2 = Wordset().addText("wonder missioan! new. world one? piece")
print(wordSet1)
print(wordSet2)
