def count_substring(string, sub_string):
    ans = [1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)]==sub_string]
    ans= sum(ans)
    return ans
