import streamlit as st
import pandas as pd
import random

def main():
    st.title('Name and Winning Number')

    # Get the winning number, whether chosen or randomly generated
    choose_winning_number = st.checkbox('I want to choose the winning number')
    if choose_winning_number:
        st.session_state.winning_number = st.number_input('Enter the winning number (between 0 and 7500):', min_value=0, max_value=7500, value=0)
    else :
        if 'winning_number' not in st.session_state:
            st.session_state.winning_number = random.randint(0, 7500)
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"The randomly selected winning number is: {st.session_state.winning_number}")
        with col2:
            generate_winning_number = st.button('Random winning number')
        if generate_winning_number:
            st.session_state.winning_number = random.randint(0, 7500)

    # Let the user enter names
    names_string = st.text_area("Enter names, one per line. Add an asterisk (*) after the winning name:", height=150)
    
    # When the button is clicked to generate the CSV...
    generate_button = st.button('Generate CSV')
    if generate_button and names_string:
        # Process the entered names
        names_list = [name.strip() for name in names_string.split('\n') if name.strip() != '']

        # Generate random numbers and results; mark the name with an asterisk as the winner
        random_numbers = []
        results = []
        index = -1
        for name in names_list:
            index += 1
            if name.endswith('*'):
                # If the name ends with an asterisk, it's the winner
                names_list[index] = name.rstrip('*')  # Remove asterisk for display
                random_numbers.append(st.session_state.winning_number)
                results.append('Win')
            else:
                # Otherwise, generate a random number and it's a 'Lose'
                random_number = random.randint(0, 7500)
                random_numbers.append(random_number)
                results.append('Lose' if random_number != st.session_state.winning_number else 'Win')  # This covers the very unlikely event the random number matches the winning one
        
        # Prepare the data frame
        data = pd.DataFrame({
            'Name': names_list,
            'RandomNumber': random_numbers,
            'Result': results
        })

        # Download button for the CSV
        st.download_button(
            label="Download CSV",
            data=data.to_csv(index=False).encode('utf-8'),
            file_name='names_winning_numbers.csv',
            mime='text/csv',
        )

if __name__ == '__main__':
    main()
