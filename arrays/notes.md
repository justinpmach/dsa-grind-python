## 🧠 Problem: Best Time to Buy and Sell Stock

**LeetCode Link:** [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
**Category:** Arrays, Two Pointers  
**Difficulty:** Easy

---

### ✅ Problem Summary

You’re given a list of stock prices where `prices[i]` is the price on day `i`.  
The goal is to **maximize profit** by choosing one day to **buy** and one day to **sell** after that.  
If no profit is possible, return `0`.

---

### 🧠 Key Insight

Track the **lowest price so far** (`min_price`).  
As you iterate through the array, for each day calculate:

potential_profit = current_price - min_price


Update the `max_profit` if the `potential_profit` is higher.

---

### 🧪 My First Attempt (Incorrect)

Initially, I was comparing the current price to the next day’s price using:

```python
if price - prices[i + 1] >= currentMax:\
```

But this actually checked for the largest drop, not the largest gain.
I realized the goal is to find the lowest price to buy and then the best future price to sell — not compare immediate neighbors.

### ⏱️ Time & Space Complexity

Time: O(n) — Single pass through the array

Space: O(1) — Only two variables (min_price, max_profit)


💡 What I Learned
Always re-read the prompt carefully — this one’s about max gain, not adjacent differences

You don’t always need enumerate() — only use it when index is actually needed

The pattern of tracking a running minimum (or maximum) is common in greedy and sliding window problems