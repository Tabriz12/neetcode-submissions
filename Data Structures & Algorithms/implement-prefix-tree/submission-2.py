
from dataclasses import dataclass, field
from typing import Self

@dataclass
class Node:

    val: str
    childs: dict = field(default_factory=dict)
    is_end: bool = False

class PrefixTree:

    def __init__(self):

        self.head = Node(val="")


    def insert(self, word: str) -> None:

        st = self.head

        for i in range(len(word)):

            if word[i] not in st.childs:
                break
            
            st = st.childs[word[i]]
        
        else:

            st.is_end = True
            return

                
        for j in range(i, len(word)):

            st.childs[word[j]] = Node(val=word[j])

            st = st.childs[word[j]]
        
        st.is_end = True
        
        


    def search(self, word: str) -> bool:

        st = self.head

        for i in range(len(word)):

            if word[i] not in st.childs:
                return False
            
            st = st.childs[word[i]]
        
        return st.is_end
        

        

    def startsWith(self, prefix: str) -> bool:

        st = self.head

        for i in range(len(prefix)):

            if prefix[i] not in st.childs:
                return False
            
            st = st.childs[prefix[i]]
        
        return True
        
        