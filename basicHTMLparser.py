# 
# Example file for parsing and processing HTML
#

# import the HTMLParser classs that Python provides
from html.parser import HTMLParser

metacount = 0

class MyHTMLParser(HTMLParser):
  # override default implementation of handle_comment
  # that's already in the HTML parser class
  def handle_comment(self, data):
    print("Encountered comment: ", data)
    pos = self.getpos() # get position where comment was encountered
    print("\tAt line: ", pos[0], " position ", pos[1])

  # handle the start tag
  def handle_startag(self, tag, attrs):
    global metacount
    if tag == 'meta':
      metacount += 1
    print("Encountered tag: ", tag)
    pos = self.getpos() 
    print("\tAt line: ", pos[0], " position ", pos[1])

    if attrs.__len__() > 0:
      print("\tAttributes:")
      for a in attrs:
        print("\t", a[0], "=", a[1])

  # handle the end tag
  def handle_endtag(self, tag):
    print("Encountered tag: ", tag)
    pos = self.getpos() 
    print("\tAt line: ", pos[0], " position ", pos[1])

  # handle text data
  def handle_data(self, data):
    if (data.isspace()):
      print("Encountered data: ", data)
      pos = self.getpos() 
      print("\tAt line: ", pos[0], " position ", pos[1])




def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()

  # open and read the html file
  f = open("samplehtml.html")
  if f.mode == 'r':
    contents = f.read()
    # the parer reads through the passed-in html string
    # line by line
    parser.feed(contents)

    # to test the parser, we'll read from a sample HTML file
    # # but usually we'd use URL lib to open up a URL 
    # and read the HTML data straight from the web


if __name__ == "__main__":
  main()
  