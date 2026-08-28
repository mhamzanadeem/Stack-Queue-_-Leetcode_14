# Stack & Queue - LeetCode 14 Problem Collection

> A beginner-friendly walkthrough of 14 LeetCode problems using **Stacks** and **Queues**.

---

## Table of Contents

- [All 14 Solutions with Links](#all-14-solutions-with-links)
- [Step-by-Step Diagram: Valid Parentheses](#step-by-step-diagram-valid-parentheses)
- [Concept Explainers](#concept-explainers)
  - [LIFO vs FIFO](#lifo-vs-fifo)
  - [Valid Parentheses Explained](#valid-parentheses-explained)
  - [Min Stack Explained](#min-stack-explained)
  - [Queue Using Two Stacks + Amortized Cost](#queue-using-two-stacks--amortized-cost)

---

## All 14 Solutions with Links

| #  | Problem                                                           | Difficulty | Data Structure | Solution File                             |
|----|-------------------------------------------------------------------|------------|----------------|-------------------------------------------|
| 1  | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)                       | Easy       | Stack          | [`valid_parentheses.py`](valid_parentheses.py)                         |
| 2  | [Min Stack](https://leetcode.com/problems/min-stack/)                                         | Medium     | Stack          | [`min_stack.py`](min_stack.py)                                         |
| 3  | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)   | Easy       | Stack          | [`implement_queue_using_stacks.py`](implement_queue_using_stacks.py)   |
| 4  | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)   | Easy       | Queue          | [`implement_stack_using_queues.py`](implement_stack_using_queues.py)   |
| 5  | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)                | Medium     | Queue          | [`design_circular_queue.py`](design_circular_queue.py)                 |
| 6  | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)          | Easy       | Stack          | [`backspace_string_compare.py`](backspace_string_compare.py)           |
| 7  | [Remove All Adjacent Duplicates](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | Easy | Stack | [`remove_all_adjacent_duplicates_in_string.py`](remove_all_adjacent_duplicates_in_string.py) |
| 8  | [Make The String Great](https://leetcode.com/problems/make-the-string-great/)                | Easy       | Stack          | [`make_the_string_great.py`](make_the_string_great.py)                 |
| 9  | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | Easy | Stack | [`minimum_add_to_make_parentheses_valid.py`](minimum_add_to_make_parentheses_valid.py) |
| 10 | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | Medium | Stack | [`minimum_remove_to_make_valid_parentheses.py`](minimum_remove_to_make_valid_parentheses.py) |
| 11 | [Dota2 Senate](https://leetcode.com/problems/dota2-senate/)                                  | Medium     | Queue          | [`dota2_senate.py`](dota2_senate.py)                                   |
| 12 | [Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) | Medium | Queue | [`find_the_winner_of_the_circular_game.py`](find_the_winner_of_the_circular_game.py) |
| 13 | [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)              | Easy       | Queue          | [`number_of_recent_calls.py`](number_of_recent_calls.py)               |
| 14 | [Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) | Easy | Queue | [`number_of_students_unable_to_eat_lunch.py`](number_of_students_unable_to_eat_lunch.py) |

---

## Step-by-Step Diagram: Valid Parentheses

**Problem:** Given a string `s` containing just `(` and `)`, determine if the input string is valid.

**Input:** `s = "(())"`

We process each character one at a time. The stack holds opening brackets we haven't matched yet.

```
Input string:  (  (  )  )
Index:         0  1  2  3

============================================================
STEP 0:  char = '('
============================================================

  Character is '('  -->  PUSH onto stack

  String:   (  (  )  )
             ^
             processing here

  Stack:    [ ( ]        <-- top

============================================================
STEP 1:  char = '('
============================================================

  Character is '('  -->  PUSH onto stack

  String:   (  (  )  )
                ^
                processing here

  Stack:    [ (          <-- top
             ( ]

============================================================
STEP 2:  char = ')'
============================================================

  Character is ')'  -->  Check top of stack
  Top of stack is '('   -->  MATCH! Pop '('

  String:   (  (  )  )
                   ^
                   processing here

  Stack:    [ ( ]        <-- top

============================================================
STEP 3:  char = ')'
============================================================

  Character is ')'  -->  Check top of stack
  Top of stack is '('   -->  MATCH! Pop '('

  String:   (  (  )  )
                      ^
                      processing here

  Stack:    [ ]  (empty!)

============================================================
RESULT:  Stack is empty  -->  VALID!  (return True)
============================================================
```

**Another example:** `s = "(()"`

```
Input string:  (  (  )

STEP 0:  char = '('  --> Push    Stack: [ ( ]
STEP 1:  char = '('  --> Push    Stack: [ (  ( ]
STEP 2:  char = ')'  --> Match!  Stack: [ ( ]

End: Stack is NOT empty  -->  INVALID!  (return False)
```

**Key Idea:** Every closing bracket `)` must have a matching opening bracket `(` before it. The stack tracks which opening brackets are still waiting to be matched.

---

## Concept Explainers

### LIFO vs FIFO

These are two fundamental ways to organize data:

```
LIFO - Last In, First Out              FIFO - First In, First Out
(Stack)                                 (Queue)

   |   |                                  ___________
   | 3 |  <-- 3 entered LAST             |           |
   | 2 |      but leaves FIRST           | 1  2  3   |  1 entered FIRST
   | 1 |  <-- 1 entered FIRST            |___________|  but leaves FIRST
   |___|                                  1st      3rd

   Think: Stack of plates                Think: Line at a grocery store
```

#### Real-World LIFO Example: Stack of Plates

```
    You put plates here (top)
         ___________
        |           |
        |   PLATE   |  <-- You take THIS one first (the top one)
        |___________|
        |           |
        |   PLATE   |  <-- This one stays
        |___________|
        |           |
        |   PLATE   |  <-- This was placed first but taken last
        |___________|

  When you add a plate: put it on TOP
  When you remove a plate: take from TOP
  => Last plate added = First plate removed (LIFO)
```

#### Real-World FIFO Example: Line at a Grocery Store

```
  CASHIER serves here
      |
      v
  +-------+   +-------+   +-------+   +-------+
  | Person|-->| Person|-->| Person|-->| Person|
  |  (A)  |   |  (B)  |   |  (C)  |   |  (D)  |
  +-------+   +-------+   +-------+   +-------+
   1st in       2nd          3rd         4th in
   line        in line      in line      line

  Person A arrived FIRST  -->  Person A is served FIRST
  Person D arrived LAST   -->  Person D waits the LONGEST

  => First person in = First person out (FIFO)
```

---

### Valid Parentheses Explained

**The Problem:** Check if brackets `()`, `{}`, `[]` are properly opened and closed in the right order.

**The Trick:** Use a **stack** and a **mapping** of closing-to-opening brackets.

```
  mapping = { ")": "(",  "}": "{",  "]": "[" }

  For each character in the string:
  ┌──────────────────────────────────────────────────────┐
  │  Is it a CLOSING bracket?                           │
  │  YES --> Is the stack top the matching opener?      │
  │          YES --> Pop it (they matched!)             │
  │          NO  --> Return False (mismatch!)           │
  │  NO  --> It's an OPENING bracket. Push it on stack.│
  └──────────────────────────────────────────────────────┘

  After processing everything:
  Stack empty?  -->  Valid!
  Stack has stuff?  -->  Invalid (unmatched openers)
```

**Why a stack?** Because the most recent unmatched opener is always the one we need to check next. That's exactly what a stack gives us - access to the most recent item.

```
  Example:  ( [ ] )

  (  --> push (          Stack: [ ( ]
  [  --> push [          Stack: [ (, [ ]
  ]  --> top is [  MATCH! Pop [   Stack: [ ( ]
  )  --> top is (  MATCH! Pop (   Stack: [ ]

  Stack empty --> VALID!
```

---

### Min Stack Explained

**The Problem:** Design a stack that supports `push`, `pop`, `top`, and `getMin` -- all in **O(1)** time.

**The Trick:** Use **two stacks**:

```
  ┌─────────────────────┐     ┌─────────────────────┐
  │     main_stack      │     │     min_stack        │
  │   (holds all values)│     │  (tracks minimums)   │
  ├─────────────────────┤     ├─────────────────────┤
  │                     │     │                     │
  │   push(5)           │     │   push(5)           │  5 is new min
  │   push(3)           │     │   push(3)           │  3 < 5, so push 3
  │   push(7)           │     │                     │  7 > 3, skip
  │   push(2)           │     │   push(2)           │  2 < 3, so push 2
  │                     │     │                     │
  └─────────────────────┘     └─────────────────────┘

  getMin() --> look at top of min_stack --> returns 2

  When we pop(2):
    main_stack:  pop 2
    min_stack:   top IS 2, so also pop 2

  getMin() --> now returns 3
```

**The Rule:**
- **Push(x):** Always push to `main_stack`. Only push to `min_stack` if `x <= current min`.
- **Pop():** If the value being popped equals the top of `min_stack`, pop from `min_stack` too.
- **getMin():** Just return the top of `min_stack`.

**Why does this work?** The `min_stack` keeps a "history of minimums". Each time a new minimum arrives, we record it. When that minimum is removed, we go back to the previous minimum.

```
  Operations:    push(5)   push(3)   push(7)   pop()    getMin()

  main_stack:      [5]      [5,3]   [5,3,7]   [5,3]     [5,3]
  min_stack:       [5]      [5,3]   [5,3]     [5,3]     [5,3]
  min value:        5         3        3         3         3
```

---

### Queue Using Two Stacks + Amortized Cost

**The Problem:** Implement a FIFO queue using only two LIFO stacks.

**The Trick:** Two stacks + lazy transfer

```
  stack_in:   handles PUSH operations
  stack_out:  handles POP and PEEK operations

  PUSH(x):
  ┌────────────────────────────────────────┐
  │  Just push x onto stack_in            │
  │  This is ALWAYS O(1)                  │
  └────────────────────────────────────────┘

  POP() / PEEK():
  ┌────────────────────────────────────────┐
  │  Is stack_out empty?                  │
  │  YES --> Move ALL elements from       │
  │          stack_in to stack_out        │
  │          (this reverses the order!)   │
  │  NO  --> Just pop/peek from stack_out│
  └────────────────────────────────────────┘
```

**Visual walkthrough:**

```
  PUSH 1, 2, 3:

  stack_in:  [1, 2, 3]      stack_out: [ ]
               ^                  ^
             push here          empty

  POP() --> stack_out is empty, so TRANSFER:

  Transfer all from stack_in to stack_out:
    pop 3 from stack_in, push to stack_out
    pop 2 from stack_in, push to stack_out
    pop 1 from stack_in, push to stack_out

  stack_in:  [ ]              stack_out: [3, 2, 1]
                                  ^
                               pop from here

  POP() --> returns 1  (oldest first = FIFO!)
  POP() --> returns 2
  POP() --> returns 3
```

#### Amortized Cost Analysis

This is the key insight: **transferring elements looks expensive, but it's actually cheap over time.**

```
  ┌─────────────────────────────────────────────────────────────┐
  │  Each element is moved at most ONCE from stack_in          │
  │  to stack_out during its entire lifetime.                  │
  │                                                           │
  │  Cost per element:                                        │
  │    Push onto stack_in:    1 operation                     │
  │    Transfer to stack_out: 1 operation (happens once)      │
  │    Pop from stack_out:    1 operation                     │
  │    ─────────────────────────────────                      │
  │    TOTAL: 3 operations per element = O(1) amortized       │
  └─────────────────────────────────────────────────────────────┘
```

```
  Example: Push 5 elements, then pop 5 elements

  Naive approach would think: "Transfer moves 5 elements = O(n)!"
  But consider the FULL picture:

  Operation       Cost    Running Total   Amortized Cost
  ─────────────────────────────────────────────────────
  push(1)          1          1             1/1 = 1.0
  push(2)          1          2             2/2 = 1.0
  push(3)          1          3             3/3 = 1.0
  push(4)          1          4             4/4 = 1.0
  push(5)          1          5             5/5 = 1.0
  pop()           6*          11            11/6 = 1.83
  pop()           1          12            12/7 = 1.71
  pop()           1          13            13/8 = 1.63
  pop()           1          14            14/9 = 1.56
  pop()           1          15            15/10 = 1.50

  * 6 = 5 transfers + 1 pop

  Over 10 operations, total cost = 15
  Average cost per operation = 15/10 = 1.5 = O(1) amortized!
```

**Bottom line:** Even though a single transfer can cost O(n), that cost is **spread across** all the operations. On average, each operation is still O(1). This is what "amortized" means -- expensive operations are rare enough that the average stays low.

---

## Quick Reference: When to Use What

| Scenario              | Data Structure | Why                              |
|-----------------------|----------------|----------------------------------|
| Match parentheses     | Stack          | Need to check most recent first  |
| Undo/redo functionality| Stack         | LIFO behavior                    |
| BFS / level traversal | Queue          | Process in arrival order         |
| Sliding window        | Queue/Deque    | Maintain a moving window         |
| Reverse something     | Stack          | LIFO reverses order naturally    |

---

> **Remember:** Stacks and Queues are simple structures, but they solve a surprising number of problems. The key is recognizing **when** you need LIFO (stack) vs FIFO (queue) behavior!
