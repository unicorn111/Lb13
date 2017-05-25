from arraystack import *


st = ArrayStack()

def brackets_checker(s):
    try:
        if st.isEmpty() == True:
            for i in s:
                if i == "(":
                    st.push(")")
                elif i == "[":
                    st.push("]")
                elif i == "{":
                    st.push("}")
                elif i == ")" or i == "]" or i == "}":
                    if st.peek() == i:
                        st.pop()
        if st.isEmpty() == True:
            return True
        else:
            return False
    except KeyError:
        return False
