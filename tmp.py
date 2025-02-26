import re


def execute(code):
    patterns = {}

    # Step 3: Extract and store pattern definitions
    pattern_def_regex = r"p(\d+)(.*?)q"
    matches = re.findall(pattern_def_regex, code, re.DOTALL)
    for match in matches:
        identifier = int(match[0])
        pattern_code = match[1]
        patterns[identifier] = pattern_code

    # Step 5: Remove pattern definitions from code
    code = re.sub(pattern_def_regex, '', code)

    # Step 6: Process pattern invocations
    def processPattern(pattern_id):
        if pattern_id not in patterns:
            raise Exception(f"Undefined pattern: P{pattern_id}")

        pattern_code = patterns[pattern_id]

        # Step 9: Replace pattern invocations in the pattern code
        pattern_code = re.sub(r"P(\d+)", lambda m: processPattern(int(m.group(1))), pattern_code)

        return pattern_code

    # Step 11: Replace pattern invocations in the code
    code = re.sub(r"P(\d+)", lambda m: processPattern(int(m.group(1))), code)

    return code
