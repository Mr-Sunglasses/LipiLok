from spello.model import SpellCorrectionModel
import pandas as pd

# df = pd.read_csv('data.csv')

# training_data = [{'source': row['misspelled_text'],
#                   'target': row['correct_text']} for _, row in df.iterrows()]

# print(training_data)

sp = SpellCorrectionModel(language="en")

sp.load(model_path="en_large.pkl")

sp.train(['I want to play cricket', 'Kohli scores another century'])

# Save the trained model for later use
sp.save(model_save_dir="/Users/kanishkpachauri/Desktop/oss/samagra/LipiLok/language_models/en_large.pkl")

# # Your text with a spelling mistake
# text_with_mistake = "I canot beleive this is hapening."

# # Use Spello to correct the spelling
# result = sp.spell_correct(text_with_mistake)

# print(result)

# # Access the corrected text
# corrected_text = result['spell_corrected_text']

# print("Original Text:", text_with_mistake)
# print("Corrected Text:", corrected_text)

# training_data = [
#     {"incorrect": "JavaScript is the Best Programming Language",
#         "correct": "Python is the Best Programming Language"}
# ]

# # Train the model
# sp.train(training_data)

# # Save the trained model for later use
# sp.save()
