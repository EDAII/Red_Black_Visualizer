RED = True
BLACK = False

class Node:
    def __init__(self, key):
        self.key = key
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:

    def rotate_left(self, root, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x

        y.parent = x.parent
        if not x.parent:
            root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y
        return root

    def rotate_right(self, root, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x

        y.parent = x.parent
        if not x.parent:
            root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
        return root

    # ---------- INSERTION ----------
    def insert_fix(self, root, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u and u.color == RED:
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        root = self.rotate_left(root, k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    root = self.rotate_right(root, k.parent.parent)
            else:
                u = k.parent.parent.left
                if u and u.color == RED:
                    k.parent.color = BLACK
                    u.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        root = self.rotate_right(root, k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    root = self.rotate_left(root, k.parent.parent)
        root.color = BLACK
        return root

    def insert(self, root, key):
        new_node = Node(key)
        y = None
        x = root

        while x:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if not y:
            root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        return self.insert_fix(root, new_node)

    def _min(self, x):
        while x.left:
            x = x.left
        return x

    def delete_fix(self, root, x):
        while x != root and (not x or x.color == BLACK):
            if x == x.parent.left:
                s = x.parent.right
                if s and s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    root = self.rotate_left(root, x.parent)
                    s = x.parent.right
                if (not s.left or s.left.color == BLACK) and (not s.right or s.right.color == BLACK):
                    s.color = RED
                    x = x.parent
                else:
                    if not s.right or s.right.color == BLACK:
                        if s.left:
                            s.left.color = BLACK
                        s.color = RED
                        root = self.rotate_right(root, s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    if s.right:
                        s.right.color = BLACK
                    root = self.rotate_left(root, x.parent)
                    x = root
            else:
                s = x.parent.left
                if s and s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    root = self.rotate_right(root, x.parent)
                    s = x.parent.left
                if (not s.right or s.right.color == BLACK) and (not s.left or s.left.color == BLACK):
                    s.color = RED
                    x = x.parent
                else:
                    if not s.left or s.left.color == BLACK:
                        if s.right:
                            s.right.color = BLACK
                        s.color = RED
                        root = self.rotate_left(root, s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    if s.left:
                        s.left.color = BLACK
                    root = self.rotate_right(root, x.parent)
                    x = root
        if x:
            x.color = BLACK
        return root

    def delete(self, root, key):
        z = root
        while z:
            if key == z.key:
                break
            elif key < z.key:
                z = z.left
            else:
                z = z.right
        if not z:
            return root

        y = z
        y_original_color = y.color
        if not z.left:
            x = z.right
            self._replace(root, z, z.right)
        elif not z.right:
            x = z.left
            self._replace(root, z, z.left)
        else:
            y = self._min(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                if x:
                    x.parent = y
            else:
                self._replace(root, y, y.right)
                y.right = z.right
                y.right.parent = y
            self._replace(root, z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == BLACK:
            root = self.delete_fix(root, x)

        return root

    def _replace(self, root, u, v):
        if not u.parent:
            root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent
        return root
