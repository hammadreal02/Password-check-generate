# Password Generator & Strength Meter

A Python-based web application built with Streamlit that helps users generate secure passwords and check password strength.

## Features

### 1. Password Generator
- Generate random passwords with customizable length (8-32 characters)
- Options to include:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Visual feedback with loading animation
- Secure random generation using Python's random module

### 2. Password Strength Meter
- Check the strength of any password
- Provides detailed feedback and suggestions for improvement
- Evaluates multiple security criteria:
  - Minimum length requirement (6+ characters)
  - Presence of uppercase letters
  - Presence of lowercase letters
  - Presence of numbers
  - Presence of special characters
- Categorizes passwords as:
  - Strong
  - Medium
  - Weak

## How to Use

1. **Password Generation:**
   - Select desired password length using the slider
   - Choose character types using checkboxes
   - Click "Generate" to create a new password
   - Copy the generated password for use

2. **Password Strength Check:**
   - Enter any password in the text input field
   - Click "Check Strength" to analyze
   - Review strength rating and suggestions
   - Follow recommendations to improve password security

## Technical Requirements
- Python 3.x
- Streamlit
- Required Python packages:
  - string
  - random
  - time
  - re

## Developer
Developed by Hammad Iqbal

