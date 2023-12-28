from cssminifier import Minifier

with open("tests/media_queries.css", 'r') as fp:
    minifier = Minifier(fp.read())

    print(minifier())
    
    fp.close()