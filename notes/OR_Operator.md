# Ultimate Python `or`-Operation Guide 🧠🐍🔥

---

**`or` is a** 👉 **short-circuit logical operator** 👈
**But also acts like** 👉 **a value-returning expression**

## 🧾 PYTHON `or` — THE RULES OF THE GAME:

### 🥇 1. `or` returns the **first truthy value** it finds.

```python
x = 0 or "hello"   # 👉 "hello"
x = "" or 123      # 👉 123
```

---

### ❌ 2. If ALL values are falsy, it returns the **last one**.

```python
x = None or 0 or False   # 👉 False
x = [] or {} or ()       # 👉 ()
```

---

### 🧠 3. Python **evaluates left to right**, and stops as soon as it finds something truthy. This is called **short-circuiting**.

```python
x = "hi" or some_function()  # 👉 some_function() is NEVER called
```

---

### 🚨 4. Even if the value is falsy, Python **has to evaluate** it to know that.

So if it’s a function call, the function **will run**.

```python
x = None or spooky()  # 👻 spooky() gets called!
```

---

### 👻 5. Every function on the left of the first truthy one **WILL be called**, and their print side-effects WILL show up.

```python
x = spooky() or spooky()  # BOTH print "👻 Boo!"
```

---

### 🧨 6. Functions on the **right** of a truthy value? **Never get touched**.

```python
x = "truth" or spooky()  # spooky() is IGNORED
```

---

### 🔁 7. You can chain as many `or`s as you want. Python just walks through each until it's satisfied like a buffet line 🍱

```python
x = [] or {} or () or 0 or False or "finally!"  # 👉 "finally!"
```

---

### 🧪 8. `or` returns the **actual value**, NOT just `True`/`False`

```python
x = 0 or 5      # 👉 5
x = False or [] # 👉 []
```

---

## 🔮 THE GOLDEN MANTRA:

> **“or” gives you the first non-garbage it finds. If all are trash, it hands you the last piece of garbage and walks away.**

---
