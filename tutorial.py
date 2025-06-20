import requests
from typing import List, Dict
from sqlalchemy import Column, String, Float, Date
from time import sleep
from datetime import datetime

# Inicialização das extensões
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

# Coloque a string de conexção do seu banco aqui!
engine = create_engine('mysql+pymysql://root:admin@localhost/pedidos_tiny_tutorial', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# Definindo a classe Pedido no banco
class Pedido(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True)
    numero = Column(String(150))
    numero_ecommerce = Column(String(150), nullable=True)
    data_pedido = Column(Date)
    data_prevista = Column(Date, nullable=True)
    nome = Column(String(150))
    valor = Column(Float)
    id_vendedor = Column(String(150))
    situacao = Column(String(150))
    codigo_rastreamento = Column(String(150), nullable=True)
    url_rastreamento = Column(String(150), nullable=True)

Base.metadata.create_all(engine)

def get_pedidos(pagina: int = 1) -> List[Dict]:
    # Buscar todos os pedidos da API

    url = "https://api.tiny.com.br/api2/pedidos.pesquisa.php"
    params = {
        "token": os.getenv("TOKEN_TINY"),
        "formato": "json",
        "pagina": pagina
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        if data.get("retorno"):
            return data["retorno"]["pedidos"]
        return []
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar pedidos: {e}")
        return []

def parse_pedido(pedido_data: Dict) -> Pedido:
    return Pedido(
        numero=pedido_data["numero"],
        numero_ecommerce=pedido_data["numero_ecommerce"],
        data_pedido=datetime.strptime(pedido_data["data_pedido"], "%d/%m/%Y").strftime("%Y-%m-%d"),
        data_prevista=datetime.strptime(pedido_data["data_prevista"], "%d/%m/%Y").strftime("%Y-%m-%d") if pedido_data["data_prevista"] else None,
        nome=pedido_data["nome"],
        valor=float(pedido_data["valor"]),
        id_vendedor=pedido_data["id_vendedor"],
        situacao=pedido_data["situacao"],
        codigo_rastreamento=pedido_data["codigo_rastreamento"],
        url_rastreamento=pedido_data["url_rastreamento"]
    )   

def fetch_all_pedidos_and_insert():
    # Buscar todos os pedidos da API
    pagina = 1
    while pagina <= 10:
        print(f"Buscando página {pagina}")

        sleep(2)
        pedidos_data = get_pedidos(pagina)
        if not pedidos_data:
            break
   
        for pedido_data in pedidos_data:
            pedido_extrated = pedido_data['pedido']
            pedido = parse_pedido(pedido_extrated)
            insert_pedido(pedido)

        pagina += 1


def insert_pedido(pedido: Pedido) -> None:
    try:
        # Adiciona todos os pedidos na sessão
        session.add(pedido)
        
        # Comita as alterações
        session.commit()
        print("Pedido inserido com sucesso!")
        
    except Exception as e:
        # Se houver erro, faz rollback para manter a integridade do banco
        session.rollback()
        print(f"Erro ao inserir pedido: {e}")
        
    finally:
        # Fecha a sessão
        session.close()


if __name__ == "__main__":
    fetch_all_pedidos_and_insert()


