class Solution:

    def encode(self, strs: List[str]) -> str:
        strings = ""
        for word in strs:
            strings = strings + word + '§'
        return strings

    def decode(self, s: str) -> List[str]:
        decoded = s.split('§')
        decoded.pop()
        return decoded
