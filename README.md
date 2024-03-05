# Conversor de Moeda

Este é um sistema de conversão de moeda desenvolvido em Django, que permite aos usuários converter valores entre diferentes moedas com base nas taxas de câmbio atualizadas.

## Funcionalidades

- Conversão de valores entre diferentes moedas.
- Suporte às seguintes moedas:
  - USD (Dólar dos Estados Unidos)
  - BRL (Real Brasileiro)
  - EUR (Euro)
  - BTC (Bitcoin)
  - ETH (Ethereum)
- Fácil integração com serviços de cotação de moedas para obter taxas de câmbio atualizadas.

## Configuração do Ambiente de Desenvolvimento

Para configurar o ambiente de desenvolvimento e executar o sistema localmente, siga estas etapas:

1. Clone este repositório para o seu ambiente de desenvolvimento:
 
   ```bash
   git clone https://github.com/Wsanbey/CurrencyConverterAPI.git
  
   ```

2. Instale as dependências do projeto:

   ```bash
   cd CurrencyConverterAPI
   pip install -r requirements.txt
   ```

3. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

5. Acesse o sistema no seu navegador web em `http://localhost:8000`.

## Uso

Para usar o sistema, você pode acessar a interface web fornecida e seguir as instruções para realizar as conversões monetárias. Além disso, você pode interagir com a API diretamente usando as seguintes endpoints:

- `GET /convert`: Endpoint para realizar a conversão monetária.
  - Parâmetros:
    - `from`: Moeda de origem (ex: `from=BTC`).
    - `to`: Moeda de destino (ex: `to=USD`).
    - `amount`: Valor a ser convertido (ex: `amount=1.0`).

## Falhas Identificadas

Até o momento, foram identificadas as seguintes falhas no sistema:

1. O sistema aceita moedas inválidas e não fornece uma validação adequada para as moedas de origem e destino. Por exemplo, a requisição com moedas inválidas `BRsdgsdgsadg` e `USDkk` foi processada sem retornar erros.
2. A taxa de câmbio usada para realizar a conversão monetária é uma taxa fixa (1.5), o que não reflete a realidade e não fornece resultados precisos.

## Melhorias Necessárias

Para corrigir as falhas identificadas e melhorar o sistema, as seguintes melhorias são necessárias:

1. Implementar validação para as moedas de origem e destino, garantindo que apenas moedas válidas sejam aceitas pelo sistema.
2. Integrar o sistema com um serviço de cotação de moedas para obter taxas de câmbio atualizadas e precisas.
3. Refatorar a lógica de conversão monetária para usar as taxas de câmbio reais obtidas do serviço de cotação de moedas.

## Contribuição

Se você deseja contribuir para o desenvolvimento deste projeto, siga estas etapas:

1. Faça um fork deste repositório.
2. Crie uma branch com a sua feature ou correção de bug: `git checkout -b feature/nova-feature`.
3. Faça suas alterações e adicione os arquivos modificados: `git add .`
4. Faça um commit com suas alterações: `git commit -m "Descrição da sua alteração"`
5. Faça um push para a sua branch: `git push origin feature/nova-feature`
6. Abra um Pull Request neste repositório.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
 
