from anytree import Node

# LEVELS:
# root: book;
book = Node("book")

# book-children level: chapter_1, chapter_2, text_8;
text_8 = Node("...", book)
chapter_1 = Node("chapter", book)
chapter_2 = Node("chapter", book)

# chapter-children level: paragraph_1, paragraph_2, paragraph_3, text_7:
paragraph_1 = Node("paragraph", chapter_1)
paragraph_2 = Node("paragraph", chapter_1)
paragraph_3 = Node("paragraph", chapter_1)
text_7 = Node("...", chapter_2)

# paragraph-children level: text_1, quotation_1, text_3, quotation_2, text_5, text_6;
text_1 = Node("Alice was beginning to get very tired of sitting by "
"her sister on the bank, and of having nothing to do: "
"once or twice she had peeped into the book her sister "
"was reading, but it had no pictures or conversations "
"in it, ", paragraph_1)
quotation_1 = Node("quotation", paragraph_1)
text_3 = Node(" thought Alice, ", paragraph_1)
quotation_2 = Node("quotation", paragraph_1)
text_5 = Node("So she was considering in her own mind, (as well as "
"she could, for the hot day made her feel very sleepy "
"and stupid,) whether the pleasure of making a "
"daisy-chain would be worth the trouble of getting up "
"and picking the daisies, when suddenly a white rabbit "
"with pink eyes ran close by her.", paragraph_2)
text_6 = Node("...", paragraph_3)

# quotation-children level: text_2, text_4;
text_2 = Node("“and what is the use of a book,”", quotation_1)
text_4 = Node("“without pictures or conversations?”", quotation_2)
