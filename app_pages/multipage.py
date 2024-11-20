import streamlit as st


class MultiPage:
    
    """
    self.pages:
    Creates an empty list to store all the app pages
    self.app_name:
    Stores the app´s name
    self.default_page:
    Default page when app starting
    
    st.set_page_config:
    Puts the apps name as browsers title 
    adds icon to the browser head    
    """
    def __init__(self, app_name, default_page=None) -> None:
        self.pages = []
        self.app_name = app_name
        self.default_page = default_page
        
        st.set_page_config(
            page_title = self.app_name,
            page_icon = "🌻"
        )
    
    
    # Adds every page with their function as a list in a dictionary
    def add_page(self, title, func) -> None:
        self.pages.append({'title': title, 'function': func})
    
    
    """
    st.title(self.app_name):
    Shows the apps name on top of the page
    
    page:
    Creates a menu at the sidebar with:
    - 'Menu' as title
    - a list of all the pages (self.pages)
    - the pages name in the menu (format_func)
    
    page['function']():
    - runs the function that belongs to the default_page
    """
    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func = lambda page: page['title'])
        
        if self.default_page and not page:
            page = self.default_page
            
        page['function']()