from bs4 import BeautifulSoup

# htmlFile = "D:/Projects/GitHub/twine-parser/examples/TwineParseStory.html"

with open(htmlFile, 'r') as html:
    contents = html.read()
    soup = BeautifulSoup(contents, 'lxml')
    story = soup.find('tw-storydata')
    storyComponents = soup.find_all("tw-passagedata")
    for comp in storyComponents:
        print("Node name is " + comp['name'])  # keep
        print("Tag(s) is/are " + comp['tags'])  # keep
        # print(comp.prettify())
        # print("Dialogue choices (children) are: ")
        lines = comp.text.splitlines()
        print(lines)
        dialogue = lines[0]
        children = lines[1:]
        if len(children) > 0:
            print(children)
        else:
            children = None
            print("No children")

        # print(children)
        # print(comp.text + "\n")

# def createNode():

def parseHtml(htmlFile):
    with open(htmlFile, 'r') as html:
        contents = html.read()
        soup = BeautifulSoup(contents, 'lxml')
        storyData = soup.find('tw-storydata')
        storyComponents = soup.find_all('tw-passagedata')
        for component in storyComponents:
            print("Node name is " + component['name'])
            print("Tag is " + component['tags'])
            lines = comp.text.splitlines()
            dialogue = lines[0]
            responses = lines[1:]
            if len(responses) > 0:
                print(responses)
            else:
                responses = None
                print("No responses, end of the conversation")