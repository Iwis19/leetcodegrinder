class Solution:
    def simplifyPath(self, path: str) -> str:

        """
        mostly my own implementation :)

        debugged on my own, needed a small nudge from description and look at topic, but no chatgpt used besides asking how mutating arr goes in a for loop

        0 ms runtime beats 100%
        """
        
        full_path = [directory for directory in path.split("/") if directory]

        if not full_path: 
            return "/"

        ans = []

        for i, path in enumerate(full_path):

            ans.append(path)

            # if .. -> remove end and previous (if it exists)
            if path == "..":
                ans.pop(-1)
                if ans:
                    ans.pop(-1)

            # if . -> remove end
            elif path == ".":
                ans.pop(-1)

            # else -> nothing

        return "/" + "/".join(ans)

        
