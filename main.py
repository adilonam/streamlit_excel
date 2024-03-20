import streamlit as st
import pandas as pd
import random

def main():
    # Title of the application
    st.title('Name and Winning Number')
    
    # Option to choose a winning number or generate it randomly
    choose_winning_number = st.checkbox('I want to choose the winning number')
    if choose_winning_number:
        winning_number = st.number_input('Enter the winning number (between 0 and 7500):', min_value=0, max_value=7500, value=0)
    else:
        winning_number = random.randint(0, 7500)
        st.write(f"The randomly selected winning number is: {winning_number}")

    # Input text area for user to enter names, height can be adjusted as needed
    names_string = st.text_area("Enter names, one per line:", height=150)
    generate_button = st.button('Generate CSV')

    if generate_button and names_string:
        # Split the string of names into a list using newlines
        names_list = [name.strip() for name in names_string.split('\n') if name.strip() != '']
        
        # Generate a random number for each name and check if it's the winning number
        random_numbers = [random.randint(0, 7500) for _ in names_list]
        results = ['Win' if number == winning_number else 'Lose' for number in random_numbers]
        
        # Create a DataFrame
        data = pd.DataFrame({
            'Name': names_list,
            'RandomNumber': random_numbers,
            'Result': results
        })
        
        # Convert DataFrame to CSV and allow user to download
        st.download_button(
            label="Download CSV",
            data=data.to_csv(index=False).encode('utf-8'),
            file_name='names_winning_numbers.csv',
            mime='text/csv',
        )

if __name__ == '__main__':
    main()
