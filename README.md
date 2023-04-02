# Data Structures and Algorithms Practice
## Introduction
This repository contains my solutions to algorithmic problems (mostly LeetCode, with some problems from other sites sprinkled in). Main languages are Python, Java, and C++. \
You are free to use this repository as you see fit, but please do not use this to cheat on your homework; you will only do yourself a disservice. Appreciate the chance to practice! \
Topics included:
1. Basic Algorithms: LC 412, LC 463
  * Recursion: LC 66
  * Sorting, Comparator and Comparable: LC 75 (Dutch Flag Problem), LC 88, LC 165, LC 179, LC 280, LC 436, LC 611, LC 825, LC 881, LC 910, LC 923 (3Sum with Multiplicity), LC 937, LC 945, LC 948, LC 969 (Pancake Sorting), LC 973, LC 976, LC 1029, LC 1051, LC 1169, LC 1196, LC 1288, LC 1311, LC 1326, LC 1365, LC 1383, LC 1604, LC 1619, LC 1632, LC 1636 (Sort by Frequency), LC 1834, LC 1838, LC 1859, LC 2007, LC 2092
    * Coordinate Compression: LC 327, LC 673, LC 1649
    * Merge Sorted Array: LC 977, LC 1213
    * Counting Sort: LC 451 (Solution 1), LC 539 (Minimum Time Difference), LC 561, LC 833, LC 1200 (Minimum Absolute Difference), LC 1202
      * Sorting By Frequency (exactly O(N)): LC 1338
    * Bucket Sort: LC 164 (Maximum Gap), LC 220
    * Radix Sort: LC 1163
    * Selection: LC 296 (Geometric Median on Grid)
      * QuickSelect: LC 462, LC 973 (Sol 2)
  * Binary Search: LC 4 (Median of 2 Sorted Arrays), LC 33 (Search in Rotated Sorted Array), LC 34, LC 35 (Search Insert Position), LC 57, LC 74, LC 81, LC 153 (Min of Rotated Sorted Array), LC 154, LC 162, LC 167, LC 240 (2D Binary Search), LC 302, LC 278, LC 313, LC 327, LC 374, LC 410 (sol 1, sol 2), LC 436, LC 441, LC 493, LC 497, LC 528, LC 540 (Single Element in a Sorted Array), LC 658, LC 644, LC 704, LC 744, LC 825, LC 875, LC 887 (Egg Drop), LC 900, LC 911, LC 1055, LC 1064 (Fixed Point in Sorted Array), LC 1150, LC 1196, LC 1315, LC 1838, LC 1901
    * Binary Search The Answer (BSTA): LC 222 (Sol 2), LC 275, LC 367, LC 483, LC 718 (Solution 2), LC 754, LC 774, LC 786 (Sol 2), LC 1011, LC 1231, LC 1283, LC 1337, LC 1631, LC 1891
    * Exponential Search (Search over unbounded list): LC 702 (Search in a Sorted Array of Unknown Size)
    * Parallel Binary Search: LC 1697
    <!-- * Fractional Cascading: LC 483 (Sol 2) -->
    * Missing Numbers: LC 1060 (Missing Element in Sorted Array), LC 710 (Random Pick with Blacklist), LC 1539 (Kth Missing Positive Number)
  * Ternary Search (Unimodal Array): LC 852 (Peak Index in a Mountain Array), LC 1095 (Find in Mountain Array)
  * Backtracking: LC 37 (Sudoku Solver), LC 39, LC 40 (Combination Sum II), LC 46, LC 47, LC 51-52 (N-Queens), LC 139-140 (Word Break), LC 79 (2D String Search), LC 90 (Subsets with Duplicates), LC 93, LC 131, LC 212, LC 216, LC 247, LC 257, LC 282, LC 306, LC 425, LC 465 (Optimal Account Balancing), LC 489, LC 526, LC 679, LC 784, LC 797 (All Paths From Source to Target), LC 980, LC 1079, LC 1088, LC 1219, LC 1239, LC 1291, LC 1307 (Verbal Arithmetic Puzzle)
    * Number Construction: LC 1215, LC 1849
  * Divide and Conquer: LC 23, LC 395 (Longest Substring with At Least K Repeating Characters), LintCode 399 (Nuts & Bolts Problem), Merge Sort: Counting Inversions (HR)
    * Halving Method: LC 49 (Sol 2), LC 932 (Arithmetic-Free Permutation)
    * Find Split Point in O(min(k, n - k)): BS 718
  * Greedy: LC 45, LC 55, LC 68 (Word Justification), LC 330, LC 376 (Wiggle Subsequence), LC 402, LC 406, LC 455, LC 484, LC 502 (IPO), LC 605, LC 630, LC 659, LC 678, LC 759 (Sol 2), LC 763, LC 910, LC 921, LC 942, LC 945, LC 948, LC 991, LC 1007 (Sol 2), LC 1024 (Sol 2), LC 1029, LC 1055, LC 1057, LC 1090, LC 1167, LC 1217, LC 1282, LC 1288, LC 1338, LC 1383, LC 1465, LC 1509, LC 1564, LC 1576, LC 1578, LC 1605, LC 1647, LC 1675, LC 1710, LC 1775, LC 2007
    * Exchange Argument: LC 2178
    * Packing/Assignment: LC 870, LC 881
    * Activity Selection Problem: LC 435 (Non-overlapping Intervals - Interval Scheduling), LC 452 (Minimum Number of Arrows to Burst Balloons), LC 1326, LC 1353
      * Longest Remaining Time First Scheduling: LC 358, LC 621 (Task Scheduler), LC 1405
      * Shortest Job First Scheduling (SJF): LC 1834
    * Huffman Coding: LC 1199
    * Digits/Lexicographical Order: LC 670, LC 1202, LC 1323, LC 1663, Studious Student (Hacker Cup 2011 Qualification Round)
    * Rearrangement Inequality: LC 1589, LC 2285
  * Count Array/Histogram: LC 274, LC 791 (Custom Sort String), LC 1347, LC 1426, LC 1429, LintCode 960
  * Contribution Analysis: LC 1588
