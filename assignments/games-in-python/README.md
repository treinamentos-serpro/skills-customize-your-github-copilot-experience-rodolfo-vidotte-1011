
# 📘 Assignment: Jogo da Forca

## 🎯 Objetivo

Implemente um jogo da forca em Python para praticar manipulação de strings, listas, seleção aleatória, loops e condicionais. O jogador deve descobrir uma palavra secreta antes de atingir o limite de tentativas incorretas.

## 📝 Tarefas

### 🛠️ Implementar o Jogo da Forca

#### Descrição
Complete o código inicial para escolher uma palavra aleatoriamente e conduzir uma partida. Mostre as letras já descobertas e peça palpites até o jogador vencer ou esgotar as tentativas.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista `words` fornecida no código inicial.
- Mostrar cada letra ainda não descoberta como `_` e revelar as letras acertadas nas posições correspondentes.
- Aceitar palpites de uma letra e informar se a letra aparece na palavra secreta.
- Acompanhar os palpites incorretos e permitir no máximo seis erros.
- Encerrar a partida quando todas as letras forem descobertas ou quando o jogador atingir o limite de erros.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.

Exemplo de progresso para a palavra `python` após acertar `p` e `o`:

```text
p _ _ _ o _
```