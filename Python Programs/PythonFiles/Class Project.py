fileToRead = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\CROSSWD.TXT')
for word in fileToRead:
      print (word.strip())
fileToRead.close()


##fileToRead = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\CROSSWD.TXT')
####for word in fileToRead:
####    if 'a' in word[0] and 'c' in word[1]:
####        print(word.strip())
####fileToRead.close()
##
####fileToRead = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\CROSSWD.TXT')
####counter = 0
####for word in fileToRead:
####    if 'a' in word[0] and 'c' in word[1] and 'q' in word[2]:
####        counter += 1
####print("Number of words with acq in the beginning:", counter)
####fileToRead.close()
##
##fileToRead = open('C:\\Users\\Alexander\\Desktop\\Python Programs\\PythonFiles\\CROSSWD.TXT')
##for word in fileToRead:
##    if len(word) > 20:
##        print(word.strip())
##fileToRead.close()
