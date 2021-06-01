#!/usr/bin/env python
# coding: utf-8

# # Notebook de exemplo
# 
# <br>description: desc
# <br>author:      name
# <br>email:       mail
# <br>date:        date

# ## Seção Cabeçalho

# In[6]:


import sys
sys.path.insert(0, '../src')

from utils import util
params = util.getParams()


# ### Instructions
# 
# - Evitar a utilização de hardcode. Todos os parametros devem ser inseridos em /config/[env]-config.yaml
# - Todos os parametros são carregados automaticamente dentro da variável "params"

# ## Seção Desenvolvimento

# In[9]:


def bark():
    print(params)


# In[ ]:




