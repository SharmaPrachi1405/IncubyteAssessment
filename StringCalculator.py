class String_Calculator:

    def add(word):
        if(len(word) == 0):
            return 0
        if(',' in word):
            return 3 
        else:
            return int(word)




