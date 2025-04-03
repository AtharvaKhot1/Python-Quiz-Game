# Quiz Game

A command-line quiz application written in Python that lets users test their knowledge in various categories.

# Features

- Multiple quiz categories: Python, General Knowledge, and Sports
- Score tracking system with rewards for correct answers and penalties for wrong ones
- Database integration to save user scores
- JSON-based question management for easy customization

# Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/quiz-game.git
   cd quiz-game
   ```

2. Install required dependencies:
   ```
   pip install mysql-connector-python
   ```

3. Set up the MySQL database:
   ```sql
   CREATE DATABASE quiz_game;
   USE quiz_game;
   CREATE TABLE scores (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       score INT NOT NULL,
       date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

# Configuration

Update the database connection settings in `Quiz.save_score()` method if needed:

```python
mysql.connector.connect(
    host='localhost',
    password='1234', 
    user='root',
    database='quiz_game'
)

# Usage

Run the game:
```
python quiz_game.py
```

Follow the on-screen prompts to:
1. Enter your name
2. Choose a quiz category
3. Answer the questions
4. View your final score

# Customizing Questions

Questions are stored in the `questions.json` file in the following format:

```json
{
  "Category": [
    {
      "prompt": "Question text?\n",
      "answer": ["Acceptable Answer 1", "Alternative Answer"]
    },
    ...
  ]
}
```

To add more questions or categories, simply edit the JSON file following this structure.

# Scoring System

- Each correct answer: +4 points
- Each wrong answer: -1 point

You can customize the scoring system by modifying the `correct_score` and `incorrect_penalty` parameters when creating a `Quiz` instance.

