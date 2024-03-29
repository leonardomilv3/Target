# Target
Desafios do Processo Seletivo da Empresa Target.


## Perguntas

1) Observe o trecho de código abaixo: 

 	int INDICE = 13, SOMA = 0, K = 0; 

 	enquanto K < INDICE faça 

	{ 

		K = K + 1; 

		SOMA = SOMA + K; 

	} 

 	imprimir(SOMA); 

  

Ao final do processamento, qual será o valor da variável SOMA? 

  

 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

  

IMPORTANTE:  

	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 

   

3) Descubra a lógica e complete o próximo elemento:  

   

a) 1, 3, 5, 7, ___  

b) 2, 4, 8, 16, 32, 64, ____  

c) 0, 1, 4, 9, 16, 25, 36, ____  

d) 4, 16, 36, 64, ____  

e) 1, 1, 2, 3, 5, 8, ____  

f) 2,10, 12, 16, 17, 18, 19, ____  

   

4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

   

5) Escreva um programa que inverta os caracteres de um string. 


IMPORTANTE: 

	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

	b) Evite usar funções prontas, como, por exemplo, reverse; 


## Respostas

Resposta da questão 1:

- Resposta: 91

Este pseudocódigo é um exemplo de um loop em uma linguagem de programação. Ele inicializa três variáveis: INDICE com o valor 13, SOMA com o valor 0 e K com o valor 0. Em seguida, ele entra em um loop enquanto K for menor que INDICE.

Dentro do loop, a cada iteração, K é incrementado em 1 e SOMA é atualizado somando o valor de K. Este processo continua até que K seja igual a INDICE, momento em que o loop termina.

O valor final de SOMA será a soma de todos os números de 1 até 13, ou seja, 1 + 2 + 3 + ... + 13. Para este caso, o valor impresso será 91.

Resposta da questão 2:

- [questão 2](/questao2.py)

Resposta da questão 3:

a) 1, 3, 5, 7, **9**.

Letra a, sequencia de 2 em 2.

b) 2, 4, 8, 16, 32, 64, **128**.  

Letra b, sequencia de 2 elevado a n.

c) 0, 1, 4, 9, 16, 25, 36, **49**.

Letra c, sequencia de quadrados perfeitos.

d) 4, 16, 36, 64, **100**.  

Letra d, sequencia de quadrados dos numeros naturais, 2^2 , 4^4, 6^6, 8^8.

e) 1, 1, 2, 3, 5, 8, **13**.

Letra e, sequencia de fibonacci.

f) 2, 10, 12, 16, 17, 18, 19, **20**. 

Resposta da questão 4:

Primeira ida:
- Ligue o primeiro interruptor e espere alguns minutos.
- Depois, desligue o primeiro interruptor e ligue o segundo interruptor.
- Em seguida, entre na sala onde está a lâmpada correspondente aos interruptores 1 e 2.

Segunda ida:
- Neste momento, você estará na sala com a lâmpada acesa.
- Sinta a temperatura das lâmpadas ou olhe se estão acesas. A lâmpada que estiver acesa corresponderá ao último interruptor ligado antes de você entrar na sala.
- A lâmpada que ainda estiver apagada será a que corresponde ao interruptor que não foi usado.


Resposta da questão 5:

- [questão 5](/questao5.py)

