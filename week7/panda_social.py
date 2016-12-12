# import json
import re
import deque


class Panda:

    def __init__(self, name, mail, gender):
        if re.match(r"(\w+[.|\w])*@(\w+[.])*\w+", mail):
            self.ime = name
            self.mail = mail
            self.gender = gender
        else:
            raise TypeError("E-mail is not the corrent format")

    def getName(self):
        return self.name

    def isMale(self):
        return self.gender == 'male'

    def isFemale(self):
        return self.gender == 'female'

    def __str__(self):
        return self.mail

    def __repr__(self):
        return str(self)

    def __eq__(self, ob2):
        return self.mail == ob2.mail

    def __hash__(self):
        return hash(self.mail)


class pandaSocialNetwork:

    def __init__(self):
        self.network = {}

    def add_panda(self, panda):
        if panda in self.network:
            return
        else:
            self.network[panda] = set()

    def has_panda(self, panda):
        return panda in self.network

    def get_pandas(self):
        return list(self.network.keys())

    def make_friends(self, panda1, panda2):
        self.add_panda(panda1)
        self.add_panda(panda2)
        if not self.are_friends(panda1, panda2):
            self.network[panda2].add(panda1)
            self.network[panda1].add(panda2)
        else:
            raise AssertionError("Pandas already friends")

    def are_friends(self, panda1, panda2):
        check1 = panda1 in self.network[panda2]
        check2 = panda2 in self.network[panda1]

        if (check1 and not check2) or (check2 and not check1):
            raise AssertionError("Something's wrong with the graph")

        return check1 and check2

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.network[panda]
        else:
            return False

    def connection_level_bfs(self, start, target):
        q = deque()
        visited = set()
        # paths = {start: None}

        q.append((0, start))
        visited.add(target)

        while q:
            level, current = q.popleft()

            if current == target:
                # paths = {str(key): str(value) for key, value in paths.items}
                # print(json.dumps(path, indent=4))
                path = []
                while target is not None:
                    path.append(target)
                    target = path[target]

                return (level, reversed(path))

            for neigh in self.network[current]:
                if neigh not in visited:
                    q.append((level + 1, neigh))
                    visited.add(neigh)
        # return None



        # add direct neighbors in queue
        # next itteration next vertex visited: if it's neighbors in visited


    def connection_level(self, panda1, panda2, counter=1):
        if self.are_friends(panda1, panda2):
            return counter
        for panda in self.network[panda1]:
            return self.connection_level(panda, panda2, counter + 1)

    def how_many_gender_in_network(self, level, panda, gender, counter=0):
        if level == 1:
            counter += len([friends for friends in self.network[panda] if friends.gender == gender])
            return counter
        else:
            for friend in self.network[panda]:
                if friend.gender == "female":
                    counter += 1
                return self.how_many_gender_in_network(level - 1, friend, gender, counter)



# def bfs(graph, start):
#     visited, queue = set(), [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph[vertex] - visited)
#     return visited





