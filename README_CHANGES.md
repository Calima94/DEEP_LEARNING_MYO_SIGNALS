# Modificações no Projeto DEEP_LEARNING_MYO_SIGNALS

## Resumo das Alterações

Foram realizadas duas modificações principais no projeto:

1. **Uso dinâmico do número de canais**: O combobox `cb_raw_signal_1` na tela "Plot Raw Signals" agora usa dinamicamente o número de canais definido em `param_to_use.py` (parâmetro `n_of_channels_and_category`) em vez dos 8 canais fixos anteriores.

2. **Melhoria na estilização da interface**: A interface PyQT5 foi completamente reformulada com um design moderno, incluindo uma nova paleta de cores, estilos para botões, frames, labels e outros elementos.

## Detalhes das Modificações

### 1. Uso Dinâmico do Número de Canais

#### Arquivos Modificados:
- `train_emg_data.py`: Modificado para importar a classe `ParametersToUse` e usar o número de canais definido.
- `main.py`: Atualizado para importar e usar a classe `ParametersToUse`.

#### Alterações Específicas:
- Adicionada a importação da classe `ParametersToUse` no início dos arquivos.
- Criada uma instância da classe `ParametersToUse` para acessar o número de canais.
- Modificado o combobox `cb_raw_signal_1` para adicionar itens dinamicamente com base no número de canais definido.
- Atualizada a função `retranslateUi` para definir o texto dos itens do combobox dinamicamente.

Agora, se o número de canais for alterado no arquivo `parameters.csv` (parâmetro `n_of_channels_and_category`), a interface se adaptará automaticamente, exibindo apenas o número correto de canais no combobox.

### 2. Melhoria na Estilização da Interface

#### Arquivos Modificados:
- `main.py`: Adicionada a função `apply_modern_styling()` e atualizadas as funções de plotagem.

#### Alterações Específicas:
- Adicionada uma nova função `apply_modern_styling()` que aplica estilos modernos a todos os elementos da interface.
- Definida uma paleta de cores consistente para toda a aplicação:
  - Cor primária: `#3498db` (Azul)
  - Cor secundária: `#2c3e50` (Azul escuro/cinza)
  - Cor de destaque: `#e74c3c` (Vermelho)
  - Cor clara: `#ecf0f1` (Cinza claro)
  - Cor escura: `#34495e` (Azul escuro/cinza mais escuro)
- Aplicados estilos específicos para diferentes tipos de elementos:
  - Botões: Cor de fundo azul, texto branco, cantos arredondados, efeitos hover
  - Frames: Cor de fundo branca, bordas sutis, cantos arredondados
  - Labels: Cores consistentes, títulos em negrito
  - Comboboxes e campos de texto: Bordas sutis, efeitos de foco
  - Widgets de árvore: Cores alternadas para linhas, seleção destacada
- Melhoradas as funções de plotagem para usar estilos consistentes:
  - Adicionado fundo branco aos gráficos
  - Melhorada a legibilidade com grades e rótulos mais claros
  - Adicionados títulos em negrito e rótulos de eixos mais legíveis
  - Removidas bordas desnecessárias para um visual mais limpo
  - Adicionadas cores consistentes e atraentes para os gráficos

## Como as Modificações Afetam o Uso

### Uso Dinâmico do Número de Canais
- Agora a interface se adapta automaticamente ao número de canais definido em `parameters.csv`.
- Se você alterar o número de canais em `parameters.csv`, a interface mostrará apenas os canais disponíveis.
- Não há mais necessidade de modificar manualmente o código para adicionar ou remover canais.

### Melhoria na Estilização da Interface
- A interface agora tem uma aparência mais moderna e profissional.
- A navegação é mais intuitiva com botões claramente destacados.
- Os gráficos são mais legíveis e visualmente atraentes.
- A experiência do usuário é mais consistente em toda a aplicação.

## Observações Adicionais

- Todas as funcionalidades originais foram preservadas.
- O código foi organizado para facilitar futuras modificações.
- A estilização pode ser facilmente ajustada modificando as variáveis de cor na função `apply_modern_styling()`.
