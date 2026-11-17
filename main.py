
import cv2
import face_recognition
import os

# Pasta com as imagens cadastradas
PASTA_ROSTOS = "rostos"

# Listas para armazenar os rostos conhecidos
rostos_conhecidos = []
nomes_conhecidos = []

# =====================================
# 1. CARREGAR ROSTOS CADASTRADOS
# =====================================

for arquivo in os.listdir(PASTA_ROSTOS):

    caminho = os.path.join(PASTA_ROSTOS, arquivo)

    if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):

        imagem = face_recognition.load_image_file(caminho)

        codificacoes = face_recognition.face_encodings(imagem)

        if len(codificacoes) > 0:

            rostos_conhecidos.append(codificacoes[0])

            nome = os.path.splitext(arquivo)[0]
            nomes_conhecidos.append(nome)

            print(f"Rosto cadastrado: {nome}")

        else:
            print(f"Nenhum rosto encontrado em: {arquivo}")


if not rostos_conhecidos:
    raise RuntimeError("Nenhum rosto válido foi cadastrado na pasta rostos.")


# =====================================
# 2. INICIAR A WEBCAM
# =====================================

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Não foi possível acessar a webcam.")

print("Reconhecimento facial iniciado!")
print("Pressione Q para encerrar.")


# =====================================
# 3. PROCESSAR OS FRAMES
# =====================================

while True:

    sucesso, frame = camera.read()

    if not sucesso:
        print("Erro ao capturar imagem.")
        break

    # Reduzir tamanho para melhorar desempenho
    frame_pequeno = cv2.resize(
        frame,
        (0, 0),
        fx=0.25,
        fy=0.25
    )

    # OpenCV utiliza BGR, face_recognition utiliza RGB
    frame_rgb = cv2.cvtColor(
        frame_pequeno,
        cv2.COLOR_BGR2RGB
    )

    # Detectar rostos
    localizacoes = face_recognition.face_locations(frame_rgb)

    # Gerar codificações faciais
    codificacoes = face_recognition.face_encodings(
        frame_rgb,
        localizacoes
    )

    # =================================
    # 4. COMPARAR OS ROSTOS
    # =================================

    for codificacao, localizacao in zip(
        codificacoes,
        localizacoes
    ):

        distancias = face_recognition.face_distance(
            rostos_conhecidos,
            codificacao
        )

        melhor_indice = distancias.argmin()

        if distancias[melhor_indice] <= 0.50:
            nome = nomes_conhecidos[melhor_indice]
        else:
            nome = "Desconhecido"

        # Recuperar coordenadas do rosto
        topo, direita, baixo, esquerda = localizacao

        # Como reduzimos o frame para 25%,
        # precisamos multiplicar as coordenadas por 4
        topo *= 4
        direita *= 4
        baixo *= 4
        esquerda *= 4

        # Desenhar retângulo
        cv2.rectangle(
            frame,
            (esquerda, topo),
            (direita, baixo),
            (0, 255, 0),
            2
        )

        # Exibir nome
        cv2.putText(
            frame,
            nome,
            (esquerda, topo - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    # Exibir imagem
    cv2.imshow(
        "Sistema de Reconhecimento Facial",
        frame
    )

    # Encerrar com Q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# =====================================
# 5. FINALIZAR
# =====================================

camera.release()
cv2.destroyAllWindows()

print("Sistema encerrado.")
