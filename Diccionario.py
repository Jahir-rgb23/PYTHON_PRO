meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "XD": "respuesta a algo gracioso",
            }
            
palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")     

if palabra in meme_dict.keys():
   print(meme_dict[palabra])
else:
   print("Lo siento la palabra no se encuentra en el diccionario")
