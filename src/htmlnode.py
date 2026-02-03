# HDRM Node Definition

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not yet implemented")
    
    def props_to_html(self):
        props_out = ""
        for prop in self.props:
            props_out += f" {prop}={self.props[prop]}"
        return props_out
            
    def __eq__(self,other):
        if not isinstance(other,HTMLNode):
            return False
        
        return(
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
    


    def __repr__(self):
        html_rep = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return html_rep





class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        prop_string = self.props_to_html()
        return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        leaf_rep = f"LeafNode({self.tag}, {self.value}, {self.props})"
        return leaf_rep


class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be none.")
        
        if self.children is None:
            raise ValueError("Child nodes cannot be none.")
        
        if len(self.children) == 0:
            raise ValueError("child nodes cannot be empty list")
        
        child_html_string = ""
        for child in self.children:
            child_html_string += child.to_html()
        
        if self.props:
            prop_string = self.props_to_html()
            return f"<{self.tag}{prop_string}>{child_html_string}</{self.tag}>"

        return f"<{self.tag}>{child_html_string}</{self.tag}>"

    def __repr__(self):
        parent_rep = f"ParentNode({self.tag}, {self.children}, {self.props})"
        return leaf_parent_reprep