'''
    Generate all valid IPs given a string of numbers. 
'''
def generate_ip_addresses(s):
    def backtrack(remaining, segments, curr_ip):
        # Base case: If we have found 4 valid segments and used up all characters, add the IP address to the result
        if segments == 4 and not remaining:
            result.append(curr_ip[:-1])  # Remove the trailing dot
            return

        # Base case: If we have used up all characters but haven't found 4 segments yet
        if not remaining or segments == 4:
            return

        # Recursive case: Try all possible segment lengths (1, 2, or 3)
        for i in range(1, min(4, len(remaining) + 1)):
            segment = remaining[:i]

            # Ignore segments with leading zeros (except for zero itself)
            if segment[0] == '0' and len(segment) > 1:
                continue

            # Ignore segments larger than 255
            if int(segment) > 255:
                continue

            # Recursive call with updated parameters
            backtrack(remaining[i:], segments + 1, curr_ip + segment + '.')

    result = []
    backtrack(s, 0, "")
    return result

# run
input_str = "25601690"
ip_addresses = generate_ip_addresses(input_str)
for ip in ip_addresses:
    print(ip)
