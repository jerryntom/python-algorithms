def possibleChanges(usernames):
    answer = []
    for username in usernames:
        is_possible = "NO"
        i = 0
        j = 0

        while i < len(username):
            temp_username = list(username)
            temp_char = temp_username[i]
            temp_username[i] = temp_username[j]
            temp_username[j] = temp_char
            j += 1

            if temp_username < list(username):
                is_possible = "YES"
                answer.append("YES")
                break

            if j == len(username) - 1:
                i += 1
                j = 0

        if is_possible == "NO":
            answer.append("NO")

    return answer


print(possibleChanges(["bee", "superhero", "ace"]))
