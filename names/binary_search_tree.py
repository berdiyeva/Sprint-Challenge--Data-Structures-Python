class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # if the value is less than self.value then will go to the left, otherwise will go to the right
    def insert(self, value):
        if value < self.value:
            # if the left side has a node insert the value
            if self.left:
                self.left.insert(value)
            # if not create one
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        # if the root value is less than the target
        # check to right of tree
        if self.value < target:
            if self.right is None:
                return False
            return self.right.contains(target)
        # if the root value is greater than the target
        # check to the left of the true
        else:
            if self.left is None:
                return False
            return self.left.contains(target)
