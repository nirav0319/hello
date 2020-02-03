import urllib.parse as parse
import re
import json

def normalize_encode_search_query(search_query):
    """Handle what happens to the string entered by a user on the search box.

    Essentially lower, strip, remove multiple spaces, parse url using urllib ("C++ jobs in pune! !  " -> c%2B%2B%20jobs%20in%20pune%21%20%21)
    This gets us a google search style query string we can decode later


    Parameters:
    search_query (str)

    Returns:
    encoded_normalized_search_query (str) 

    """

    normalized_search_query = re.sub(' +', ' ', str(search_query).lower().strip())
    encoded_normalized_search_query = parse.quote_plus(normalized_search_query)

    return encoded_normalized_search_query

def decode_search_query(encoded_search_query):
    """Handle how to decode the search query given in a url 
    (eg: tildehat.com/job_search/?q=hey%20man -> this converts hey%20man to "hey man" to be used downstream for search/indexing/ranking)


    Parameters:
    encoded_search_query (str)

    Returns:
    decoded_search_query (str) 

    """

    decoded_search_query = parse.unquote_plus(encoded_search_query)

    return decoded_search_query


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)  
    return d

# sql connections here