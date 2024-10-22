import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to draw a heart shape
def draw_heart():
    # Heart shape coordinates
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * (np.sin(t) ** 3)
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    # Create the plot
    plt.figure(figsize=(8, 8))
    plt.fill(x, y, color='red')
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.axis('off')  # Hide axes
    plt.text(-6, 0, 'jahnvi', fontsize=20, fontweight='bold', color='white', ha='center')

    # Save the plot to a file
    plt.savefig('heart.png', bbox_inches='tight', dpi=300, facecolor='black')
    plt.close()

# Streamlit application
st.title("Vishnu Rathod")
st.markdown("<h1 style='text-align: center; color: red;'>❤️</h1>", unsafe_allow_html=True)

# Draw the heart
draw_heart()
# Display the heart image
st.image('heart.png', use_column_width=True)

# Keep the Streamlit app running
st.write("Love you always!")
