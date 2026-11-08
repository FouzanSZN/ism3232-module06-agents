
# Week 10: OOP for Agents

**Author:** Fouzan Haider  
**Course:** ISM3232 - Business Application Development

## Part 1: Chatbot and Tools

This project demonstrates object-oriented programming by using separate classes for an order lookup tool, a stock lookup tool, and a support chatbot. The chatbot receives the lookup tools through its constructor and stores conversation history. It uses simple keyword rules to decide how to respond to customer messages.

## Part 2: Two Chatbots

The `two_bots.py` program creates two chatbot objects named Sunny and River. Both chatbots share the same order and stock lookup tools, but each maintains its own conversation history and instructions.

## Part 3: Mini-Project - Fouzan's Appointment Assistant

Fouzan is a mock appointment assistant that helps customers check available appointment times. Customers can ask about availability on a particular weekday, and the assistant uses an appointment lookup tool to return the available times. If a customer does not specify a day, the assistant asks which day they want to check.

The appointment schedule is mock data stored in a Python dictionary. It does not connect to a real calendar or booking system, and the available times are examples rather than live appointments.

Requests to book or schedule an appointment are passed to the front desk because the assistant cannot confirm or create real bookings. This ensures that a human handles requests that require an actual appointment confirmation.

One risk of using real customer data is exposing private information, such as names, contact details, or appointment records. Real customer information would need to be protected with appropriate security and access controls.

## Files

- `order_tool.py` - Looks up order IDs and order statuses.
- `stock_tool.py` - Looks up product names and stock quantities.
- `chatbot.py` - Contains the SupportChatbot class.
- `main.py` - Runs the support chatbot.
- `two_bots.py` - Demonstrates two chatbot objects sharing tools.
- `exercise1.md` - Answers the OOP concept questions.
- `my_tool.py` - Contains the appointment lookup tool.
- `my_assistant.py` - Contains Fouzan's appointment assistant.
- `my_main.py` - Runs the appointment assistant.
- `tests/` - Contains automated tests for the chatbot and appointment assistant.

## Week 11: Local Model Integration

This project integrates a local Ollama model using the granite4.1:3b model. The model answered general questions well when the instructions provided the necessary information, such as explaining the office schedule. It can also produce incorrect answers when a user provides misleading information, as demonstrated by the store-hours exercise. Important operations such as appointment availability and booking handoffs remain in Python code because they require reliable, verified information and human involvement. The mock model and automated tests allow the project to work without Ollama running.
