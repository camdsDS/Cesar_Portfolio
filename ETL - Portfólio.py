#!/usr/bin/env python
# coding: utf-8

# #### Importando bibliotecas

# In[1]:


import sqlalchemy
import pandas as pd


# #### Criando engine de origem

# In[2]:


engine_origem = sqlalchemy.create_engine("mssql+pyodbc://usuario_prd:123456@./PORTFOLIO_PRD?driver=SQL Server")


# #### Importando tabelas do SQL Server

# In[3]:


pedidos = pd.read_sql(sql='SELECT * FROM pedidos', con=engine_origem)
produtos = pd.read_sql(sql='SELECT * FROM produtos', con=engine_origem)
lojas = pd.read_sql(sql='SELECT * FROM lojas', con=engine_origem)


# In[4]:


pedidos.head()


# In[5]:


produtos.head()


# In[6]:


lojas.head()


# #### Tratando as tabelas

# In[7]:


# merge das tabelas
consolidado_dw = pd.merge(left=pedidos, right = produtos, how='left', left_on='produto', right_on='id')
consolidado_dw = pd.merge(left=consolidado_dw, right = lojas, how='left', left_on='loja', right_on='id')


# In[8]:


# dropando colunas que não nos interessa
consolidado_dw.drop(['id_x', 'id_y', 'id', 'produto_x', 'loja'], axis=1, inplace=True)


# In[9]:


# reposionando as colunas
consolidado_dw = consolidado_dw[['produto_y', 'valor', 'data', 'estado', 'cidade', 'logradouro']]


# In[10]:


# renomeando colunas
consolidado_dw.rename(columns={'produto_y':'Produto', 'valor': 'Preço', 'data':'Data','estado':'Estado', 'cidade':'Cidade', 'logradouro':'Endereço'}, inplace=True)


# In[11]:


consolidado_dw.head()


# #### Criando engine de destino

# In[12]:


engine_destino = sqlalchemy.create_engine("postgresql+psycopg2://usuario_dw:123456@localhost/portfolio_DW")


# #### Exportando tabela do Postgre

# In[13]:


# calculando chunksize(cs) máximo
cs = 2097//len(consolidado_dw.columns)
if cs > 1000:
    cs = 1000
else:
    cs=cs


# In[14]:


consolidado_dw.to_sql(name='pedidos', con=engine_destino, if_exists='replace', index=False, chunksize=cs)

