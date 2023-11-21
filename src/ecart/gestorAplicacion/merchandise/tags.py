from enum import Enum

"""
En esta clase se encuentran las representaciones graficas de las distintas categorias o etiquetas
estan dadas por emojis que generalizar el ambito cotidiano al que simulan pertenecer.


Método de Clase get_list:
Retorna una lista con los valores de todas las categorías definidas en la enumeración.


Método de Clase get_entry_for_tag:
Recibe el valor de una categoría (tag_value) y retorna la entrada correspondiente en la enumeración (Tags). 
Si no encuentra una coincidencia, retorna None
"""


class Tags(Enum):
    ALIMENTOS = "🍎"
    HOGAR = "🏡"
    LIMPIEZA = "🧹"
    ELECTRODOMESTICOS = "📺"
    JUGUETES = "🎠"

    @classmethod
    def get_list(cls):
        return [tag.value for tag in cls]

    @classmethod
    def get_entry_for_tag(cls, tag_value):
        for tag in cls:
            if tag.value == tag_value:
                return tag
        return None
