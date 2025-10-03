"""
AgentLang - A programming language where text has semantic properties
"""

from .transpiler import transpile
from .runtime import __extract, load_file

__all__ = ['transpile', '__extract', 'load_file']
__version__ = '0.1.0'