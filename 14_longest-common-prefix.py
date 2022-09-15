def longestCommonPrefix(strs: list[str]) -> str:
    result = ""
    if len(strs) == 1:
        result = strs[0]
        return result
    for i in range(0, len(strs[0])):
        char = strs[0][i]
        for word in strs:
            if word == "":
                return ""
            if len(word) <= i or char != word[i]:
                return result
        result += char
    return result


if __name__ == "__main__":
    print(longestCommonPrefix(["flower", "flow", "flight"]))
