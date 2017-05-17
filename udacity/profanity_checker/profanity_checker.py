import urllib.request

def open_text():
    textf = open("sample_text.txt")
    content = textf.read()
    print(content)
    textf.close()
    check_for_shit(content)

def check_for_shit(text_to_check):
    conn = urllib.request.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = conn.read()
    print(output)
    conn.close()


open_text()
