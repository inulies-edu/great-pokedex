from pyodide.http import pyfetch
from pyodide.ffi import create_proxy
from js import console, document, alert
import asyncio

number = document.getElementById('pokemon-number')
image = document.getElementById('pokemon-img')
name = document.getElementById('pokemon-name')
form = document.getElementById('form')

next_btn = document.getElementById('btn-next')
prev_btn = document.getElementById('btn-prev')

image.style.display = 'none'
current_pokemon = 1

async def fetch_pokemon(id):
    response = await pyfetch(url=f"http://127.0.0.1:5000/api/{id}", method="GET")
    output = await response.json()
    return output

async def render_pokemon(id):
    global current_pokemon

    number.innerHTML = ''
    image.style.display = 'none'
    name.innerHTML = 'Carregando'
    
    response = await fetch_pokemon(id)

    if response:
        number.innerHTML = response['id']
        image.src = response['image']
        image.style.display = 'block'
        name.innerHTML = response['name']
        current_pokemon = response['id']
    else:
        number.innerHTML = ''
        image.style.display = 'none'
        name.innerHTML = 'Não Encontrado'
    
  
async def next_pokemon():
    global current_pokemon
    next = current_pokemon + 1
    if next >= 3:
        await render_pokemon(1)
    else:
        await render_pokemon(next)
    return



        
    return

class Pokedex():
    def __init__(self):
        self.search_pokemon_proxy = create_proxy(self.search_pokemon)
        self.next_pokemon_proxy = create_proxy(self.next_pokemon)
        self.previous_pokemon_proxy = create_proxy(self.previous_pokemon)
        form.addEventListener('submit', self.search_pokemon_proxy)
        next_btn.addEventListener('click', self.next_pokemon_proxy)
        prev_btn.addEventListener('click', self.previous_pokemon_proxy)
        
    
    async def search_pokemon(self, pointerEventObj):
        element = document.getElementById('input-search')
        input_value = int(element.value)
        element.value = ''
        await render_pokemon(input_value)

    async def next_pokemon(self, pointerEventObj):
        global current_pokemon
        next = current_pokemon + 1
        if next >= 3:
            await render_pokemon(1)
        else:
            await render_pokemon(next)

    async def previous_pokemon(self, pointerEventObj):
        global current_pokemon
        prev = current_pokemon - 1
        if prev <= 0:
            await render_pokemon(2)
        else:
            await render_pokemon(prev)
    
    def shutdown(self):
        self.search_pokemon_proxy.destroy()

pokedex = Pokedex()
# Make sure in the program to keep holding a reference of klass ...
# do the whole program here
# When all done, call klass.shutdown()


render_pokemon(current_pokemon)

