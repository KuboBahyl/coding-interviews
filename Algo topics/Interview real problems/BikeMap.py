"""
- - B - -
B - - - P
- - - B -
P - - - -
- - x - -
- - - - -

B = bike
P = person
x = me

In: grid: List[Lists], position of me: List
Assumption: #B >= #P
Out: position of the best bike for me
"""


# search for all P, B = O(M*N)
# calc all dists = O(P*B) =w O(M*N/2 * M*N/2) = O(M^2*N^2)
# sort them = O(M^2*N^2*log(M^2*N^2)) = O(M^2*N^2*log(M*N))
# find the best one = O(M^2*N^2)


def find_bike(grid, my_position):
    M = len(grid)
    if M == 0:
        return

    N = len(grid[0])
    if N == 0:
        return

    # M,N > 0
    people = []
    bikes = []
    for i in range(M):
        for j in range(N):
            point = grid[i][j]
            if point == 'P':
                people.append((i, j))
            elif point == 'B':
                bikes.append((i, j))

    dists = []
    for person in people:
        for bike in bikes:
            dist = abs(person[0] - bike[0]) + abs(person[1] - bike[1])
            dists.append((person, bike, dist))

    dists.sort(key=lambda x: x[2])

    assigned = set()
    for person, bike, dist in dists:
        if person == my_position and bike not in assigned:
            return bike

        if person in assigned or bike in assigned:
            continue
        else:
            assigned.add(person)
            assigned.add(bike)


grid = [
    ['-', '-', 'P', '-'],
    ['B', 'P', '-', 'B'],
    ['B', '-', 'P', '-'],
    ['B', '-', 'B', '-'],
    ['-', 'P', '-', 'P'],
]
my_position = (4, 3)  # right down corner
# out: (2,0)

find_bike(grid, my_position)