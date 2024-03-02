import streamlit as st #For UI,  we can use flask as well
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers
from get_llm_response import getLlamaresponse

##Function to get response from LLama 2 model ##


# def getLlamaresponse(input_text, no_words, blog_style):
#     ### Llama 2 model call
#     llm = CTransformers(model = 'models\llama-2-7b-chat.ggmlv3.q8_0.bin',
#                         model_type = 'llama',
#                         config = {'max_new_tokens':256,
#                                   'temperature': 0.01}) #LLM Model created
    
#     ## PROMPT TEMPLATE

#     template = """ 
#     write a blog for {blog_style} job profile for a topic {input_text} with in {no_words} words.
#     """
#     prompt = PromptTemplate(input_variables = ["blog_style", "input_text", "no_words"],
#                             template = template)

#     ## Generate the response form LLama 2 model
#     response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_words= no_words))
#     print(response)
#     return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon=":bar_chart:",
                   layout = 'centered',
                   initial_sidebar_state='collapsed')


     
st.header("Generate Blogs")     

input_text = st.text_input("Enter the Blog Topic") #parameter 1

## creating two more columns for additional 2 fields ###
col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of Words') #parameter 2

with col2:
    blog_style = st.selectbox('Writing the blog for',
                            ('Researchers', 'Data Scientist', 'Data Engineers', 'AI Engineers', 'DevOps Engineer', 'Graduate Students', 'Primary School Students', 'Common People'), index = 0) #parameter 3

submit = st.button("Generate") #button to generate blogs based on inout text

## Finsl Response
if submit:
    st.write(getLlamaresponse(input_text, no_words, blog_style))
