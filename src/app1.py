import modelbit
import pandas as pd
import gradio as gr

def recommend(movie_name):
    response_json = modelbit.get_inference(
        region="ap-south-1",
        workspace="mustafaansari",
        deployment="recommend",
        data=movie_name
    )
    data_list = response_json['data']
    df = pd.DataFrame(data_list)
    return df

# Add an example for the UI
examples = [
    ["The Dark Knight"],
    ["Inception"],
    ["Interstellar"]
]

gr.Interface(fn=recommend, inputs="text", outputs=gr.DataFrame(), title="Hollywood Movie Recommendation System",
    description="Enter a Hollywood movie name, and this system will recommend similar movies based on your input.",
    examples=examples  # Add examples to the UI
).launch()
