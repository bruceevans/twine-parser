# custom tree class to link dialogue and responses

class StoryNode():
    """ Base class for a dialogue node
    """
    def __init__(self, dialogue, parent, children = None, flag = None):
        """ Init with the dialogue, connections, and whether to set a bool
            args:
                dialogue (str): Dialogue said/read on screen
                parent (StoryNode): Parent story node, previous dialogue
                children (StoryNode[]): List of dialogue options to select, can be None
                flag (tuple (str, bool)): Tuple containing the name of the flag and a bool value, can be None
        """
        self.dialogue = dialogue
        self.parent = parent
        self.children = children
        self.flag = flag
