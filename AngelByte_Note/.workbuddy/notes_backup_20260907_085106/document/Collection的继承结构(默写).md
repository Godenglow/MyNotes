---
来源文件: "[[Collection的继承结构(默写).mdj]]"
图类型: UML 类图 (Class Diagram)
转换时间: 2026-08-31
---

# Collection的继承结构(默写)

> 源文件：[[Collection的继承结构(默写).mdj]]

```mermaid
classDiagram
    direction LR

    class Collection {
        <<interface>>
    }
    class Iterable {
        <<interface>>
    }
    class Iterator {
        <<interface>>
    }
    class Queue {
        <<interface>>
    }
    class Deque {
        <<interface>>
    }
    class SequencedCollection {
        <<interface>>
    }
    class Set {
        <<interface>>
    }
    class List {
        <<interface>>
    }
    class SequencedSet {
        <<interface>>
    }
    class SortedSet {
        <<interface>>
    }
    class NavigableSet {
        <<interface>>
    }
    class LinkedList
    class ArrayList
    class Vector
    class Stack
    class TreeSet
    class HashSet
    class LinkedHashSet

    Iterable <|-- Collection
    Collection ..> Iterator
    Collection <|-- Queue
    Queue <|-- Deque
    Collection <|-- SequencedCollection
    Collection <|-- Set
    SequencedCollection <|-- List
    SequencedCollection <|-- SequencedSet
    Set <|-- SequencedSet
    SequencedSet <|-- SortedSet
    SortedSet <|-- NavigableSet
    List <|.. LinkedList
    Deque <|.. LinkedList
    List <|.. ArrayList
    List <|.. Vector
    Vector <|-- Stack
    NavigableSet <|.. TreeSet
    Set <|.. HashSet
    HashSet <|-- LinkedHashSet
    SequencedSet <|.. LinkedHashSet
```

