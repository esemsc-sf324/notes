import ipywidgets as widgets
from IPython.display import display, Markdown
import os

if not os.path.exists("notes"):
    os.makedirs("notes")

note_index = 1 

def create_note():

    text_area = widgets.Textarea(
        value='',
        placeholder='请输入笔记内容',
        description='📝 笔记:',
        layout=widgets.Layout(width='500px', height='100px')
    )

    # text_area.layout.border = '2px solid black' 
    # text_area.layout.background_color = '2px solid darkgray' 
    # text_area.style = {'font_weight': 'bold'}  
    def on_button_click(b):
        global note_index
        note_content = text_area.value.replace('\n', '<br>')
        file_name = f"notes/note_{note_index}.md"
        note_index += 1
        
        # 将笔记保存为文件
        with open(file_name, 'w') as f:
            f.write(f"## 📝 Note:<br>{note_content}")

        display(Markdown(f"## 📝 Note:<br>{note_content}"))
        display(Markdown(f"笔记已保存为文件: {file_name}"))

    button = widgets.Button(description="保存笔记")
    button.on_click(on_button_click)

    display(text_area, button)


    # def on_button_click(b):
    #     note_content = text_area.value
    #     note_content = note_content.replace('\n', '<br>')
    #     display(Markdown(f"## 📝 Note:<br>{note_content}"))

 




# import ipywidgets as widgets
# from IPython.display import display, Markdown

# def create_note():

#     text_area = widgets.Textarea(
#         value='',
#         placeholder='请输入笔记内容',
#         description='📝 笔记:',
#         layout=widgets.Layout(width='500px', height='100px')
#     )

#     # text_area.layout.border = '2px solid black' 
#     # text_area.layout.background_color = '2px solid darkgray' 
#     # text_area.style = {'font_weight': 'bold'}  

#     def on_button_click(b):
#         note_content = text_area.value
#         note_content = note_content.replace('\n', '<br>')
#         display(Markdown(f"## 📝 Note:<br>{note_content}"))

#     button = widgets.Button(description="生成笔记")
#     button.on_click(on_button_click)

#     display(text_area, button)




