## caminho feliz
* saudacao
  - utter_saudacao
* afirmacao
  - action_cardapio
* comprar
  - action_comprar
* carrinho
  - action_carrinho
* finalizar
  - action_carrinho
  - action_resumo
* afirmacao
  - action_finalizar
  - utter_possoajudar
* negacao
  - utter_despedida

## caminho triste
* saudacao
  - utter_saudacao
* negacao
  - utter_despedida

## estória 1
* saudacao
    - utter_saudacao
* comprar{"produto":"pastel","number":1}
  - action_comprar
* comprar
  - action_comprar
* carrinho
  - action_carrinho
* despedida
  - utter_despedida

## compra rápida
* comprar
  - action_comprar
* finalizar
  - action_carrinho
  - action_resumo
* afirmacao
  - action_finalizar
  - utter_possoajudar
* negacao
  - utter_despedida

## compra errada
* comprar
  - action_comprar
* cardapio
  - action_cardapio
* comprar
  - action_comprar
* finalizar
  - action_carrinho
  - action_resumo
* afirmacao
  - action_finalizar
  - utter_possoajudar
* negacao
  - utter_despedida

## volta ao menu
* comprar
  - action_comprar
* finalizar
  - action_carrinho
  - action_resumo
* negacao
  - utter_possoajudar

## comprar
* comprar
  - action_comprar

## você é um bot?
* desafio
  - utter_eusouumbot

## gerar número aleatório
* aleatorio
  - action_aleatorio

## despedida
* despedida
  - utter_despedida