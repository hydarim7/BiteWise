# BiteWise

**From pantry chaos to plated perfection—smarter, healthier, waste-wise cooking starts here.**

BiteWise is an AI-powered kitchen assistant that transforms your pantry and fridge contents into personalized, calorie-conscious, and dietary-friendly recipes. Whether you're a busy home cook, a health-conscious eater, or a culinary explorer, BiteWise helps you create delicious meals while minimizing food waste and respecting your dietary preferences, allergies, and cuisine choices.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Problem Statement](#problem-statement)
- [Target Users](#target-users)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)
- [License](#license)

## Overview
BiteWise is a recipe recommendation system that leverages generative AI to suggest meals based on your available ingredients, calorie limits, dietary restrictions, allergies, and preferred cuisines. It supports both manual ingredient input and image uploads for ingredient detection, making meal planning effortless and sustainable.

## Features
- **Ingredient-Based Recipe Suggestions**: Generate recipes using only the ingredients you have, reducing the need for extra shopping.
- **Calorie-Conscious Recommendations**: Filter recipes to meet your specified calorie goals for healthier eating.
- **Dietary Customization & Allergies**: Accommodate dietary preferences (e.g., vegan, keto, gluten-free) and avoid allergens (e.g., nuts, dairy).
- **Global Cuisine Exploration**: Discover recipes from various culinary traditions (e.g., Italian, Mexican, Indian) using your ingredients.
- **Detailed Recipe Information**: Access full preparation instructions and nutritional breakdowns for suggested recipes.
- **Photo & Manual Ingredient Input**: Upload images of your fridge/pantry for AI-powered ingredient detection or manually enter ingredients for flexibility.

## Problem Statement
Many people struggle to cook meals due to limited time, leftover ingredients, and personal constraints like dietary restrictions, allergies, or calorie goals. Scrolling through countless recipes online is time-consuming and inefficient. BiteWise addresses this by:
- Using your pantry as the primary search space.
- Filtering recipes based on calories, allergies, and dietary preferences in one go.
- Delivering quick, clear, and tailored recipe suggestions to save time and reduce waste.

## Target Users
- **Home Cooks**: Create meals with what's already in your kitchen.
- **Health-Conscious Eaters**: Track calories and align with fitness or wellness goals.
- **Diet-Restricted Users**: Follow specific diets or avoid allergens.
- **Culinary Explorers**: Try new global recipes with familiar ingredients.
- **Busy Individuals**: Get quick, simple recipes with minimal prep.
- **Sustainability-Focused Users**: Reduce food waste and use seasonal/local items.

## How It Works
1. **Input Ingredients**:
   - Upload a photo of your fridge/pantry, and BiteWise's computer vision identifies ingredients.
   - Alternatively, manually select or enter ingredients.
2. **Set Preferences**:
   - Specify calorie limits, dietary preferences, allergies, and preferred cuisines.
3. **Get Recipes**:
   - The AI generates a list of recipes tailored to your inputs, including names, ingredients, and estimated calories.
4. **Explore Details**:
   - View preparation instructions, nutritional breakdowns, and waste reduction tips for each recipe.

## Installation
To run BiteWise locally, follow these steps:

### Prerequisites
- Python 3.8+
- Google Cloud account with access to the Gemini API (for AI and vision capabilities)
- Jupyter Notebook or compatible environment

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/bitewise.git
   cd bitewise
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Required packages include:
   - `google-generativeai`
   - `ipywidgets`
   - `Pillow`
   - `typing-extensions`

3. **Set Up API Key**:
   - Obtain a Google Cloud API key for the Gemini API.
   - Set the environment variable:
     ```bash
     export GOOGLE_API_KEY='your-api-key'
     ```

4. **Run the Notebook**:
   ```bash
   jupyter notebook bitewise.ipynb
   ```

## Usage
1. Open the Jupyter Notebook (`bitewise.ipynb`).
2. Run the cells to initialize the environment and load dependencies.
3. Interact with the Food Crafter App interface:
   - Upload an image or manually select pantry items.
   - Specify calorie limits, cuisines, allergies, and dietary preferences.
   - Click "Process" to generate and view recipe suggestions.
4. Explore recipe cards withdetailed instructions and nutritional info.

## Technologies Used
- **Generative AI**:
  - **JSON Mode**: Structured recipe output with standardized fields.
  - **Few-Shot Prompting**: Example-based prompts for relevant, context-aware recipes.
  - **Image Understanding**: Computer vision for ingredient detection from photos.
- **Python Libraries**:
  - `google-generativeai`: Interface with Gemini API.
  - `ipywidgets`: Interactive UI for Jupyter Notebook.
  - `Pillow`: Image processing for uploads.
- **Jupyter Notebook**: Development and testing environment.

## Additional Resources
- **Project Blog Post**: [BiteWise: Revolutionizing Meal Planning](https://medium.com/@srastegarnia/bitewise-revolutionizing-meal-planning-with-your-ai-kitchen-assistant-fa76724b6ce9)
- **Demo Video**: [Watch on YouTube](https://www.youtube.com/watch?v=bUXtz69sTOs&t=7s)

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

Please ensure your code follows the project's style guide and includes tests where applicable.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**BiteWise** is your partner in creating smarter, healthier, and sustainable meals. Start cooking with what you have today!