2. Arrays: LC 41, LC 59, LC 73, LC 163, LC 251 (Flatten 2D Vector), LC 277, LC 419, LC 442, LC 453, LC 485, LC 566 (Reshape the Matrix), LC 624, LC 628, LC 717, LC 766, LC 835 (Convolution), LC 896, LC 941, LC 1089, LC 1299, LC 1431, LC 1437, LC 1464, LC 1470, LC 1512, LC 1528, LC 1534, LC 1672
  * Basic Operations: LC 27 (removeAll), LC 48 (Rotate Image), LC 84, LC 108 (Sorted Array to BST), LC 238, LC 832 (Flipping an Image), LC 349 (Intersection), LC 1929 (Concatenation of Array), Rotate left (HR)
  * Diagonal: LC 1572
    * Main Diagonal (indexed by difference of coords): LC 1329 (Sort the Matrix Diagonally), LC 2013
    * Anti Diagonal (indexed by sum of coords): LC 498 (Diagonal Traverse), LC 2013
  * Meet in the Middle: LC 18 (4Sum), LC 454 (4Sum II), LC 805
  * Prefix Sum/Cumulative Sum: LC 134, LC 250, LC 303 (Range Sum Query - Immutable), LC 325, LC 396, LC 437 (Path Sum), LC 497, LC 508, LC 523, LC 525, LC 548, LC 554, LC 560, LC 644, LC 724, LC 775, LC 848, LC 900, LC 915, LC 918, LC 930, LC 974, LC 1031, LC 1074, LC 1176, LC 1196, LC 1248, LC 1310, LC 1352, LC 1375, LC 1423, LC 1480, LC 1573, LC 1653, LC 1712, LC 1762, LC 1838
    * 2D: LC 1444
  * Caching: LC 304 (Range Sum Query 2D - Immutable)
  * Local Optima (Peaks/Troughs): LC 122 (Best Time to Buy and Sell Stock II), LC 135, LC 376 (Wiggle Subsequence)
  * Difference Array: LC 121, LC 123 (Best Time to Buy and Sell Stock III)
    * Offline Range Addition Query (Boundary Count): LC 370 (Range Addition), Array Manipulation (HR), LC 731 (Java Sol), LC 1589
    * Difference Square: LC 250 (Count Univalue Subtrees)
  * Sliding Window: LC 487, LC 643, LC 674, LC 786 (Sol 2), LC 1052, LC 1105, LC 1151, LC 1169, LC 1291 (Sol 2), LC 1438, LC 1456, LC 1493
  * Cyclicity: LC 189 (Rotate Array)
  * Majority Element:
    * Boyer-Moore Algorithm: LC 169, LC 1157
  * Use nums[abs(num) - 1] as flag for num: LC 442, LC 448
  * Search in Matrix with Sorted Rows and Columns - Staircase Traversal (O(M + N)): LC 240 (Solution 2), LC 1237, LC 1351
  * Patterns Repating K Times Consecutively: LC 1566
  * Find top K: LC 414
3. Linked List: LC 2, LC 21, LC 23, LC 25, LC 61, LC 82, LC 86, LC 92, LC 138 (Copy List with Random Pointer), LC 142, LC 143, LC 328, LC 369, LC 379, LC 445, LC 817, LC 1265, LC 1290
  * Operations: LC 83 (Deduplicate Sorted List), LC 109 (Sorted List to BST), LC 141 (Floyd Cycle Detection), LC 160 (Intersection), LC 203 (Remove All), LC 206 (Reverse), Reverse (HR, Non-destructive) LC 234 (isPalindrome), LC 237 (Delete), LC 725 (Split Linked List in Parts), LC 1721 (Swapping Nodes)
  * Sort: LC 147 (Insertion), LC 148 (Merge Sort)
  * Doubly Linked List: LC 146, LC 432, LC 2502, Reverse Doubly Linked List (HR)
  * Circularly Linked List: LC 281 (Zigzag Iterator), LC 708 (Insert into a Sorted Circular Linked List)
  * Slow Fast Pointer: LC 287, LC 876 (Middle of the Linked List)
  * Multi-Level: LC 430 (Flatten)
  * Cache: LC 146 (LRU Cache), LC 460 (LFU Cache)
