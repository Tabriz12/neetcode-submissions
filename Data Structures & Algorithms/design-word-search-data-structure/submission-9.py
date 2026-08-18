from dataclasses import dataclass, field
from typing import Self

@dataclass
class Node:

    val: str
    childs: dict[str, Self] = field(default_factory=dict)
    end: bool = False

    def next(self, child: str):

        try:

            return self.childs[child]
        
        except:

            raise KeyError(f"{child} is not a child of {self.val if self.val else "start"}")


class WordDictionary:

    def __init__(self):
        self.head = Node("")
        

    def addWord(self, word: str) -> None:
        
        i = 0
        cur_head = self.head

        for i in range(len(word)):

            try:
                cur_head = cur_head.next(word[i])
                #print(f"moved successfully to {word[i]}")
            
            except Exception as e:
                #print(f"Error moving to {word[i]}")
                break
        
        else:
            cur_head.end = True
            return

        for j in range(i, len(word)):

            cur_head.childs[word[j]] = Node(word[j])
            cur_head = cur_head.next(word[j])
        
        cur_head.end = True


    def search(self, word: str, cur_head = None) -> bool:

        if cur_head is None:
            cur_head = self.head
        

        for i in range(len(word)):

            if word[i] == '.':


                for child in cur_head.childs:
                    
                    if self.search(word[i+1:], cur_head.childs[child]):
                            return True

                
                return False
            
            else:

                try:
                    cur_head = cur_head.next(word[i])
                
                except Exception as e:
                    return False
        
        return cur_head.end


        
