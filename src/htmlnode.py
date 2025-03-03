
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_list = []
        for k, v in self.props.items():  # Utilisez .items() pour itérer sur un dictionnaire
            props_list.append(f' {k}="{v}"')  # Notez l'espace au début et les guillemets
        
        return "".join(props_list)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

        