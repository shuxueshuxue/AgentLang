import ast

class AgentLangTranspiler(ast.NodeTransformer):
    def __init__(self):
        self.semantic_vars = set()  # Track vars from agent calls

    def visit_Assign(self, node):
        # Track: var = agent_call(...)
        if isinstance(node.value, ast.Call):
            if isinstance(node.value.func, ast.Name):
                # Assume any function call returns semantic text
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        self.semantic_vars.add(target.id)
        self.generic_visit(node)  # Fix: traverse children
        return node

    def visit_Attribute(self, node):
        # Transform: semantic_var.property -> __extract(semantic_var, 'property')
        if isinstance(node.value, ast.Name) and node.value.id in self.semantic_vars:
            return ast.Call(
                func=ast.Name(id='__extract', ctx=ast.Load()),
                args=[node.value, ast.Constant(value=node.attr)],
                keywords=[]
            )
        return node

def transpile(code):
    tree = ast.parse(code)
    tree = AgentLangTranspiler().visit(tree)
    return ast.unparse(tree)