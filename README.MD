# Sistema de Reconhecimento Facial

Projeto acadêmico desenvolvido para a disciplina de Visão Computacional, utilizando Python, Dlib e OpenCV para detecção e reconhecimento facial por meio de uma webcam.

O sistema permite cadastrar pessoas através de fotografias capturadas pela câmera e identificar rostos previamente cadastrados durante a execução do reconhecimento facial.

## 1. Funcionalidades

- Cadastro de pessoas por meio da webcam.
- Armazenamento das fotografias cadastradas.
- Detecção facial em tempo real.
- Reconhecimento de pessoas previamente cadastradas.
- Identificação de rostos não cadastrados como "Desconhecido".
- Exibição dos resultados com caixas delimitadoras.

## 2. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| Dlib | Biblioteca de visão computacional |
| Face Recognition | Detecção e reconhecimento facial |
| OpenCV | Captura e processamento de imagens |
| NumPy | Operações numéricas |
| Matplotlib | Visualização de dados |

## 3. Estrutura do projeto

```text
Apresentação facial/
│
├── main.py
├── cadastrar.py
├── requirements.txt
├── README.md
│
└── rostos/
    ├── clara.jpg
    ├── pessoa2.jpg
    └── pessoa3.jpg
```

## 4. Pré-requisitos

Antes de iniciar a instalação, é necessário possuir:

- Windows 10 ou Windows 11.
- Python.
- Visual Studio Code.
- Git instalado.
- Webcam funcional.
- Arquivo pré-compilado do Dlib disponibilizado pelo professor.

**Importante:** o arquivo `.whl` do Dlib deve ser compatível com a versão do Python e a arquitetura do sistema operacional utilizados.

## 5. Instalação e configuração

### 5.1. Obter o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd "Apresentação facial"
```

Caso tenha recebido o projeto em ZIP, extraia os arquivos e abra a pasta no VS Code.

### 5.2. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 5.3. Ativar o ambiente virtual

```powershell
.venv\Scripts\activate
```

### 5.4. Instalar o Dlib

O professor disponibilizou um arquivo pré-compilado da biblioteca Dlib, no formato `.whl`, para facilitar sua instalação no Windows.

```

Verifique se a instalação foi realizada:

```powershell
python -c "import dlib; print(dlib.__version__)"
```

### 5.5. Instalar as demais dependências

Após instalar o Dlib, execute:

```powershell
python -m pip install --upgrade pip
```

Em seguida:

```powershell
python -m pip install -r requirements.txt
```

**Observação:** a biblioteca `face_recognition_models` é obtida diretamente do GitHub. Por isso, é necessário ter o Git instalado e disponível no terminal.

### 5.6. Verificar a instalação

Execute:

```powershell
python -c "import cv2, dlib, face_recognition, face_recognition_models; print('Ambiente configurado com sucesso!')"
```

Se aparecer a mensagem de sucesso, as principais dependências foram carregadas corretamente.

## 6. Como executar o projeto

O projeto possui dois programas independentes.

### 6.1. Cadastro facial

Para cadastrar uma pessoa, execute:

```powershell
python cadastrar.py
```

O programa solicitará o nome da pessoa e abrirá a webcam.

Passo a passo:

1. Informe o nome da pessoa.
2. Posicione o rosto diante da câmera.
3. Pressione `a` para capturar a fotografia.
4. A imagem será salva automaticamente na pasta `rostos/`.

Para cancelar, pressione `Q`.

### 6.2. Reconhecimento facial

Após realizar os cadastros, execute:

```powershell
python main.py
```

O sistema realizará as seguintes operações:

1. Carregará as fotografias cadastradas.
2. Gerará as codificações faciais.
3. Inicializará a webcam.
4. Detectará os rostos presentes na imagem.
5. Comparará os rostos encontrados com os cadastrados.
6. Exibirá o nome da pessoa identificada ou "Desconhecido".

Para encerrar a execução, pressione `Q`.

## 7. Funcionamento técnico

O reconhecimento facial ocorre por meio de quatro etapas:

**Detecção facial:** identifica a localização dos rostos presentes na imagem.

**Codificação facial:** transforma as características do rosto em uma representação numérica.

**Comparação:** calcula a distância entre a codificação do rosto capturado e as codificações cadastradas.

**Identificação:** verifica se a menor distância está dentro do limite estabelecido no código.

O sistema utiliza inicialmente o limite de distância `0.50`, que pode ser ajustado durante os testes.

Esse valor não representa uma porcentagem de confiança.

## 8. Considerações sobre instalação

O arquivo pré-compilado do Dlib não está incluído no `requirements.txt`, pois sua instalação é realizada separadamente, utilizando o arquivo `.whl` fornecido pelo professor.

A compatibilidade do arquivo depende da versão do Python e da arquitetura do sistema.

Recomenda-se utilizar a mesma versão do Python entre os integrantes do grupo para evitar problemas de instalação.

## 9. Privacidade e uso responsável

As fotografias utilizadas devem ser obtidas com autorização das pessoas envolvidas.

As imagens cadastradas são armazenadas localmente na pasta `rostos/`.

O projeto possui finalidade acadêmica e experimental, não devendo ser utilizado como único mecanismo de autenticação ou identificação de pessoas.

---

**Projeto acadêmico de Visão Computacional**

Desenvolvido com Python, Dlib, Face Recognition e OpenCV.