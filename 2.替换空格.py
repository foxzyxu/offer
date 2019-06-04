def replaceSpace(string):
    return string.replace(' ','%20')

if __name__ == '__main__':
    string = 'hallo world!'
    print(replaceSpace(string))