# Sumo-Traci

~Arquivos:

$ bib.py - Arquivo com a definição de funções úteis criadas para a utilização com o Traci.

$ turnprob.py - Programa em python que utiliza as funções definidas para inserir veículos até que o número de veículos na simulação seja maior ou igual a 1000. 

-Pasta circular/

$ circualr.flow.xml - Arquivo com a definição dos flows para a geração de demanda, omitindo os sinks que serão definidos pelo routing by turn probabilities.

$ circular.net.xml - Arquivo com a definição da rede circular.

$ circular.turns.xml - Arquivo com a definição das probabilidades de virada em cada junction.

$ circular.rou.xml - Arquivo de rotas gerado pelo jtrrouter utilizando routing by turn probabilities.

*Comando para a geração do arquivo de rotas circular.rou.xml

jtrrouter --flow-files=circular.flow.xml --turn-ratio-files=circular.turns.xml --net-file=circular.net.xml --output-file=circular.rou.xml

*Problemas:

Ocasionalmente o programa turnprob.py não funciona devidamente e falha ao inserir veículos com as rotas geradas pelo turn probabilities.

