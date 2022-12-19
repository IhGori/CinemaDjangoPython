# Cinema Django-Python/HTML/JavaScripts/CSS
Criação de aplicação web de um Cinema utilizando framework Django

- Para execução necessário configuração do protocolo SMTP com o Gmail em settings.py de acordo com o e-mail do projeto;
- Esta é uma aplicação mais simples sem utilização do AllAuth, futuramente poderá ser atualizado com uma versão otimizada do projeto.


## Instalação
<br>
<ul>
    <li>Instalação do django: pip install django</li>  
</ul>


## Instalação
<br>
<ul>
    <li>Todos imports para execução podem ser instalados a partir do comando: pip install -r requirements.txt</li> 
    <li>
        Aplicação do mekmigrations (Verificações de alterações nos modelos) e migrate para gerenciar as estruturas das tabelas para com o banco de dados:
        <ul>
            <li>python manage.py makemigrations</li>
            <li>python manage.py migrate</li>
        </ul>
    </li> 
</ul>


## Criação de usuários e superusuários
<br>
Para criação de usuários pode ser feito pelo site de administrador, ou pelo próprio template da página do cinema.
Para criação de um superusuário, deverá ser feito pelo terminal:
    - python manage.py createsuperuser





Creation of a Cinema web application using Django framework

- For execution, it is necessary to configure the SMTP protocol with Gmail in settings.py according to the project's email;
- This is a simpler application without using AllAuth, in the future it may be updated with an optimized version of the project.


## Installation
<br>
<ul>
    <li>Django installation: pip install django</li>
</ul>


## Installation
<br>
<ul>
    <li>All imports for execution can be installed using the command: pip install -r requirements.txt</li>
    <li>
        Applying mekmigrations (Checks for changes in models) and migrate to manage the table structures for the database:
        <ul>
            <li>python manage.py makemigrations</li>
            <li>python manage.py migrate</li>
        </ul>
    </li>
</ul>


## Creating users and superusers
<br>
User creation can be done through the admin site, or through the cinema page template itself.
To create a superuser, use the terminal:
    - python manage.py createsuperuser
