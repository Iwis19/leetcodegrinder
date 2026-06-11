class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        """
        never in a million years could i have thought of this solution. 
        i will definitely make sure to come back to this.

        the idea of this solution is that i use positive and negative 1s to keep track of if this happened in the guess word or the secret word.
        when freq[n] < 0, i know theres unmatched chars from guess, and when freq[n] > 0, its unmatched chars from secret
        
        some counter intuitive things from earlier:
        
        - why do i scan for both? wouldnt it make me have double? -> no, because a new guess char could match to an unmatched secret char, and the new secret char could match with an unmatched guess char

        - why am i working on scanning on both? -> because i need this to not be outdated on one or the other words.

        3 ms runtime beats 90%
        """

        freq = [0] * 10
        bull, cow = 0, 0

        for i in range(len(secret)):

            s, g = int(secret[i]), int(guess[i])
            if s == g:
                bull += 1
                continue

            # oppositely correlated so if freq[g] is gonna be positive for a match, that means freq[s] += 1 when s is seen, and vice versa
            if freq[g] > 0: cow += 1
            if freq[s] < 0: cow += 1

            """
            we update these values after because or else it might wipe previous information. 

            e.g. freq[s] just increased this spot to 1 last loop, and this loop i update freq[g] -= 1 before i take a loop at freq, wiping out this spot
            """ 
            freq[s] += 1
            freq[g] -= 1
            

        
        return f"{bull}A{cow}B"
