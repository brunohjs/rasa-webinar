# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from random import randint
import utils

cardapio = {
    "queijo": 4.99,
    "carne": 3.99,
    "camarão": 7,
    "coração": 4.99,
    "calabresa": 4.99,
    "romeu e julieta": 5,
    "chocolate": 5,
    "bacon": 4.5
}

class ActionComprar(Action):
    def name(self) -> Text:
        return "action_comprar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = ''
        quantidade = utils.getNumber(tracker.latest_message['entities'])
        sabor = utils.getFlavor(tracker.latest_message['entities']) 
        carrinho = tracker.get_slot('carrinho')
        if quantidade and sabor:
            if cardapio.get(sabor):
                pastel = {
                    'sabor': sabor,
                    'quantidade': quantidade,
                    'valor': cardapio[sabor]
                }
                if carrinho:
                    carrinho.append(pastel)
                else:
                    carrinho = [pastel]
                text = f"{quantidade} {'pastéis' if quantidade > 1 else 'pastel'} sabor {sabor} adicionado no seu carrinho! O que mais você deseja?"
            else:
                text = f"O sabor {sabor} não está no nosso cardápio ainda...Quer pedir outro sabor?"
        else:
            text = 'Por favor, informe o sabor e a quantidade.'
        dispatcher.utter_message(text=text, buttons=[
                {"title": "Pedir pastel", "payload": "/cardapio"},
                {"title": "Carrinho", "payload": "/carrinho"},
                {"title": "Finalizar pedido", "payload": "/finalizar"},
                {"title": "Sair", "payload": "/despedida"}
        ])
        return [SlotSet("carrinho", carrinho)]


class ActionCarrinho(Action):
    def name(self) -> Text:
        return "action_carrinho"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        carrinho = tracker.get_slot('carrinho')
        text = ''
        total = 0
        if carrinho:
            text += 'Seu carrinho:\n\n'
            for item in carrinho:
                text += f" - {item['quantidade']}x {item['sabor']}: R$ {utils.formatMoney(item['valor'])}\n\n"
                total += item['valor'] * item['quantidade']
            text += f'Total: R$ {utils.formatMoney(total)}'
        else:
            text = 'Seu carrinho está vazio...'
        dispatcher.utter_message(text)
        return []

class ActionCardapio(Action):
    def name(self) -> Text:
        return "action_cardapio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = 'Aqui está nosso cardápio:\n\n'
        for sabor in cardapio:
            text += f' - {sabor}: R$ {utils.formatMoney(cardapio[sabor])}\n\n'
        text += f'Você vai querer qual pastel? Digite sabor e quantidade.'
        dispatcher.utter_message(text)
        return []

class ActionResumo(Action):
    def name(self) -> Text:
        return "action_resumo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Deseja finalizar a compra?")
        return []

class ActionFinalizar(Action):
    def name(self) -> Text:
        return "action_finalizar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Seu pedido foi finalizado! Muito obrigado!")
        return [SlotSet("carrinho", [])]

class ActionAleatorio(Action):
    def name(self) -> Text:
        return "action_aleatorio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        numero = randint(1, 100)
        dispatcher.utter_message(text=f'Seu número é {numero}')
        return []