class IntegerTriangle(object):
    def __init__(self, root=None, *args):
        self.root = root

    def maximum_path(self):
        """
        Returns the value of the maximum path of the triangle from top to bottom
        return an int
        """
        return max(n.value for n in self.queue)
        
    def minimum_path(self):
        """
        Returns the value of the minumum path of the triangle from top to bottom
        return an int
        """
        return min(n.value for n in self.queue)
        
    def add_row(self, a):
        """
        Constructs a new row at the bottom of the tree
        a is a list of ints
        """
        if not self.root:
            self.root = _Node(int(a[0]))
            self.queue = [self.root]
            return
            
        r = []
        i = 0
        lr = len(self.queue)
        l = len(a)
        assert l == lr + 1, "".join(("Length of next row must be ", str(l)))
        
        last = None
        this = None
        for this in self.queue:
            if not last:
                this.left=_Node(this.value + int(a[i]))
                r.append(this.left)
                i+=1
            else:
                this.left=last.right
                this.left.value = max(this.left.value, this.value + int(a[i-1]))
            
            this.right=_Node(this.value + int(a[i]))
            r.append(this.right)
            i+=1
            last = this
        self.queue = r
        
class _Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.value)