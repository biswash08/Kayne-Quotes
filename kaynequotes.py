import flet as ft
import requests


def main(page: ft.Page):

    page.title = "Kanye Says...."
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 10

    # Function to fetch a new Kanye quote
    def quote(e):
        response = requests.get(url="http://api.kanye.rest/")
        response.raise_for_status()
        data = response.json()
        quotes = data["quote"]
        stack.width=500
        stack.height=500
        stack.alignment=ft.alignment.center
        textquote.value = quotes  # Updating the textquote value with the API response
        page.update()

    # The text control to show Kanye quotes
    textquote = ft.Text(
        value="", 
        size=20,  # Adjust font size if needed
        color="white", 
        weight=ft.FontWeight.BOLD,
        text_align="center",  # Center the text inside the container
        max_lines=5,  # Ensure multiline text within the container
        )

    stack = ft.Stack(
        [
            ft.Image(
                src="background.png",  # Replace with your image URL or local path
                fit=ft.ImageFit.CONTAIN  # Ensures the whole image is shown without cropping
            ),
            ft.Container(
                content=textquote,  # Directly place the textquote here
                alignment=ft.alignment.center,  # Centers the text inside the image
                bgcolor="#00000088",  # Optional: Add a transparent background behind the text
                padding=ft.padding.all(10),  # Add some padding to avoid touching the edges
                width=300,  # Adjust width to fit the image
                height=50,  # Adjust height as needed
            ),
        ],
        width=300,  # Match the width with the image
        height=150  # Match the height with the image
    )

    # Button to trigger the quote fetching
    button = ft.GestureDetector(
        on_tap=quote,
        content=ft.Image(
            src="kanye.png",  # Replace with your image URL or local path
            width=150,
            height=150
        ),
    )

    # Add the stack and button to the page
    page.add(stack, button)


ft.app(target=main)
