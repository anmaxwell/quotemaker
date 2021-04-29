# quotemaker

This is part 1 of a 3 part project to get experience and exposure of using APIs, classification and text generation.

Part 1 is the Quotemaker. This uses pre trained GPT2 to auto generate motivational quotes after being fine tuned on existing quotes. If the generated quote is voted good by the reader, it is pushed to the API and added to the training list. If not it's simply ignored.
(gpt_2_simple has dependencies - run through docker to enable)

For this project I have fine tuned GPT2 using gpt_2_simple and loaded the full model in LFS due to the size. 

Part 2 is the API. The API holds all the quotes and can be updated by adding more quotes from the Quotemaker. Also using streamlit as a way to connect

Part 3 is the Imagemaker. This pulls down a quote and predicts an image from a set using a trained KNN model. If the reader agrees the image matches the quote, this is added to the training list for future training.
