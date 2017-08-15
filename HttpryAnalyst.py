# Made by fxt0706 @ 01.08.2017
# This moudule was made for analysising httpry .txt data, to see the data of http GET POST URL.

def read_file(file):
    global fo
    fo = open(file, "r", encoding = "ISO-8859-1")
    for i in range(1,13):
        fo.__next__()

def get_line():
    #fo.__next__()
    global line_str
    line_str = fo.readline()
    print(line_str)

def run(keywords, file):
    if(keywords == "GET"):
        print("Search GET")
        __progress(keywords)
        __output(file)
    elif(keywords == "POST"):
        print("Search POST")
    else:
        print("The keywords not supportted!")

def __progress(keywords):
    global url_list_final
    url_list = []
    done = 0
    while not done:
        get_line()
        num = line_str.find(keywords)
        if(line_str == ''):
            url_list_final = list(set(url_list))
            url_list_final.sort(key=url_list.index)
            print(url_list_final)
            done = 1
        else:
            if(num != -1):
                url_str = ""
                num = num + 4;
                while(line_str[num] != "	"):
                    url_str = url_str + line_str[num]
                    num = num + 1
                url_list.append(url_str)

def __output(file):
    output_file = open(file,'w')
    for i in url_list_final:
        output_file.write(i + '\n')
    output_file.close()


def end():
    fo.close()