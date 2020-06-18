# Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.
# For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes .
# Function Description
# Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.
# jumpingOnClouds has the following parameter(s):
#
# c: an array of binary integers
# Input Format
# The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .
# Constraints
# Output Format
# Print the minimum number of jumps needed to win the game.
#
# Sample Input 0
# 7
# 0 0 1 0 0 1 0
# Sample Output 0
# 4
# Explanation 0:
# Emma must avoid  and . She can win the game with a minimum of  jumps:


def jumpingOnClouds(c):
    double_jump, elements = 0, []

    allowed_clouds = [_ for _, i in enumerate(c) if i == 0]
    double_step__elements = [i for i in allowed_clouds[::2]]

    print('allowed_clouds:',allowed_clouds)
    print('double_step__elements:',double_step__elements)

    for i in double_step__elements:
        if i - 2 in elements:
            double_jump += 1
            elements.append(i)
        else:
            elements.append(i)



    print('double_jump', double_jump)
    print('result:',len(allowed_clouds) -1 - double_jump)

    print('allowed_clouds:', allowed_clouds)
    print('elements:', elements)

    return len(allowed_clouds) -1 - double_jump


# Test cases:
#assert jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]) == 4
#assert jumpingOnClouds([0, 0, 0, 0, 1, 0]) == 3
#assert jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1,
#                        0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]) == 28
assert jumpingOnClouds([0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1,
                        0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0,
                        0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]) == 53