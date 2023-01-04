def checkAllDifferent(listChars: list[any]) -> bool:
    for i in range(0, len(listChars) - 1):
        for j in range(i + 1, len(listChars)):
            if listChars[i] == listChars[j]:
                return False
    return True