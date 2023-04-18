from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Action_Sabores_Pizzas(Action):

    def name(self) -> Text:
        return "action_sabores_pizzas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #Recebendo os valores dos slots:
        sabores = tracker.get_slot('pedido_pizza')
        qtde = tracker.get_slot('qtde_pizza')

        #Caso haja mais sabores do que qtdes:
        while(len(sabores)>len(qtde)):
            qtde.append('uma')
        
        #Caso haja mais qtdes do que sabores:
        inv_lista = True
        while(len(sabores)<len(qtde)):
            if(inv_lista == True):
                qtde.reverse()
                inv_lista = False
            qtde.pop()

        #Respondendo ao usuário os sabores e qtdes:
        for i in range(len(sabores)):
            dispatcher.utter_message(text="\n - "+ str(qtde[i])+ " pizza(s) de " + str(sabores[i]))
        dispatcher.utter_message(text="Favor, confirmar com sim ou não")
        
        return []
