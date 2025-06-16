# HeavyControl - Sistema de Gestão de Máquinas Pesadas e Caminhões

O HeavyControl é uma plataforma online que permite a criação e gestão de maquinários pesados e caminhões, focada na automatização e otimização de processos. O sistema será acessível via web e dispositivos móveis, oferecendo funcionalidades como: controle de manutenção, coleta de dados através das atividades realizadas pelos funcionários, emissão de relatórios e histórico de máquinas.

---

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Paradigmas e Padrões de Programação](#paradigmas-e-padrões-de-programação)
- [Como Executar Localmente](#como-executar-localmente)

---

## Sobre o Projeto

O HeavyControl visa melhorar a organização interna do setor de Pavimentação da GEES, permitindo o controle otimizado das máquinas pesadas. 

O projeto segue os requisitos especificados no documento SRS disponível no link: https://drive.google.com/file/d/1IMJn-kGLPQea8f29Ayj0KpQvLXlTpqZs/view?usp=drive_link

---

## Tecnologias Utilizadas

- **Backend:** Django
- **Frontend:** HTML5, CSS3 e Bootstrap5
- **Exportação PDF:** WeasyPrint
- **Exportação Excel:** Pandas / openpyxl

---

## Paradigmas e Padrões de Programação

- **Paradigma Principal:** Programação Orientada a Objetos (POO)
- **Design Patterns Aplicados:** Seguido pela arquitetura padrão do Django
- **Boas Prátivas:**
    - Separação de responsabilidades
    - Uso de formulários Django (forms.py)
    - Templates com filtros e blocos reutilizáveis
    - URLs amigáveis com o Django URLs dispatcher

---

## Como Executar Localmente

### Pré-requisitos:

- Python 3.8 ou superior
- Pip

### Passos:

#### 1. Clone o repositório
#### 2. Crie um ambiente virtual
#### 3. Instale as dependências (requirements.txt)
#### 4. Realize as migrações
#### 5. Crie um superusuário (para acessar o admin e por cadastrar novos usuários)
#### 6. Execute o servidor