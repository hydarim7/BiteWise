def create_food_crafter_app(client):
    """
    Create the interactive image upload widget with enhanced visualization
    Args:
       client 
    """
    
    # Custom CSS for styling with dark mode support
    style = widgets.HTML("""
    <style>
        /* Light mode styles */
        .custom-button { 
            background-color: #4CAF50 !important; 
            color: white !important; 
            border-radius: 8px !important; 
            padding: 15px !important; 
            font-size: 18px !important; 
            min-width: 400px !important; 
            height: 60px !important; 
            display: block !important; 
            margin: 10px auto !important; 
            transition: background-color 0.2s !important; 
        }
        .custom-button:hover { 
            background-color: #45A049 !important; 
        }
        .custom-header { 
            color: #2E7D32 !important; 
            font-family: Arial, sans-serif !important; 
            text-align: center !important; 
        }
        .section-box { 
            border: 1px solid #E0E0E0 !important; 
            padding: 10px !important; 
            border-radius: 8px !important; 
            background-color: #F9F9F9 !important; 
            margin-bottom: 10px !important; 
        }
        .recipe-card { 
            border: 1px solid #B0BEC5 !important; 
            border-radius: 8px !important; 
            padding: 15px !important; 
            margin: 10px !important; 
            background-color: #FFFFFF !important; 
            color: #000000 !important; 
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1) !important; 
            transition: transform 0.2s !important; 
        }
        .recipe-card:hover { 
            transform: scale(1.02) !important; 
        }
        .loading-spinner { 
            text-align: center !important; 
            font-style: italic !important; 
            color: #616161 !important; 
        }
        .widget-label { 
            text-overflow: ellipsis !important; 
            white-space: nowrap !important; 
            overflow: visible !important; 
            min-width: 150px !important; 
            color: #000000 !important; 
        }
        .widget-checkbox .widget-label {
            color: #000000 !important;
        }
        .widget-text, .widget-dropdown {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #B0BEC5 !important;
        }
        .input-message {
            margin-top: 15px !important;
            padding: 10px !important;
            background-color: #e8f5e9 !important;
            border-radius: 8px !important;
            border-left: 4px solid #4CAF50 !important;
            color: #000000 !important;
        }

        /* Dark mode styles */
        @media (prefers-color-scheme: dark) {
            .custom-button {
                background-color: #66BB6A !important;
                color: #FFFFFF !important;
            }
            .custom-button:hover {
                background-color: #81C784 !important;
            }
            .custom-header {
                color: #A5D6A7 !important;
            }
            .section-box {
                background-color: #424242 !important;
                border-color: #616161 !important;
            }
            .recipe-card {
                background-color: #616161 !important;
                color: #E0E0E0 !important;
                border-color: #757575 !important;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.3) !important;
            }
            .loading-spinner {
                color: #B0BEC5 !important;
            }
            .
    </style>
    """)

    # File upload and calorie input
    file_upload = widgets.FileUpload(
        accept='image/*',
        multiple=False,
        description='Upload Fridge Image',
        layout={'width': '400px'}
    )
    calorie_input = widgets.IntText(
        value=500,
        description='Calorie Limit (kcal):',
        layout={'width': '300px'}
    )
    upload_note = widgets.HTML(
        value='<p style="color: #2E7D32; font-style: italic;">Note: If you don’t have an image, you can manually enter your ingredients after the process.</p>'
    )
    upload_section = widgets.VBox([file_upload, calorie_input, upload_note], layout={'margin': '10px'})

    # Pantry items
    pantry_items = [
        'lentils', 'chickpeas', 'rice', 'potatoes', 'pasta', 'quinoa',
        'flour', 'sugar', 'beans', 'oats', 'cornmeal', 'butter', 'oil', 'onion', 'garlic'
    ]
    # Create checkboxes for each pantry item
    pantry_checkboxes = [
        widgets.Checkbox(value=False, description=item, indent=False, layout={'width': '200px'})
        for item in pantry_items
    ]
    # Arrange checkboxes in a grid layout
    pantry_grid = widgets.GridBox(
        pantry_checkboxes,
        layout={'grid_template_columns': 'repeat(3, 200px)'}
    )
    pantry_label = widgets.HTML(value="<b>Select Pantry Items</b>")

    # Manually adding custom pantry items
    custom_pantry_input = widgets.Text(
        value='',
        placeholder='e.g., canned tomatoes, soy sauce',
        description='Custom Pantry Items:',
        layout={'width': '600px'}
    )
    # Combine pantry widgets
    pantry_section = widgets.VBox([pantry_label, pantry_grid, custom_pantry_input], layout={'margin': '10px'})

    
    # Cuisine preferences
    cuisines = ['Italian', 'Chinese', 'Mexican', 'Indian', 'Japanese', 'American', 'Mediterranean']
    # Create checkboxes for each cuisine item
    cuisine_checkboxes = [
        widgets.Checkbox(value=False, description=cuisine, indent=False, layout={'width': '200px'})
        for cuisine in cuisines
    ]
    # Arrange checkboxes in a grid layout
    cuisine_grid = widgets.GridBox(
        cuisine_checkboxes,
        layout={'grid_template_columns': 'repeat(3, 200px)'}
    )
    cuisine_label = widgets.HTML(value="<b>Select Preferred Cuisines</b>")
    cuisine_section = widgets.VBox([cuisine_label, cuisine_grid], layout={'margin': '10px'})

    
    # Allergies list
    allergies = ['Lactose', 'Nuts', 'Shellfish', 'Eggs', 'Soy', 'Fish']
    # Create checkboxes for each allergy
    allergy_checkboxes = [
        widgets.Checkbox(value=False, description=allergy, indent=False, layout={'width': '200px'})
        for allergy in allergies
    ]
    allergy_grid = widgets.GridBox(
        allergy_checkboxes,
        layout={'grid_template_columns': 'repeat(3, 200px)'}
    )
    allergy_label = widgets.HTML(value="<b>Select Allergies</b>")
    # Manually adding custom allergies
    custom_allergy_input = widgets.Text(
        value='',
        placeholder='e.g., sesame, celery',
        description='Other Allergies:',
        layout={'width': '600px'}
    )
    # Combine allergy widgets
    allergy_section = widgets.VBox([allergy_label, allergy_grid, custom_allergy_input], layout={'margin': '10px'})

    
    # Dietary preferences
    diets = ['Vegetarian', 'Vegan', 'Pescatarian', 'Keto', 'Gluten-Free']
    # Create checkboxes for each allergy
    diet_checkboxes = [
        widgets.Checkbox(value=False, description=diet, indent=False, layout={'width': '200px'})
        for diet in diets
    ]
    diet_grid = widgets.GridBox(
        diet_checkboxes,
        layout={'grid_template_columns': 'repeat(3, 200px)'}
    )
    diet_label = widgets.HTML(value="<b>Select Dietary Preferences</b>")
    # Manually adding custom diet
    custom_diets_input = widgets.Text(
        value='',
        placeholder='e.g., Low-Carb, Paleo',
        description='Other Dietary :',
        layout={'width': '600px'}
    )
    # Combine diet widgets
    diet_section = widgets.VBox([diet_label, diet_grid, custom_diets_input], layout={'margin': '10px'})

    # Accordion for input sections
    accordion = widgets.Accordion(children=[
        upload_section,
        pantry_section,
        cuisine_section,
        allergy_section,
        diet_section
    ])
    accordion.set_title(0, 'Image Upload & Calorie Limit')
    accordion.set_title(1, 'Pantry Items')
    accordion.set_title(2, 'Cuisine Preferences')
    accordion.set_title(3, 'Allergies')
    accordion.set_title(4, 'Dietary Preferences')

    # Process button
    process_button = widgets.Button(
        description='Process',
        button_style='',
        tooltip='Click to identify ingredients and suggest recipes',
        layout={'width': '100%', 'margin': '10px auto', 'display': 'block'}
    )
    process_button.add_class('custom-button')

    # Create separate output areas
    image_output = widgets.Output()
    main_output = widgets.Output()

    # Global variable for storing generated recipes
    recipes_json_global = [None]

    def on_button_click(b):
        # Clear only the main output but keep the image output intact
        main_output.clear_output()
        image_output.clear_output()
        
        all_ingredients = []

        # Check if an image is uploaded
        if file_upload.value:
            with image_output:
                uploaded_file_info = file_upload.value[0]
                image_bytes = uploaded_file_info['content']
                display(Markdown("### Uploaded Fridge Image"))
                display(display_image(image_bytes))
            
            # Process the image and extract ingredients
            with main_output:
                display(widgets.HTML('<div class="loading-spinner">Processing image ingredients...</div>'))
                try:
                    image_ingredients = identify_ingredients_from_image(client, image_bytes)
                    all_ingredients.extend(image_ingredients)
                    main_output.clear_output()
                    display(Markdown("### Ingredients from Image"))
                    for i, ingredient in enumerate(image_ingredients, 1):
                        print(f"{i}. {ingredient}")
                    
                    # Create a button to allow adding manual ingredients
                    add_ingredients_button = widgets.Button(
                        description='Add Manual Ingredients',
                        button_style='',
                        tooltip='Click to add more ingredients manually',
                        layout={'width': 'auto', 'margin': '10px'}
                    )
                    add_ingredients_button.add_class('custom-button')
                    
                    # Output area for additional manual input
                    additional_input_output = widgets.Output()
                    
                    def on_add_ingredients_clicked(b):
                        """
                        Handle click on "Add Manual Ingredients" button:
                        - Display a text field for the user to enter missing ingredients.
                        - Show a button to submit and add those ingredients.
                        """
                        with additional_input_output:
                            additional_input_output.clear_output()
                            display(widgets.HTML(
                                value='<div class="input-message"><b>If anything’s missing or not recognized, feel free to add it yourself!</b><br>Just enter your ingredients below, separated by commas (for example: tomatoes, spinach, chicken):</div>'
                            ))
                            additional_input = widgets.Text(
                                value='',
                                placeholder='e.g., mozzarella balls, orange bell pepper, spinach',
                                description='',
                                layout={'width': '600px'}
                            )
                            submit_additional_button = widgets.Button(
                                description='Submit Additional Ingredients',
                                button_style='',
                                layout={'width': 'auto', 'margin': '10px'}
                            )
                            submit_additional_button.add_class('custom-button')
                            
                            def on_submit_additional_clicked(b):
                                """Handle adding manual ingredients"""
                                with additional_input_output:
                                    additional_input_output.clear_output()
                                    if additional_input.value.strip():
                                        new_ingredients = [item.strip() for item in additional_input.value.split(',') if item.strip()]
                                        all_ingredients.extend(new_ingredients)
                                        display(Markdown("### Additional Ingredients Added"))
                                        for i, item in enumerate(new_ingredients, 1):
                                            print(f"{i}. {item}")
                                    # Proceed to process all ingredients
                                    process_all_ingredients(all_ingredients)
                            
                            submit_additional_button.on_click(on_submit_additional_clicked)
                            display(additional_input, submit_additional_button)
                    
                    add_ingredients_button.on_click(on_add_ingredients_clicked)
                    display(add_ingredients_button, additional_input_output)
                
                except Exception as e:
                    main_output.clear_output()
                    print(f"Error identifying image ingredients: {str(e)}")
                    return
        
        else:
            # No image uploaded, prompt for manual ingredient input
            with main_output:
                display(widgets.HTML(
                    value='<div class="input-message"><b>No image? No problem!</b><br>Just enter your ingredients below, separated by commas (for example: tomatoes, spinach, chicken):</div>'
                ))
                manual_input = widgets.Text(
                    value='',
                    placeholder='e.g., tomatoes, spinach, chicken',
                    description='Ingredients:',
                    layout={'width': '600px'}
                )
                submit_manual_button = widgets.Button(
                    description='Submit Manual Ingredients',
                    button_style='',
                    layout={'width': 'auto', 'margin': '10px'}
                )
                submit_manual_button.add_class('custom-button')
                manual_input_output = widgets.Output()
                
                def on_submit_manual_clicked(b):
                    """Handle adding manual ingredients: update list, display entries, and proceed."""
                    with manual_input_output:
                        manual_input_output.clear_output()
                        if manual_input.value.strip():
                            manual_ingredients = [item.strip() for item in manual_input.value.split(',') if item.strip()]
                            all_ingredients.extend(manual_ingredients)
                            display(Markdown("### Manually Entered Ingredients"))
                            for i, item in enumerate(manual_ingredients, 1):
                                print(f"{i}. {item}")
                            # Proceed to process all ingredients
                            process_all_ingredients(all_ingredients)
                        else:
                            # Allow proceeding with pantry items even if no manual ingredients are entered
                            process_all_ingredients(all_ingredients)
                
                submit_manual_button.on_click(on_submit_manual_clicked)
                display(manual_input, submit_manual_button, manual_input_output)

    def process_all_ingredients(all_ingredients):
        """
        Gather and display all user-provided ingredients and preferences, then generate and show recipe suggestions.
        - Add selected pantry and any custom pantry items to `all_ingredients`, displaying each.
        - Display chosen cuisines, allergies/intolerances, and dietary preferences.
        - If no ingredients are available, prompt the user and exit.
        - Fetch recipe suggestions under the calorie limit, show structured JSON and render recipe cards.
        - Provide controls to select a recipe and fetch detailed preparation steps.
        """
        with main_output:
            # Collect pantry items
            pantry_selected = [cb.description for cb in pantry_checkboxes if cb.value]
            if pantry_selected:
                all_ingredients.extend(pantry_selected)
                display(Markdown("### Pantry Items Selected"))
                for i, item in enumerate(pantry_selected, 1):
                    print(f"{i}. {item}")

            custom_pantry_items = []
            if custom_pantry_input.value.strip():
                custom_pantry_items = [item.strip() for item in custom_pantry_input.value.split(',') if item.strip()]
                all_ingredients.extend(custom_pantry_items)
                if custom_pantry_items:
                    display(Markdown("### Custom Pantry Items Added"))
                    for i, item in enumerate(custom_pantry_items, 1):
                        print(f"{i}. {item}")

            # Collect cuisines, allergies, and diets
            selected_cuisines = [cb.description for cb in cuisine_checkboxes if cb.value]
            if selected_cuisines:
                display(Markdown("### Selected Cuisines"))
                for i, cuisine in enumerate(selected_cuisines, 1):
                    print(f"{i}. {cuisine}")
            else:
                selected_cuisines = None

            selected_allergies = [cb.description for cb in allergy_checkboxes if cb.value]
            if custom_allergy_input.value.strip():
                custom_allergies = [allergy.strip() for allergy in custom_allergy_input.value.split(',') if allergy.strip()]
                selected_allergies.extend(custom_allergies)
            if selected_allergies:
                display(Markdown("### Allergies/Intolerances"))
                for i, allergy in enumerate(selected_allergies, 1):
                    print(f"{i}. {allergy}")

            selected_diets = [cb.description for cb in diet_checkboxes if cb.value]
            if custom_diets_input.value.strip():
                custom_diets = [diet.strip() for diet in custom_diets_input.value.split(',') if diet.strip()]
                selected_diets.extend(custom_diets)
            if selected_diets:
                display(Markdown("### Dietary Preferences"))
                for i, diet in enumerate(selected_diets, 1):
                    print(f"{i}. {diet}")

            # Check if all_ingredients is empty after adding pantry items
            if not all_ingredients:
                print("No ingredients provided. Please upload an image, select pantry items, or enter custom ingredients.")
                return

            calorie_limit = calorie_input.value
            display(Markdown(f"### Recipe Suggestions (max {calorie_limit} calories)"))
            display(widgets.HTML('<div class="loading-spinner">Generating recipe suggestions...</div>'))
            try:
                recipes_json_global[0] = suggest_recipes_from_ingredients(
                    client, all_ingredients, calorie_limit, selected_cuisines, selected_allergies, selected_diets
                )
                display(Markdown("### Structured Recipe Output"))
                display(Markdown(f"```json\n{recipes_json_global[0]}\n```"))

                try:
                    suggested_recipes = json.loads(recipes_json_global[0])['recipes']
                    #print(f"show **{recipe}")#delete
                    if suggested_recipes:
                        # Display recipes as cards
                        recipe_cards = []
                        for recipe in suggested_recipes:
                            card = widgets.HTML(f"""
                            <div class="recipe-card">
                                <h3>{recipe['name']}</h3>
                                <p><b>Ingredients:</b> {', '.join(recipe['ingredients'])}</p>
                                <p><b>Calories:</b> {recipe['estimated_calories']} kcal</p>
                            </div>
                            """)
                            recipe_cards.append(card)
                        display(widgets.VBox(recipe_cards))

                        # Recipe selection for details
                        recipe_options = [recipe['name'] for recipe in suggested_recipes]
                        select_recipe_label = widgets.Label("Select a recipe to see details:")
                        recipe_selection = widgets.Dropdown(
                            options=recipe_options,
                            description='Choose Recipe:',
                            disabled=False
                        )
                        show_details_button = widgets.Button(
                            description="Show Recipe Details",
                            button_style='',
                            layout={'width': 'auto'}
                        )
                        show_details_button.add_class('custom-button')
                        details_output = widgets.Output()

                        def on_show_details_clicked(b):
                            """Show detailed information for the selected recipe"""
                            with details_output:
                                details_output.clear_output()
                                selected_name = recipe_selection.value
                                for recipe in suggested_recipes:
                                    if recipe['name'] == selected_name:
                                        display(Markdown(f"### Detailed Information for: **{recipe['name']}**"))
                                        display(Markdown("**Ingredients:**"))
                                        print("- " + "\n- ".join(recipe['ingredients']))
                                        display(Markdown(f"**Estimated Calories:** {recipe['estimated_calories']}"))

                                        
                                        # Prepare a prompt for more details
                                        cuisines_text = ', '.join(selected_cuisines) if selected_cuisines else 'any'
                                        allergies_text = ', '.join(selected_allergies) if selected_allergies else 'none'
                                        diets_text = ', '.join(selected_diets) if selected_diets else 'none'

                                        
                                        prompt = f"""Provide a more detailed description and potential preparation steps for the recipe: '{selected_name}'.
                                        Consider the following constraints:
                                        - Calorie Limit: {recipe['estimated_calories']} kcal
                                        - Preferred cuisines: {cuisines_text}
                                        - Allergies to avoid: {allergies_text}
                                        - Dietary preferences: {diets_text}
                                        - Only consider these Ingredients: {recipe['ingredients']}
                                        Assume the user has common spices available (e.g., salt, black pepper, red pepper, garlic powder, onion powder,paprika,basic herbs).

                                        Include these EXACT sections:

                                        **INGREDIENTS:**
                                        - Only list ingredients that were provided by the user.
                                        - Standard measurements
                                        - Include precise quantities (e.g., 1/2 cup, 2 tablespoons, 1 tsp).

                                        **INSTRUCTIONS:**
                                        - Numbered steps
                                        - Cooking times

                                        **WASTE REDUCTION:**
                                        - Specific actionable tips

                                        **NUTRITION:**
                                        - Per serving
                                        - Key nutrients
                                        
                                        **PERSONALIZATION NOTES:**
                                        - Briefly explain how this recipe aligns with the user's selected cuisines, allergies, and dietary preferences, based ONLY on the information provided.

                                        """    
                                        
                                        display(widgets.HTML('<div class="loading-spinner">Fetching details...</div>'))
                                        try:
                                            response = client.generate_content(
                                                contents=[{"parts": [{"text": prompt}]}]
                                            )
                                            details_output.clear_output()
                                            display(Markdown("**More Details:**"))
                                            print(response.text.strip())
                                        except Exception as e:
                                            details_output.clear_output()
                                            print(f"Error fetching detailed recipe information: {e}")
                                        return
                                display(Markdown("Recipe details not found."))

                        show_details_button.on_click(on_show_details_clicked)

                        display(select_recipe_label, recipe_selection, show_details_button, details_output)

                    else:
                        print("No recipes found in the suggestions to select from.")

                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error processing recipe suggestions for selection: {e}")

            except Exception as e:
                print(f"Error generating recipes: {str(e)}")

    process_button.on_click(on_button_click)

    # App layout with separate image and main output areas
    header = widgets.HTML(value='<h1 class="custom-header">Waste and Calorie Wise Food Crafter</h1>')
    description = widgets.HTML(value='<p style="color: #008000; font-weight: bold;">Upload an image of your fridge (or manually enter everything), select pantry items, choose cuisines, specify allergies and diets, and get tailored recipe suggestions.</p>')

    app = widgets.VBox([
        style,
        header,
        description,
        widgets.HTML('<div class="section-box">'),
        accordion,
        process_button,
        widgets.HTML('</div>'),
        image_output,
        main_output
    ])

    return app
