from nicegui import ui
from newspaper import Article
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')


"""Update the grid based on the user input."""

def update_grid(article):
    grid.clear()
    with grid:
        with ui.row().classes('w-full flex-center items-center'):
            ui.image(article.top_image).style('width: 70%; height: auto;')
        with ui.row().classes('w-full flex-center items-center'):
            ui.label(article.title).classes('text-3xl font-semibold')
        with ui.row().classes('w-full flex-center items-center'):
            ui.label(article.summary).classes('text-lg')
        with ui.row().classes('w-full'):
            author_text = 'Unknown' if not article.authors else ', '.join(set(article.authors))
            ui.label(f'Author: {author_text}').classes('text-sm opacity-75')
            ui.label(f'Publish Date: {article.publish_date.strftime("%B %d, %Y") if article.publish_date else 'N/A'}').classes('text-sm opacity-75')
        
    

"""Fetch the article from the URL."""
def fetch_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article

"""Handle the submit button action."""

def handle_submit():
    spinner.style('display:block')
    try:
        article = fetch_article(article_input.value)
        update_grid(article)
    except Exception as e:
        print(e)
        dialog.open()
    spinner.style('display:none')


"""Create the UI components."""

ui.page_title('Briefly - Headlines and highlights.')
ui.dark_mode().enable()

with ui.row().classes('pt-8 w-full flex-center items-center'):
    ui.label('Briefly').classes('text-4xl font-semibold font-mono italic').props('font-family: "monaco"')

with ui.row().classes('w-full flex-center items-center gap-4'):
    ui.label('Headlines and highlights.').classes('text-xl mb-4 font-semibold')

with ui.row().classes('w-full flex-center items-center gap-4'):
    article_input = ui.input('Enter Article URL here...').props('clearable').classes('flex-col col-12 col-md-8')

with ui.row().classes('w-full flex-center items-center gap-4'):
    ui.button('Submit', on_click=handle_submit)
    spinner = ui.spinner(size='lg').style('display:none')

with ui.dialog() as dialog, ui.card():
    ui.label('Invalid URL! Please enter a valid article URL. Example: https://www.bbc.com/news/articles/cr40d32zqz4o')
    ui.button('Close', on_click=dialog.close)
    
grid = ui.grid(columns=1).classes('w-full px-48 py-8')

ui.run(host='localhost', port=7777)