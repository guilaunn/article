from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Definição da estrutura básica do artigo
class ArticleBase(BaseModel):
    title: str
    body: str
    author: str
    category: str
    published_date: Optional[datetime] = None

# Estrutura para a criação de um novo artigo
class ArticleCreate(ArticleBase):
    pass

# Estrutura para a atualização de um artigo existente
class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    published_date: Optional[datetime] = None

# Estrutura para a leitura de um artigo armazenado no banco de dados
class ArticleInDB(ArticleBase):
    id: int

    class Config:
        orm_mode = True

# Estrutura para a resposta quando um artigo é retornado pela API
class Article(ArticleInDB):
    pass