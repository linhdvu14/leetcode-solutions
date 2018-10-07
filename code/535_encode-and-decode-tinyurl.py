# Note: This is a companion problem to the System Design problem: Design TinyURL.

# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
# and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode 
# algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be 
# decoded to the original URL.

# ----------------------------------------------
# Ideas: randomly generate 6-char key

# Considerations: 

# Complexity: time, space
# ----------------------------------------------

class Codec:
    def __init__(self):
        self.long2short = {}
        self.short2long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.long2short:
            shortUrl = 'http://tinyurl.com/' + \
                ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            if shortUrl not in self.short2long:
                self.long2short[longUrl] = shortUrl
                self.short2long[shortUrl] = longUrl
        return self.long2short[longUrl]
            
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short2long.get(shortUrl, '')
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))