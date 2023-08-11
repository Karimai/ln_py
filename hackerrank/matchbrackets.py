import csv
def isBalanced(brackets):
    openings = "([{"
    matches = {")":"(",
               "}":"{",
               "]":"["}
    inputs = []
    for bracket in brackets:
        if bracket in openings:
            inputs.append(bracket)
        else:
            if not inputs or inputs[-1] != matches[bracket]:
                return "NO"
            inputs = inputs[:-1]

    return "NO" if inputs else "YES"


def test_isBalanced():
    assert isBalanced("{[()]}") == "YES"
    assert isBalanced("{[(])}") == "NO"
    assert isBalanced("{{[[(())]]}}") == "YES"
    assert isBalanced("}][}}(}][))]") == "NO"
    assert isBalanced("[](){()}") == "YES"
    assert isBalanced("()") == "YES"
    assert isBalanced("({}([][]))[]()") == "YES"
    assert isBalanced("{)[](}]}]}))}(())(") == "NO"
    assert isBalanced("([[)") == "NO"
    with open("brackets.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            print(row)
            if isBalanced(row[0]) != row[1]:
                print(row[0])
