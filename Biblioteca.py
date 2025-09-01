
# Importando a biblioteca uuid para gerar IDs únicos para os livros.
import uuid

# --- Classe Livro ---
class Livro:
    """
    Representa um livro com atributos privados:
    - título
    - autor
    - id_livro (um identificador único)
    """

    def __init__(self, titulo, autor):
        # Construtor da classe, inicializando os atributos privados.
        self.__titulo = titulo
        self.__autor = autor
        # Gerando um ID único para cada livro.
        self.__id_livro = str(uuid.uuid4())

    # Métodos públicos para acessar os atributos (getters).
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_id_livro(self):
        return self.__id_livro

    # Métodos públicos para modificar os atributos (setters).
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def set_autor(self, novo_autor):
        self.__autor = novo_autor

    def __str__(self):
        # Método para representação em string do objeto Livro,
        # útil para exibir informações de forma clara.
        return f'Título: {self.__titulo}, Autor: {self.__autor}, ID: {self.__id_livro}'

# --- Classe Usuario ---
class Usuario:
    """
    Representa um usuário com atributos:
    - nome
    - matricula (privado)
    - livros_emprestados (uma lista de objetos Livro)
    """

    def __init__(self, nome, matricula):
        # Construtor da classe, inicializando os atributos.
        self.nome = nome
        self.__matricula = matricula  # Atributo privado.
        self.livros_emprestados = []

    # Métodos para acessar e modificar a matrícula (encapsulamento).
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, nova_matricula):
        # Proteção para garantir que a matrícula não seja um valor vazio.
        if nova_matricula:
            self.__matricula = nova_matricula
        else:
            print("Erro: A matrícula não pode ser vazia.")

    # Método para realizar o empréstimo de um livro.
    def emprestar_livro(self, livro):
        # Adiciona o objeto Livro à lista do usuário.
        self.livros_emprestados.append(livro)
        print(f'{self.nome} emprestou o livro "{livro.get_titulo()}".')

    # Método para realizar a devolução de um livro.
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            # Remove o objeto Livro da lista do usuário.
            self.livros_emprestados.remove(livro)
            print(f'{self.nome} devolveu o livro "{livro.get_titulo()}".')
        else:
            print(f'Erro: O usuário {self.nome} não tem o livro "{livro.get_titulo()}" emprestado.')

    def __str__(self):
        # Retorna uma representação em string do objeto Usuario.
        lista_titulos = [livro.get_titulo() for livro in self.livros_emprestados]
        return f'Usuário: {self.nome}, Matrícula: {self.__matricula}, Livros Emprestados: {", ".join(lista_titulos)}'


# --- Exemplo de Uso ---
print('--- Demonstrando o uso das classes ---')

# 1. Criação dos livros
livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien')
livro2 = Livro('1984', 'George Orwell')
livro3 = Livro('Cem Anos de Solidão', 'Gabriel García Márquez')

print('\nInformações dos livros criados:')
print(livro1)
print(livro2)
print(livro3)

# 2. Criação do usuário
usuario1 = Usuario('João da Silva', 'M2025001')

# 3. Acessando a matrícula de forma segura
print(f'\nMatrícula do usuário {usuario1.nome}: {usuario1.get_matricula()}')

# 4. Empréstimos e devoluções
print('\n--- Empréstimos e devoluções ---')
usuario1.emprestar_livro(livro1)
usuario1.emprestar_livro(livro2)
print(f'Livros emprestados por {usuario1.nome}: {usuario1.livros_emprestados}')

print(f'\nEstado atual do usuário após empréstimos:')
print(usuario1)

usuario1.devolver_livro(livro1)
usuario1.devolver_livro(livro3) # Tentativa de devolver um livro que não foi emprestado

print(f'\nEstado atual do usuário após devolução:')
print(usuario1)

# 5. Tentativa de modificar um atributo privado diretamente (não é possível)
try:
    print('\nTentando modificar a matrícula diretamente...')
    usuario1.__matricula = 'M2025999'
except AttributeError as e:
    print(f'Erro: Não é possível acessar o atributo diretamente. {e}')

# 6. Modificando a matrícula usando o método público (setter)
print(f'\nModificando a matrícula usando o método set_matricula()...')
usuario1.set_matricula('M2025100')
print(f'Nova matrícula do usuário {usuario1.nome}: {usuario1.get_matricula()}')