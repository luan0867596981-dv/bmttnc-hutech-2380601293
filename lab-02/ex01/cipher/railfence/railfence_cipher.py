class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, key):
        if key <= 1: return plain_text
        
        rails = [[] for _ in range(key)]
        rail_index = 0
        dictionary = 1 
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                dictionary = 1
            elif rail_index == key - 1:
                dictionary = -1
            rail_index += dictionary
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
        
    def rail_fence_decrypt(self, cipher_text, key):
        if key <= 1: return cipher_text
        
        rail_lengths = [0] * key
        rail_index = 0
        dictionary = 1
        
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                dictionary = 1
            elif rail_index == key - 1:
                dictionary = -1
            rail_index += dictionary

        # Reconstruct the rails with the cipher text
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Read the characters in the correct order to decrypt
        plain_text = []
        rail_index = 0
        dictionary = 1
        for _ in range(len(cipher_text)):
            plain_text.append(rails[rail_index].pop(0)) 
            if rail_index == 0:
                dictionary = 1
            elif rail_index == key - 1:
                dictionary = -1
            rail_index += dictionary

        return ''.join(plain_text)