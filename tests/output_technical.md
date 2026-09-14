# Knowledge Cards: Understanding Recursion in Programming

> Source: tests/test_technical.md
> Cards: 7 / 5-8 target

---

## Card 1: What Is Recursion

**Core Knowledge:**
Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar sub-problems.

**Explanation:**
Instead of solving a large problem directly, recursion divides it into smaller versions of the same problem. Each recursive call works on a simpler input, building up the final solution from the results of these smaller calls. This approach is particularly elegant for problems that have a naturally self-similar structure.

**Example / Self-test:**
Q: What makes recursion different from simply calling another function?

---

## Card 2: Base Case and Recursive Case

**Core Knowledge:**
Every recursive function needs a base case (which stops the recursion) and a recursive case (which calls itself with modified input moving toward the base case).

**Explanation:**
The base case is the termination condition — without it, the function recurses forever and causes a stack overflow. The recursive case must alter the input so that each call gets closer to the base case. For factorial, the base case is 0! = 1, and the recursive case is n! = n × (n-1)!.

**Example / Self-test:**
Q: What happens if a recursive function has no base case?

---

## Card 3: The Call Stack in Recursion

**Core Knowledge:**
Each recursive call is placed on the call stack, which tracks active function calls along with their parameters, local variables, and return addresses.

**Explanation:**
As recursion deepens, stack frames pile up. When the base case is reached, the stack unwinds: each frame returns its result to the frame below it, and the final answer is computed layer by layer. This is why recursion has memory overhead — each call consumes a stack frame.

**Example / Self-test:**
Q: What information does each stack frame hold during a recursive call?

---

## Card 4: Stack Overflow Risk

**Core Knowledge:**
Deep recursion consumes significant memory and can cause a stack overflow. Most languages set a recursion depth limit — Python defaults to about 1000 frames.

**Explanation:**
Because each recursive call adds a frame to the call stack, very deep recursion exhausts available stack space. This is a practical constraint that affects when recursion is safe to use: problems requiring thousands of recursive calls should be converted to iteration.

**Example / Self-test:**
Q: What is Python's default recursion depth limit?

---

## Card 5: Recursion vs. Iteration

**Core Knowledge:**
Any recursive solution can be rewritten iteratively. Recursion produces cleaner code for naturally recursive problems, while iteration is more memory-efficient.

**Explanation:**
Tree traversals, Tower of Hanoi, and divide-and-conquer algorithms like merge sort are naturally recursive and hard to express iteratively. But iteration avoids stack frame accumulation. The choice depends on problem structure and performance requirements — shallow, naturally recursive problems favor recursion; deep or performance-critical operations favor iteration.

**Example / Self-test:**
Q: Name one type of problem where recursion is usually preferred over iteration.

---

## Card 6: Tail Recursion Optimization

**Core Knowledge:**
Tail recursion optimization transforms a tail-recursive function (where the recursive call is the last operation) into an iterative loop, eliminating stack growth. Some languages support it; Python and Java do not.

**Explanation:**
When the recursive call is the final operation, the compiler can reuse the current stack frame instead of creating a new one. Languages like Scheme and Haskell guarantee this optimization. In Python and Java, even tail-recursive functions still accumulate stack frames and can overflow.

**Example / Self-test:**
Q: Do Python and Java support tail call optimization?

---

## Card 7: Common Recursion Pitfalls

**Core Knowledge:**
The most common recursion mistakes are forgetting the base case (causing infinite recursion) and making the recursive case move away from the base case (e.g., incrementing instead of decrementing).

**Explanation:**
Always verify that each recursive call brings the problem closer to termination. Forgetting the base case leads to a stack overflow. Even with a base case present, if the recursive case modifies the input in the wrong direction, the base case is never reached.

**Example / Self-test:**
Q: Why might a recursive function with a base case still recurse infinitely?
