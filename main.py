
import streamlit as st
introduction= """OpenAI DALL-E is a simple decoder-only transformer that receives both the text and the image as a single stream of 1280 tokens—256 for the text and 1024 for the image—and models all of them autoregressively². It can create original, realistic images and art from a text description by combining concepts, attributes, and styles¹. 

Here's a brief information about OpenAI DALL-E:

### What is OpenAI DALL-E?
OpenAI DALL-E is an artificial intelligence program that can create original, realistic images and art from a text description by combining concepts, attributes, and styles¹.

### How does OpenAI DALL-E work?
OpenAI DALL-E is a simple decoder-only transformer that receives both the text and the image as a single stream of 1280 tokens—256 for the text and 1024 for the image—and models all of them autoregressively².

### What can OpenAI DALL-E do?
OpenAI DALL-E can create original, realistic images and art from a text description by combining concepts, attributes, and styles¹. It can also make realistic edits to existing images from a natural language caption by adding and removing elements while taking shadows, reflections, and textures into account³.

I hope this helps! Let me know if you have any other questions.

### What is OpenAI DALL-E?
- An artificial intelligence program that can create original, realistic images and art from a text description by combining concepts, attributes, and styles.

### How does OpenAI DALL-E work?
- A simple decoder-only transformer that receives both the text and the image as a single stream of 1280 tokens—256 for the text and 1024 for the image—and models all of them autoregressively.

### What can OpenAI DALL-E do?
- Create original, realistic images and art from a text description by combining concepts, attributes, and styles.
- Make realistic edits to existing images from a natural language caption by adding and removing elements while taking shadows, reflections, and textures into account.



Source: Conversation with Bing, 5/9/2023\n
- (1) DALL·E: Creating images from text - OpenAI. https://openai.com/research/dall-e.\n
- (2) DALL·E 2 - OpenAI. https://openai.com/product/dall-e-2.\n
- (3) DALL·E - OpenAI. https://labs.openai.com/.\n
"""

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Page 1", "Page 2", "Page 3", "Page 4"])
    
    if page == "Page 1":
        st.title("OpenAI DALL·E")
        st.markdown(introduction)
        
    elif page == "Page 2":
        st.title("OpenAI DALL·E Image Generation")
        st.info("""#### NOTE: you can download image by \
                  right clicking on the image and select save image as option""")

        
    elif page == "Page 3":
        st.title("OpenAI DALL·E Image Variation")
        st.info("""#### NOTE: you can download image by \
                  right clicking on the image and select save image as option""")

        
    elif page == "Page 4":
        st.title("OpenAI DALL·E Image Editing")
        st.info("""#### NOTE: you can download image by \
                  right clicking on the image and select save image as option""")


if __name__ == "__main__":
    main()
