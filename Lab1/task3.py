"""
Objectives:
- Lists
- Dict
- constructs: loops, conditionals
- more work with files
- functions
"""


# function #1

  #  Returns the number of lines in a file given as parameter.
  #  @param filename: the file's name


def no_lines(file_name):
    f = open(file_name, 'r')
    content = f.read()
    return content.count("\n")


# function #2

#    Reads the content of a file and fills the given list with the sentences
#   found in the file
#    @param filename: the file's name
# @param sentences: the list that will be contain the sentences


def fill(file_name, sentences):
    f = open(file_name, 'r')
    content = f.read()    
    sentences.extend(content.split(". "))
    return sentences


# function #3

#    Return a list of the top N most used words in a given file
#    @param filename: the file's name
#    @param n: the number of words in the top, default is 5

#bonus 1p: implement your own sort method instead of using an existing one
def most_used_words(filename, n=5):
    f = open("fisier_input", 'r')
    content = f.read()  
    dictionar = {}  
    
    words = content.split()

    for word in words:
        if word in dictionar:
            dictionar[word] += 1
        else:
            dictionar[word] = 1

    return sorted(dictionar, key=dictionar.get, reverse=True)[:n]



if __name__ == "__main__":

    filename = "fisier_input"


    #  test the functions

    print no_lines(filename)

    

    #  print all the sentences with less than 15 words

    propoziti = []
    fill(filename, propoziti)

    for prop in propoziti:
        aux = prop.split()
        if len(aux) < 15:
            print prop

    #  write the most used words in a file, one per line

    lista = most_used_words(filename, 4)
    out = open('out', 'w')
    for cuv in lista:
        out.write("%s\n" % cuv) 