4. Stack, Queue, Deque: LC 225 (Implement Stack using Queues), LC 232 (Implement Queue using Stacks)
  * Stack: LC 71 (Simplify Path), LC 106, LC 150 (Reverse Polish Notation), LC 155 (Min Stack), LC 173, LC 224 + 227 (Infix to Postfix/Dijkstra's Shunting yard algorithm), LC 234, LC 394 (Solution 2), LC 402, LC 581, LC 636, LC 682, LC 716 (Max Stack), LC 722, LC 735, LC 880, LC 889, LC 895 (Maximum Frequency Stacks), LC 917, LC 946, LC 1019, LC 1047, LC 1209, LC 1441
    * Parentheses:  LC 20 (Valid Parentheses), LC 394, LC 536, LC 856 (Score of Parentheses, Sol 1), LC 921, LC 1249 (Minimum Remove to Make Valid Parentheses)
  * Queue: LC 105, LC 106, LC 158, LC 346, LC 353 (Design Snake Game), LC 358, LC 621 (Task Scheduler), LC 622 (Circular Queue), LC 889, LC 917, LC 933, LC 1043, LC 1429
    * Rate Limiter: LC 362 (Design Hit Counter), LC 1604
  * Deque: LC 84, LC 199, LC 341, LC 456, LC 641 (Circular Deque), LC 644, LC 659, LC 862, LC 901, LC 907, LC 2271, LintCode 960
  * Monotonicity: LC 85, LC 402, LC 456, LC 581, LC 862, LC 901, LC 907, LC 1019
    * Stack: LC 134, LC 496 (Next Greater Element), LC 683, LC 1504, LC 1673, LC 1944, LC 1996 (Solution 2)
    * Deque: LC 503, LC 1105, LC 1425 (Solution 2)
5. Tree: LC 113, LC 572 (Subtree of Another Tree), LC 582, LC 865, LC 1161, LC 1367 (Linked List in Binary Tree)
  * Binary: LC 100 (equals), LC 112, LC 101 (Symmetric), LC 105 (BT from Preorder and Inorder), LC 106 (BT from Inorder and Postorder), LC 111 (Minimum Depth), LC 114 (Flatten), LC 124, LC 129, LC 156 (Upside Down), LC 199 (Right Side View), LC 222, LC 226 (Invert), LC 298, LC 366 (Find Leaves of Binary Tree), LC 257 (Root-to-Leaf Paths), LC 404 (Sum of Left Leaves), LC 513, LC 515, LC 543 (Diameter), LC 545 (Boundary), LC 563 (Tilt), LC 617 (Merge Two Trees), LC 623, LC 637 (Average of Levels), LC 669 (Trim), LC 742 (Closest Leaf), LC 814, LC 863 (All Nodes Distance K in Binary Tree), LC 872 (Leaf-Similar), LC 889 (BT from Preorder and Postorder), LC 951, LC 958 (Check Completeness), LC 965 (Univalued) LC 971, LC 988, LC 1022 (Sum of Root To Leaf Binary Numbers), LC 1110, LC 1120 (Maximum Average Subtree), LC 1123, LC 1302, LC 1448, LC 1457, LC 1469, LC 1602 (Nearest Right Node), LC 1660, LC 1740 (Find Distance), LC 1973, Optimal BST (GFG)
    * Serialization: LC 297 (Serialize and Deserialize), LC 331 (Verify Preorder Serialization), LC 536 (Construct Binary Tree from String)
    * Binary Tree Traversal: LC 94 (BT Inorder), LC 103 (Zig Zag Level Order), LC 144 (BT Preorder), LC 145 (BT Postorder), LC 897, LC 987 (Vertical Order), LC 1214
      * Morris Traversal: LC 99 (Sol 2)
      * Binary Code: LC 222 (Sol 2), LC 662 (Maximum Width of Binary Tree)
  * Euler Tour/Tree Flattening: LC 250, LC 508
  * LCA: LC 235 (BST), LC 236, LC 1650 (LCA with Parent Pointer), LC 1724
  * Filepath/File System: LC 388, LC 588 (Design In-Memory File System), LC 609 (Find Duplicate File in System), LC 1166 (Design File System)
  * x = change(x): LC 1325
  * N-ary Tree: LC 428 (Serialize and Deserialize N-ary Tree; Newick Format), LC 431 (Encode N-ary Tree to Binary Tree), LC 559 (Maximum Depth), LC 589 (Preorder Traversal), LC 1490 (Clone N-ary Tree), LC 1506
  * Small To Large Merge/DSU on Tree/Sack: LC 1519, LC 1530
6. Binary Search Tree: LC 98, LC 99, LC 315, LC 352, LC 538, LC 653 (2Sum on BST), LC 729, LC 981, LC 1038 (BST to GST)
  * Operations: LC 109 (Sorted List to BST), LC 173 (Iterator), LC 230 (Kth Smallest Element in a BST), LC 270 (Closest Binary Search Tree Value), LC 285 (Inorder Successor), LC 426 (BST to Doubly Circular Linked List) LC 450 (Delete), LC 510, LC 530, LC 700 (Search), LC 701 (Insert), LC 783, LC 938 (Range Sum). isBST (HR), LC 1008 (Construct BST from Preorder Traversal), LC 1382 (Balance BST)
  * Pre Order Traversal (Insertion Order): LC 449 (Serialize and Deserialize BST)
  * Node's range management: LC 255 (Verify Preorder Sequence), LC 333 (Largest BST Subtree), LC 1008 (Construct BST from Preorder Traversal)
7. Graphs: LC 24, LC 997, LC 1557, LC 1743, LC 2508
  * Basic Operation: LC 133 (Clone, Undirected)
  * Shortest Path:
    * Dijkstra: LC 399, LC 505, LC 743, LC 1786
    * Dial's Algorithm (constraint edge weight): LC 743 (Solution 2)
      * 0-1 BFS: LC 1263
    * Bellman-Ford: LC 787
    * A*: LC 1197
  * DFS: LC 112, LC 116, LC 207(Detect Cycle in Directed Graph), LC 257, LC 298, LC 329, LC 339, LC 332, LC 364, LC 437, LC 490, LC 547 (Solution 2), LC 549, LC 559, LC 582, LC 623, LC 684 (Detect Cycle in Undirected Graph), LC 690, LC 720, LC 802, LC 814, LC 820, LC 841, LC 863 (All Nodes Distance K in Binary Tree), LC 886 (Possible Bipartition), LC 965, LC 971, LC 979, LC 993, LC 1059, LC 1123, LC 1136, LC 1192 (DFS Low Link/Finding Bridges), LC 1302, LC 1306 (Reachability), LC 1315, LC 1361, LC 1376, LC 1448, LC 1457, LC 1466, LC 1469, LC 1631, LC 1740, LC 1973, LC 2092
    * Connected Components: LC 200 (Connected Components), LC 323 (Number of Connected Components in an Undirected Graph), LC 565, LC 924, LC 947
    * Strongly Connected Components (Kosaraju-Sharir Algorithm): LC 1520
      * 2-SAT: LC 2128
    * Flood Fill (DFS on Grid): LC 130, LC 417, LC 200, LC 529 (Minesweeper), LC 694, LC 695, LC 733, LC 827, LC 934, LC 1254, LC 1391
    * Directed Cycle: LC 1153 (String Transforms Into Another String)
  * BFS: LC 102, LC 107, LC 126, LC 127, LC 210, LC 310, LC 314 (Binary Tree Vertical Order Traversal), LC 317 (Shortest Distance from All Buildings), LC 386, LC 433, LC 513, LC 515, LC 637, LC 742 (Closest Leaf), LC 773, LC 752, LC 785, LC 815, LC 818, LC 864, LC 934, LC 958 (Check Completeness), LC 994, LC 1091, LC 1161, LC 1236, LC 1284, LC 1293, LC 1311, LC 1345, LC 1602, LC 1660, LC 1730, LC 1926, LC 2096
    * BFS on State-Transition Graph: LC 2059
    * Simultaneous BFS/Multi-Source BFS: LC 286
  * Topological Sort:
    * Kahn's Algorithm: LC 269, LC 444, LC 802 (Solution 2), LC 851, LC 2115, LC 2392
    * Incremental Computation: LC 631 (Excel Sum Formula)
  * Minimum Spanning Tree (MST):
    * Prim: HR
    * Kruskal: LC 1135, LC 1168, LC 1319, LC 1489, LC 1584 (Manhattan MST), LC 1697
      * Minimax Path: LC 778
        * Kruskal Reconstruction Tree/DSU-Tree/Reachability Tree: LC 1724
  * TSP:
    * aTSP: LC 943 (Shortest Superstring) (Solved with DP, Bellman–Held–Karp algorithm)
  * Eulerian Circuit: LC 753 (Hierholzer's Algorithm)
  * Cycle Decomposition: LC 765
  * Stable Marriage Problem (Gale-Shapley Algorithm): DailyCoding
  * Max Flow:
    * Maximum Bipartite Matching (Kuhn's Algorithm): LC 1820
8. Heap: LC 630, LC 755, LC 1167, LC 1606, LC 2402, Maximum distinct elements after removing K elements (GFG)
  * Priority Queue: LC 347, LC 358, LC 621 (Task Scheduler), LC 642, LC 716 (Max Stack), LC 759 (Sol 2), LC 1046, LC 1057, LC 1424, LC 1834
    * Indexed Priority Queue: LC 1353, LC 1425, LC 1786, LC 1801
  * HeapSort: LC 215
   * Partial Heapsort (for top K): LC 692, LC 703 (Kth Largest Element in a Stream), LC 1086, LC 1337
  * Two Heaps: LC 295 (Find Median from Data Stream), LC 480 (Sliding Window Median), LC 502 (IPO)
  * Fracturing Search: LC 1439 (Find the Kth Smallest Sum of a Matrix With Sorted Rows)
    * K Way Merge: LC 355 (Design Twitter), LC 373, LC 378 (Kth Smallest Element in a Sorted Matrix), LC 786 (K-th Smallest Prime Fraction)
9. Trie/Prefix Tree: LC 208, LC 211, LC 212, LC 336, LC 472, LC 642, LC 676, LC 720, LC 820, LC 1032, LC 1461
  * Bit Trie: LC 421 (Maximum XOR of Two Numbers in an Array), LC 1707 (Maximum XOR With an Element From Array), LC 1938
  * Trie on Tree: LC 1430 (Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree)
  * Trie on Sorted Set: LC 2135
  * Trie Map: LC 677 (with prefix sum)
10. Set, Map (Dictionary)
  * Map: LC 49, LC 128, LC 146, LC 166 (Fraction to Recurring Decimal), LC 246, LC 380 (Randomized Set), LC 359, LC 387, LC 432, LC 451 (Solution 2), LC 535, LC 811, LC 815, LC 953, LC 966, LC 981, LC 1056, LC 1152, LC 1396, LC 1629, LC 1797, LC 1817, LC 2502
    * Cache: LC 146 (LRU Cache), LC 460 (LFU Cache)
    * Inverted Index: LC 105, LC 219, LC 243, LC 244, LC 245, LC 325, LC 398, LC 403, LC 496, LC 524, LC 525, LC 599, LC 609 (Find Duplicate File in System), LC 690, LC 697, LC 760, LC 791 (Custom Sort String), LC 828, LC 1027 (Longest Arithmetic Subsequence), LC 1051, LC 1055, LC 1074, LC 1102, LC 1138, LC 1156, LC 1157, LC 1198, LC 1477
      * Next/Prev Pointer: LC 1182
    * Group By: LC 249, LC 963
    * Sparse Vector/Matrix: LC 311 (Sparse Matrix Multiplication), LC 1570 (Dot Product of Two Sparse Vectors)
    * Bidirectional Map (BiMap): LC 205, LC 936, LC 734, LC 2034
  * Set: LC 128, LC 217 (Contains Duplicate), LC 353 (Design Snake Game), LC 356, LC 380 (Randomized Set), LC 771
    * Deduplication: LC 532, LC 575, LC 804, LC 859, LC 1207, LC 1838
    * Existence: LC 379, LC 755, LC 1684, LC 1832
    * Intersection: LC 548
  * Sorted Set/Map: LC 635 (Solution 2), LC 855, LC 975, LC 1105, LC 1244 (Solution 2), LC 1348 (Solution 2), LC 1395, LC 1438, LC 1500, LC 1606, LC 2034
    * Coastline/Pareto Frontier: LC 1996
  * Multiset: LC 692, LC 904, LC 1438
  * Frequency Map/Histogram/Counter: LC 47, LC 159, LC 266, LC 299, LC 340 (Longest Substring with At Most K Distinct Characters), LC 350, LC 389, LC 381 (Insert Delete GetRandom O(1) - Duplicates allowed), LC 383, LC 409, LC 423, LC 424, LC 447, LC 532, LC 554, LC 594, LC 697, LC 794, LC 819, LC 869, LC 884, LC 895 (Maximum Frequency Stack), LC 911, LC 916, LC 923 (3Sum with Multiplicity), LC 930, LC 1002, LC 1010, LC 1079, LC 1133, LC 1160, LC 1169, LC 1207, LC 1248, LC 1311, LC 1338, LC 1457, LC 1460, LC 1573, LC 1603, LC 1636 (Sort by Frequency), LC 1649, LC 1657, LC 1679, LC 1700, LC 1704, LC 1711, LC 1748, LC 1775, LC 1861, LC 2007, LC 2080, LC 2085
    * Cumulative Frequency/Prefix Counter: LC 395 (Longest Substring with At Least K Repeating Characters), LC 825 (Solution 2), LC 1297
    * Prefix Inverted Index (Shortest Subarray Ending At Current Index): LC 1477
  * Two Sum: LC 1 (Two Sum), LC 15 (3Sum), LC 653 (2Sum on BST), LC 1711
11. Hash: LC 128, LC 146, LC 242, LC 380 (Randomized Set), LC 387, LC 535, LC 771, LC 489, LC 957
  * Separate Chaining: LC 705 (Design Hash Set)
  * Rolling Hash/String Polynomial Hash: LC 187, LC 718 (Solution 2), LC 1044, LC 1147, LC 1316, LC 1461 (Solution 2), LC 1554 (Solution 2)
  * Designing Hash Function: LC 149, LC 939
  * Cuckoo Hashing: LC 706 (Design Hashmap)
  * Merkle Tree: LC 572 (Subtree of Another Tree, Sol 2), LC 652 (Find Duplicate Subtrees), LC 694, LC 1379
12. Range Query: LC 131O (Range XOR)
  * Segment Tree (Construction and Update; Range Sum Query): LC 152, LC 307, LC 1157 (Range Majority Element Query), LC 2080 (Range Frequency Queries - each node stores a counter)
    * Dynamic/Implicit: LC 699, LC 731 (Python Solution), LC 715, LC 732, LC 1649, LC 2158
    * Wavelet Tree/Weighted Segment Tree (i.e Segment Tree of Count of Values in Range): LC 327, LC 673, LC 1649
    * Lazy Propagation: LC 715, LC 699, LC 2158
    * 2D Segment Tree:  LC 427 (Construct Quad Tree)
    <!-- * Lazy Propagation: LC 732 -->
  * Fenwick Tree/Binary Indexed Tree (BIT): LC 307 (Range Sum Query Mutable, Sol 2)
    * 2D BIT: LC 308 (Range Sum Query 2D - Mutable)
  * Sparse Table: LC 1335 (Sol 1)
  * Sqrt Decomposition:
    * Mo's Algorithm: LC 1310 (Sol 2)
13. Union-Find/Disjoint Sets: LC 128, LC 261, LC 305, LC 547 (sol 1), LC 684, LC 721, LC 737, LC 839, LC 952, LC 990, LC 1102, LC 1101, LC 1135 (Kruskal), LC 1168, LC 1202, LC 1319, LC 1489, LC 1584, LC 1632, LC 1697, LC 1724, LC 2424
  * Cycle Detection: LC 1559 (2D Grid)
14. Other Data Structures: LC 284 (Peeking Iterator), LC 432
  * Intervals: LC 56 (Merge), LC 57(Insert Interval), LC 252, LC 352 (Data Stream as Disjoint Intervals), LC 436, LC 729, LC 759, LC 986 (Interval List Intersections), LC 1024, LC 1156, LC 1288, LC 1272 (Remove Interval)
  * Nested List: LC 341 (Flatten Iterator), LC 339 (Nested List Weight Sum), LC 364 (Nested List Weight Sum II)
  * Skiplist: LC 1206 (Design Skiplist)
  * Cartesian Tree:
    * Construction: LC 654 (Maximum Binary Tree)
  * Persistence:
    * Fat Node:
      * Persistent Array: LC 1146
    * Path Copying:
      * Persistent Trie: LC 1938
      * Persistent/Immutable Stack: LC 78, LC 2096
  * Venice Technique: LC 1381 (Design a Stack With Increment Operation), LC 1530, LC 1622 (Sequence with Add-All and Multiply-All Operations)
  * MEX Query:
    * Complement Set: LC 2003
15. Dynamic Programming: LC 17, LC 77, LC 91, LC 96, LC 97, LC 115, LC 132 (Palindrome Factorization), LC 139-140, LC 221, LC 264, LC 301, LC 313, LC 322, LC 338, LC 343, LC 357, LC 368, LC 396, LC 397, LC 403, LC 420, LC 639, LC 714, LC 718, LC 746, LC 790, LC 823, LC 903, LC 920, LC 940, LC 975, LC 1000, LC 1024, LC 1027 (Longest Arithmetic Subsequence), LC 1043, LC 1220, LC 1240, LC 1277, LC 1335 (Sol 1), LC 1359, LC 1425, LC 1444, LC 1692, LC 1866, LC 1997, LC 2400, LC 2501
  * Prefix/Suffix State Space: LC 276, LC 801, LC 838, LC 983, LC 1105, LC 1320, LC 1406, LC 1416, LC 1937, LC 2361
  * Subarray State Space: LC 87, LC 877, LC 1246, LC 1849
  * Bottom-Up: LC 120, LC 241, LC 764, LC 1269, LC 1824, LC 2361
  * Merging Intervals Pattern: LC 1130 (Minimum Cost Tree From Leaf Values)
  * DP with Grid: LC 62, LC 63, LC 64, LC 174, LC 562, LC 741, LC 750, LC 764, LC 931, LC 1463
  * DP with Extra Parameters: LC 188 (Best Time to Buy and Sell Stock IV), LC 256 (Paint House), LC 265 (Paint House II), LC 309 (Best Time to Buy and Sell Stock with Cooldown), LC 518, LC 546, LC 552, LC 689, LC 801, LC 935, LC 1007, LC 1049, LC 1824, Abbreviation (HR)
  * DP on Tree: LC 120, LC 333 (Largest BST Subtree), LC 337, LC 549, LC 968, LC 979, LC 1026, LC 1048, LC 1273, LC 1339, LC 1372, LC 1373, LC 1376
    * In-Out DP/Pivot DP: LC 687, LC 1245 (Binary Tree Diameter), LC 1522 (N-Ary Tree Diameter), LC 2246
    * Tree-Rerooting DP: LC 663 (Equal Tree Partition), LC 834 (Sum of Distances in Tree)
    * Binary Lifting: LC 1483 (Kth Ancestor), LC 1724
  * DP on DAG: LC 851, LC 1136 (Longest Path in DAG), LC 1786, LC 1857, LC 1928
  * Bit Mask/Bit Set: LC 351, LC 473, LC 698, LC 805, LC 943 (Shortest Superstring), LC 1066, LC 1125, LC 2376
    * Profile: LC 1411
    * Broken Profile: LC 1349
  * Digit DP: LC 600, LC 738, LC 788, LC 902, LC 967, LC 1641, LC 2376
  * DP over Divisors: LC 1025 (Solution 2)
  * Lexicographical Configuration: LC 60 (Find the kth permutation)
  * Jumping: LC 32
  * Combine with BS: LC 410 (Sol 1), LC 887 (Egg Drop)
  * Change of State Variable: LC 1218
  * Longest Common Subsequence (LCS): LC 72 (Levenshtein), LC 583, LC 1035, LC 1092 (Shortest Common Supersequence), LC 1143 (LCS), LC 1312 (Minimum Insertion Steps to Make a String Palindrome), LC 1458 (Max Dot Product of Two Subsequences), Longest Common Subsequence Again (HackerEarth, LCS with Modifications)
  * Max Contiguous Array: LC 53 (Kadane's Algorithm), LC 121, LC 123 (Best Time to Buy and Sell Stock III), LC 918
  * Longest Increasing Subsequence (LIS)/Distance to Monotonicity/Patience Sort: LC 300, LC 354, LC 1671 (Distance to Bitonicity/Longest Bitonic Subsequence)
  * Probability: LC 688, CSES Dice Probability
    * Indicator Variable Trick: CSES Inversion Probability
  * Knapsack: 0 - 1 Knapsack Problem (GFG), LC 474, LC 494, LC 1155, LC 1223, LC 1774
    * Unbounded Knapsack/Coin Change: LC 377, LC 518
    * Vector Subset Sum: LC 691
  * Minimax DP: LC 294, LC 375, LC 464, LC 486, LC 877, LC 1406, LC 1510
  * Distance Transform:
    * L1 Distance, 2D: LC 542, LC 1162
  * Knuth-Yao Optimization: LC 1547
  * Divide and Conquer Optimization: LC 1478 (1D p-Median Problem)
  * Lagrangian Relaxation/WQS Binary Search/Alien Trick: LC 188, LC 1751
  * Memoizing Immutable Data Structure: LC 95 (Unique BSTs II), LC 241, LC 894 (Full Binary Trees)
  * Other Notable Problems: LC 10 (Regex Matching), LC 22 (Generate Parentheses), LC 416 (Partition Equal Subset Sum), LC 418 (Sentence Screen Fitting), LC 629 (K Inverse Pairs Array), Matrix Chain Multiplication (GFG), Optimal BST (GFG), LC 887 (Egg Drop), LC 1039 (Minimum Score Triangulation of Polygon), LC 1216 (Longest Palindromic Subsequence), LC 1235 (Weighted Job Scheduling), LC 1751 (Weighted Interval Scheduling, At Most K Intervals), Knuth's Text Justification/Word Wrap (GFG)
16. String: LC 3, LC 58, LC 115, LC 161, LC 316, LC 340 (Longest Substring with At Most K Distinct Characters), LC 345, LC 387, LC 392, LC 438, LC 482, LC 520, LC 551, LC 709 (To Lower Case), LC 722, LC 804, LC 824, LC 833, LC 844, LC 859, LC 916, LC 929, LC 1071, LC 1078, LC 1108, LC 1181 (Before and After Puzzle), LC 1271, LC 1662
  * Basic Operations: LC 151, LC 157 (Read N Characters Given Read4), LC 186, LC 271 (Encode and Decode Strings - Chunked Transfer Encoding), LC 344 (Reverse), LC 557, LC 1112 (Remove Vowels), LC 1427 (String Shift)
  * Longest Prefix Suffix: LC 459
  * Search: LC 616 (Sol 1)
    * Aho-Corasick Automaton: LC 616 (Sol 2)
    * NFA: LC 44 (Wild Card Matching)
    * Knuth-Morris-Pratt (KMP): LC 28, LC 796, LC 1367 (Linked List in Binary Tree), LC 1392 (Longest Proper Prefix That Is Also Suffix)
    * Regex: LC 10, LC 44 (Wild Card Matching), LC 65 (Valid Number), LC 468 (Validate IP Address), LC 609 (Find Duplicate File in System), LC 819, LC 831, LC 1592
    * Dictionary of Patterns: LC 1554
  * Palindrome: LC 14 (Longest Common Prefix), LC 125 (Valid Palindrome), LC 131 (Palindrome Partitioning), LC 132 (Palindrome Factorization), LC 409, LC 680 (Valid Palindrome II), LC 1216 (Valid Palindrome III), LC 1312 (Minimum Insertion Steps to Make a String Palindrome), LC 1332 (Remove Palindromic Subsequences)
    * Manacher's Algorithm: LC 5 (Longest Palindrome Substring), LC 214 (Shortest Palindrome), LC 647 (Count Palindromic Substrings)
  * Metric: LC 72 (Levenshtein Distance)
  * Parentheses:  LC 20, LC 394, LC 678, LC 856, LC 921, LC 1021, LC 1541, LC 1614
  * Suffix Array: LC 1163
  * Inverted Index: LC 525, LC 546, LC 609 (Find Duplicate File in System), LC 791 (Custom Sort String), LC 821, LC 839, LC 1055 (Sol 1), LC 1165, LC 2135
    * Inverted Index of Suffix/Prefix; Next/Previous Letter Pointer: LC 316 (Sol 2), LC 524, LC 546, LC 792, LC 1055 (Sol 2), LC 1081, LC 1180, LC 1216
  * Universal Superstring and de Brujin Graph: LC 753
  * Anagram: LC 1347
    * Magnitude Set: LC 438, LC 567
  * Parsing: LC 394
   * CFG and Predictive Parsing: LC 726, LC 1096
  * Gap Buffer (Character Zipper): LC 2296 (Design Text Editor)
17. Bit Manipulation: LC 89 (Gray Code), LC 137, LC 190 (Reverse Bits), LC 191, LC 231 (Power of Two), LC 342, LC 461 (Hamming Distance), LC 477 (Total Hamming Distance), LC 693, LC 868, LC 1290, LC 1611
  * AND:
    * Checking active bits: LC 393, LC 1342
    * Check/Turn off rightmost set bit (Brian Kernighan's): LC 201, LC 260
    * Find the rightmost bit (`x & ~(x - 1)`): LC 645
  * Bitwise XOR: LC 136-137 (Single Number), LC 260, LC 421 (Maximum XOR of Two Numbers in an Array), LC 1310 (XOR Queries of a Subarray), LC 1506, Introduction to Nim Game (HR)
    * Flip a bit (XOR with 1): LC 476 (Base 10 Complement) = LC 379
  * Bitset/Bitmap: LC 957
  * Concatenation (`<<` then `|`): LC 1680
18. Math: LC 628, LC 670, LC 1016, LC 1041, LC 1217, LC 1317, LC 1551, LC 1785
  * Basic Arithmetic: LC 2, LC 8 (String to Integer (atoi)), LC 12 (Integer to Roman), LC 13 (Roman to Integer), LC 29 (Divide Two Integers), LC 43 (Multiply Strings), LC 50 (Pow(x, n)), LC 66, LC 67 (Add Binary), LC 171, LC 273 (Integer to English Words), LC 279 (Perfect Squares), LC 311 (Sparse Matrix Multiplication), LC 326, LC 372 (Modulo Exponentiation), LC 415 (Add Strings), LC 445, LC 728, LC 1073 (Adding Two Negabinary Numbers), LC 1281, LC 1295, LC 1570 (Dot Product of Two Sparse Vectors)
  * Algebra: LC 458, LC 1276 (Number of Burgers with No Waste of Ingredients)
    * Quadratic Function: LC 360, LC 754 (Solution 2), LC 1103
    * Arithmetic Progression: LC 1103, LC 1228
    * Linear Algebra: LC 867 (Transpose Matrix)
  * BigInteger: LC 78, LC 91, LC 179
  * Fast Matrix Exponentiation: LC 70, LC 509 (Fibonacci Number), LC 1137 (N-th Tribonacci Number)
  * Combinatorics: LC 47 (Permutation II), LC 77 (Combinations), LC 78 (Subsets), LC 118-119 (Pascal's Triangle), LC 456 (132 Pattern), LC 1286 (Iterator for Combination), LC 1359
    * Pigeonhole Principle: LC 523
    * Permutation: LC 31 (Next Permutation), LC 46 (Permutations), LC 526, LC 556, LC 949
    * Principle of Inclusion-Exclusion (PIE): LC 825
    * Binomial Coefficient: LC 2400 (Solution 2)
  * Puzzles: LC 289 (Conway's Game of Life), LC 319
  * Number Theory: LC 204 (Count Primes, Sieve Method), LC 254 (Factor Combinations), LC 258, LC 263, LC 268, LC 365 (Water and Jug), LC 523, LC 633, LC 780, LC 829 (Consecutive Numbers Sum), LC 858, LC 1010, LC 1015, LC 1175, LC 1492, LC 1497
    * Number Systems: LC 166(Fraction to Recurring Decimal)
    * p-adic: LC 172 (Factorial Trailing Zeros; Legendre's Theorem)
    * Primes: O(sqrt(n)) test (HR)
    * Modular multiplicative inverse (Fermat's Theorem): LC 1622 (Sequence with Add-All and Multiply-All Operations), LC 2400 (Solution 2)
    * GCD (Euclidean's Algorithm): LC 914
  * Numeric Method: LC 69 (Sqrt(x) - Newton's Method)
  * Polynomials:
    * FFT: LC 43 (Multiply Strings)
  * Probability: LC 688, Dice Probability (CSES)
19. Geometry: LC 149 (Max Points on a Line), LC 223, LC 356, LC 593 (Valid Square), LC 1232 (Check Straight Line), LC 1266, LC 1344
  * Area (Shoelace Formula): LC 963, LC 1037 (Valid Triangle)
  * Convex Hull (Graham Scan): LC 587,
    * Monotone Chain: LC 644 (Sol 2)
  * Line Sweep: LC 218 (Skyline Problem), LC 759 (Sol 1), LC 850 (Union of Rectangles), LC 1094, LC 1229, LC 1272 (Remove Interval), LC 1353, LC 2271
    * Union of Intervals (Klee's Algorithm): LC 495
    * Angular Sweep: LC 1610
  * Grid: LC 296 (Geometric Median on Grid), LC 573
    * Point Index: LC 2013
20. Two Pointers: LC 3, LC 11, LC 16, LC 26, LC 38, LC 42, LC 56, LC 76, LC 80, LC 142, LC 159, LC 209, LC 228, LC 239, LC 243, LC 245, LC 259, LC 283, LC 334, LC 340 (Longest Substring with At Most K Distinct Characters), LC 360, LC 408, LC 413, LC 424, LC 434, LC 457, LC 484, LC 696, LC 708, LC 713, LC 727, LC 739, LC 763, LC 809, LC 830, LC 845, LC 849, LC 904, LC 905, LC 948, LC 978, LC 1004, LC 1578, LC 1446, LC 1658, LC 1712
  * Condensing Repetition (RLE): LC 546, LC 1287, LC 1541
  * Three Pointers: LC 930 (Sol 2)
21. Ad Hoc: LC 54, LC 667, LC 927, LC 1304, LC 1428, LC 2018
  * Simulation: LC 6, LC 202, LC 253, LC 348 (Design Tic-Tac-Toe), LC 510, LC 573, LC 657, LC 755, LC 799, LC 874, LC 1041, LC 1243, LC 1275, LC 1611, LC 1646, LC 1675, LC 1801, LC 1861
22. Compression Algorithm:
  * RLE: LC 443, LC 604 (Iterator),LC 809, LC 900 (Iterator), LC 925, LC 1313 (Decompress), LC 1541, LC 1868 (Dot Product)
  * Huffman: Decoding (HR)
23. Randomized Algorithm: LC 384 (Shuffle an array, Fisher-Yates Algorithm), LC 398, LC 497 (Random Point in Non-overlapping Rectangles), LC 528 (Random Pick with Weight), LC 710 (Random Pick with Blacklist), LC 1157 (Sol 2)
  * Reservoir Sampling: LC 382
  * Rejection Sampling: LC 470, LC 478
  * Inverse Transform Sampling: LC 478 (Sol 2)
24. Approximation Algorithm:
  * Approximate Set Membership (Bloom Filter): LC 287 (Sol 2)
25. Game: LC 1025
  * Minimax: LC 292, LC 375, LC 464, LC 843, LC 877, LC 1406, LC 1510
  * Nim: LC 1908 (Game of Nim), Introduction to Nim Game (HR)
26. Parallelism and Concurrency:
  * Locks: LC 1114, LC 1115, LC 1116, LC 1195, LC 1242 (Web Crawler Multithreaded)
    * Guarded Suspension: LC 1279
  * Reentrant Locks: LC 1188 (Design Bounded Blocking Queue)
  * Condition Variables: LC 1114, LC 1115, LC 1116, LC 1188 (Design Bounded Blocking Queue), LC 1195
  * Deadlock Resolution:
    * Resource Hierarchy: LC 1226 (The Dining Philosophers)
  * Semaphore: LC 1117
  * Barrier: LC 1117
  * MapReduce Paradigm: LintCode 499 (Word Count), LintCode 504 (Inverted Index), LintCode 537 (N-Gram)
27. Datetime: LC 539 (Minimum Time Difference), LC 681 (Next Closest Time), LC 949 (Largest Time for Given Digits), LC 1360 (Number of Days Between Two Dates), LC 1604, LC 2162
28. Stream: LC 295 (Find Median from Data Stream), LC 346 (Moving Average from Data Stream), LC 352 (Data Stream as Disjoint Intervals), LC 703 (Kth Largest Element in a Stream), LintCode 960 (First Unique Number in Data Stream)
  * Frequency Estimator:
    * Count-min Sketch: LC 229
  * Sliding Window/Batch Operations: LC 239 (Sliding Window Maximum), LC 480 (Sliding Window Median), LC 1425
    * Sliding Window Top K: LC 1383
29. Design Question: LC 288 (Unique Word Abbreviation), LC 355 (Twitter), LC 379 (Phone Directory), LC 631 (Excel Sum Formula), LC 635 (Log Storage System), LC 677 (Map Sum Pairs), LC 911, LC 1166 (File System), LC 1244 (Leaderboard), LC 1348 (Tweet Count per Frequency), LC 1357 (Apply Discount Every n Orders), LC 1472 (Browser History), LC 1500 (File Sharing System), LC 1797 (Authentication Manager), LC 2296 (Text Editor), LC 2424 (Longest Uploaded Prefix), LC 2502 (Memory Allocator)
30. Functional Programming Style: LC 848, LC 1859
