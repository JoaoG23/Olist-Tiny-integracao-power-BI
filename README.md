# Integração Tiny com Power BI

Este projeto permite a integração entre o Tiny ERP e o Power BI, facilitando a análise de dados de pedidos.

## Pré-requisitos

- Python 3.8 ou superior
- Conta no Tiny ERP com acesso à API
- MySQL Server instalado localmente
- Power BI Desktop

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/JoaoG23/Olist-Tiny-integracao-power-BI.git
   cd Olist-Tiny-integracao-power-BI
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto com seu token da API do Tiny:
   ```
   TOKEN_TINY=seu_token_aqui
   ```

5. Crie um banco de dados MySQL chamado `pedidos_tiny_tutorial` ou altere a string de conexão no arquivo `tutorial.py`.

## Configuração

1. Execute o script Python para importar os pedidos:
   ```
   python tutorial.py
   ```

2. Abra o arquivo `bi.pbix` no Power BI Desktop.

3. No Power BI, atualize a conexão com o banco de dados MySQL local.

## Uso

- O script irá buscar os pedidos da API do Tiny e armazená-los no banco de dados MySQL.
- O dashboard do Power BI já está configurado para visualizar os dados importados.

## Personalização

Você pode modificar o arquivo `tutorial.py` para incluir mais campos ou ajustar a lógica de importação conforme necessário.

## Solução de Problemas

- Certifique-se de que o MySQL está rodando localmente.
- Verifique se o token da API do Tiny está correto e tem permissões necessárias.
- Em caso de erros de conexão, verifique as credenciais do banco de dados no arquivo `tutorial.py`.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.