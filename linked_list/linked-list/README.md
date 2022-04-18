# Singly Linked List
A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail). Each element in a linked list is called a node. A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.

## Challenge
<!-- Description of the challenge -->
### Node

- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

### Linked List

- Create a Linked List class
- Within your Linked List class, include a head property.
    - Upon instantiation, an empty Linked List should be created.
- The class should contain the following methods
    - insert
        - Arguments: value
        - Returns: nothing
        - Adds a new node with that value to the head of the list with an O(1) Time performance.
    - includes
        - Arguments: value
        - Returns: Boolean
         - Indicates whether that value exists as a Node’s value somewhere within the list.
    - to string
        - Arguments: none
        - Returns: a string representing all the values in the Linked List, formatted as:
        - "[ a ] -> [ b ] -> [ c ] -> NULL"

    - Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
    - Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

### Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

1. Can successfully instantiate an empty linked list
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list
4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
What approach did you take?
- Singly Linked List

Why?
- Linked list is a linear data structure which overcomes the limitation of another data structure array. In the linked list, each element is considered as an object. Unlike array, in Linked list, there is no any contiguous memory structure. Here each element is linked to the next element through a pointer.

What is the Big O space/time for this approach? 
- O(n)

## API
- The class should contain the following methods
    - insert
        - Arguments: value
        - Returns: nothing
        - Adds a new node with that value to the head of the list with an O(1) Time performance.
    - includes
        - Arguments: value
        - Returns: Boolean
         - Indicates whether that value exists as a Node’s value somewhere within the list.
    - append 
        - Arguments: value
        - Returns: nothing
        - Adds a new node with that value to the end of the list with an O(n) Time performance.
    - to string
        - Arguments: none
        - Returns: a string representing all the values in the Linked List, formatted as:
        - "[ a ] -> [ b ] -> [ c ] -> NULL"