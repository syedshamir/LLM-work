from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLlamaresponse(input_text, no_words, blog_style):
    ### Llama 2 model call
    llm = CTransformers(model = 'models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens':256,
                                  'temperature': 0.01}) #LLM Model created
    
    ## PROMPT TEMPLATE

    template = """ 
    write a blog for {blog_style} job profile for a topic {input_text} with in {no_words} words.
    """
    prompt = PromptTemplate(input_variables = ["blog_style", "input_text", "no_words"],
                            template = template)

    ## Generate the response form LLama 2 model
    response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_words= no_words))
    print(response)
    return response