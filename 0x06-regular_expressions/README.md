# Regular Expressions

![regex_meme](https://intranet.alxswe.com/images/contents/sysadmin/concepts/29/regex_now_2_problems.jpg)

---
> Some people, when confronted with a problem, think “I know, I’ll use regular expressions.”   Now they have two problems.

**Jamie Zawinski** - American computer programmer and blogger

---


### Okay, what's Regex????

A regular expression, commonly called a **regexp**, or **regex**, is a sequence of characters that define a search pattern.  It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a “find and replace” command). While it is a very powerful tool, it is also very dangerous because of its complexity.

### They Call Them "Common" Uses

* Validating E-mails
* Validating IP Adresses
* Validating Credit Cards
* Validating Phone Numbers
* etc.

### Python Module

```python
import re
```

### Okay Just Get To The Point!

* **.**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Any Character Except New Line
* **\d**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Digit (0-9)
* **\D**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Not a Digit (0-9)
* **\w**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Word Character (a-z, A-Z, 0-9, _)
* **\W**&nbsp;&nbsp;&nbsp;&nbsp;- Not a Word Character
* **\s**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Whitespace (space, tab, newline)
* **\S**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Not Whitespace (space, tab, newline)

* **\b**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Word Boundary (similar to "Is your boundary a WORD?" or even more like "Is it separated by something?")
* **\B**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Not a Word Boundary
* **^**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Beginning of a String
* **$**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- End of a String

* **[]**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Matches Characters in brackets
* **[^ ]**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Matches Characters NOT in brackets
* **|**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Either Or
* **( )**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Group

#### Quantifiers:
* **\***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 0 or More
* **\+**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 1 or More
* **?**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 0 or One (Optional)
* **{3}**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Exact Number
* **{3,4}**&nbsp;&nbsp;&nbsp;&nbsp;- Range of Numbers (Minimum, Maximum)

