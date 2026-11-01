# Exercise 1: OOP Concepts

**1. What are the class names in this project?**

The class names are `OrderLookup` and `SupportChatbot`.

**2. What objects are created in main.py?**

The objects are `order_tool` and `bot`.

**3. What are all the SupportChatbot attributes?**

The attributes are `self.name`, `self.instructions`, `self.order_tool`, and `self.history`.

**4. What methods belong to OrderLookup?**

The methods are `__init__()`, `find_order_id()`, and `find_status()`.

**5. What line shows composition?**

The line `self.order_tool = order_tool` shows composition because the chatbot stores and uses an OrderLookup object.

**6. What does self mean in bot.respond("hello")?**

`self` refers to the current SupportChatbot object that is calling the method.