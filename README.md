# Controle de Plantas

# Definição do tema e estrutura dos dados 
O Tema foi escolhido na melhor necessidade de organização e controle de plantas ornamentais, frutífera, remédio e sua localização, tanto para residência urbana quanto rural, o sistema conta com o nome, tipo, local e frequência de rega facilitando o controle de cuidados para cada tipo de planta. Foi pensado futuramente em ter um controle mais especifico e detalhado dos métodos principais utilizando rotação de cultura o uso de herbicidas e as funções da lavoura. 
Entretanto o sistema é de simples acesso somente para ter uma organização e controle de cada planta em suas áreas.

O sistema contém:

Dicionário: chaves de ID, nome, tipo, local e frequência de rega.

Lista: Armazenando todos os dicionários.

# Persistência JSON
Para que os dados não fossem apagados foram implementados as funções:
Carregar: Usa biblioteca json para ler o arquivo, se o arquivo não existir ele retorna uma lista vazia.

Salvar lista: Escreve no arquivo json com indent=4.

# Implementação das funções CRUD
Criar: Solicita os dados do usuário gerando um ID automático, baseado na quantidade de criação de plantas e faz um append na lista.

Listar: Percorre a lista com um laço e imprime os dados.

Ler(ID): Percorre a lista procurando a chave de id digitado.

Atualizar: Localiza pelo ID permitindo que o usuário informe novos atualizações no campo desejado ou que mantenha as mesmas informações.

Deletar: Localiza o item da lista removendo usando lista.remove.

# Menu interativo
A função menu contém um laço while True, exibindo as opções de escolha do usuário e do número correspondido, a opção 0 quebra o laço e encerra o programa.

# Tratamento de erros
Try/except: Essa funçaõ evita que o programa trave se o usuário digitar uma letra no lugar do ID.

Verificação: Antes de atualizar o sistema verifica se o ID existe.


