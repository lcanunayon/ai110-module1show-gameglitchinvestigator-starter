# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

-The game looked really simple when i first ran it, and pretty clean. Two concrete bugs I noticed were easy being the 2nd hardest difficulty with only 6 guesses, and the wrong hint every time saying go lower, even if I had to go higher. Also, the game would be over even though i had some attempts left.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude AI

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

A AI suggestion that was correct was fixing the diffulty bug by just changing the values of the amount of attempts you get for each classification. I verified this result by fixing the bug which the AI suggested and testing it with test cases and live demo.

An AI suggestion that was misleading was writing test cases over previous test cases that were already there, which gave me test cases that were failing at first but were actually just the preexisting test cases in the repo, which the AI did not tell me about.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I first saw a bug was fixed by the test cases in pytest I wrote, then to really make sure it was fixed I ran the game live in streamlit.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test I ran manually through a live demo was seeing if it was giving me the right hint. At first, it was backwards, which showed me that my code logic was broken and backwards, and immediately had to be fixed.

- Did AI help you design or understand any tests? How?
It did not essentially help me design the tests, but I could under stand the basic nature of it. Making sure that it is giving the expected output for what is put into the input field. The reason I could understand this was its explanation of what the tests were doing and its names.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain that using streamlit session state is logged only onto your computer, so only you can run it on localhost, which is great for testing. When ready to deploy and all functionality is fixed, then we could move from a localhost to a real deploy.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Marking bugs in the code for the AI to go straight into, and making pytest tests to test my code in terminal without always running a live demo.


- What is one thing you would do differently next time you work with AI on a coding task?
I would make sure to let it have full context of the game and the tests that come with it, the backend and everything.


- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project changed the way I thought about AI generated code by not looking at AI as something to replace our thinking, but something to help us pilot the ship.
