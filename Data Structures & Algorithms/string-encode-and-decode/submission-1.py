class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            length = len(s)
            encoded_string += str(length) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        j = i
        while i < len(s):
            while s[j] != '#':
                j += 1

            length =int(s[i:j])
            word = s[j + 1:length + j +1]
            decoded_strs.append(word)

            i = length + j +1 
            j = i


        return decoded_strs

