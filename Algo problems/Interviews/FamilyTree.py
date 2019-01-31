# Create a structure for monarchy hierarchy (parents and children)
# Add methods birth() = add member, death() = mark member as dead, and order() - print alive members

# Logic: Tree DS with the family founder in root

class Person(object):
    def __init__(self, name, children=[], is_alive=True):
        self.name = name
        self.children = children or []
        self.is_alive = is_alive


class Monarchy(object):
    def __init__(self, king):
        self.root = king

    def birth(self, child_name, parent_name):
        parent = self.search_person(parent_name)
        child_new = Person(child_name)
        parent.children.append(child_new)

    def death(self, name):
        person_dead = self.search_person(name)
        person_dead.is_alive = False

    def order(self):
        # DFS
        def search_alive_children(person, alive_members):
            for child in person.children:
                if child.is_alive:
                    alive_members.append(child.name)
                alive_members = search_alive_children(child, alive_members)

            return alive_members

        alive_members = []
        if self.root.is_alive:
            alive_members.append(self.root.name)

        return search_alive_children(self.root, alive_members)

    def search_person(self, name):
        def search_rec(name, person):
            # DFS
            for child in person.children:
                if child.name == name:
                    return child

                found = search_rec(name, child)
                if found:
                    return found

            return False

        if self.root.name == name:
            return self.root

        return search_rec(name, self.root)


king = Person(name='King', children=[Person('Charles'), Person('Harry')])
king.children[0].children = [Person('Jack'), Person('Jones')]
king.children[1].children = [Person('Armani'), Person('Versace')]

"""
King -> Charles -> Jack
                -> Jones
     -> Harry   -> Armani
                -> Versace
"""

family = Monarchy(king)
family.birth(child_name='Gucci', parent_name='Versace')
family.birth(child_name='Sheldon', parent_name='King')
family.death('Jones')
family.death('King')
"""
King* -> Charles -> Jack
                 -> Jones*
      -> Harry   -> Armani
                 -> Versace -> Gucci
      -> Sheldon
"""
family.order()